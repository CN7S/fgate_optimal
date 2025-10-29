from .design import Design
from verilog_parser.netlist import Gate, Module, Port, Wire, Instance
import queue
import time
import copy

def get_time(f):

    def inner(*arg,**kwarg):
        s_time = time.time()
        res = f(*arg,**kwarg)
        e_time = time.time()
        print('Used Time : {} s.'.format(e_time - s_time))
        return res
    return inner



class OptEngine() :
    def __init__(self, design : Design):
        self.circuit_design = design
        self.circuit_design.genGateNetwork()
        self.circuit_design.checkGateNetwork()
        self.circuit_design.runSTA(result_log=False)
        self.teriod = 1000 # ps
        self.sim_time = 100000 #ps
        self.cycles = 100
        print('OptEngine Init Successfully.')

    def getPowerCost(self, gate : Gate) :
        return 1 * self.cycles

    def getPowerGain(self, gate : Gate) : 
        return gate.attr.glitch_tr * self.cycles

    @get_time
    def fgate_cutset_opt(self):

        total_glitch = 0
        total_tr = 0

        stats_gain = 0
        stats_cost = 0
        stats_fgate_num = 0

        replace_gate_list = []
        replace_gate_set = {}
        clear_gate_list = []

        gate_id_set = {}
        gate_net = self.circuit_design.getGateNetwork()
        for g in gate_net.gate_dict.values() : 
            gate_id_set[g.name] =  len(g.input_port_driver)
            cost = self.getPowerCost(g)
            gain = self.getPowerGain(g)

            total_glitch = total_glitch + g.attr.glitch_tr
            total_tr = total_tr + g.attr.func_tr

            opt_gain = gain - cost
            if opt_gain > 0 :
                replace_gate_list.append( g )
        
        def clearGate(g):
                for load_list in g.output_port_load.values() : 
                    for out_gate in load_list : 
                        out_gate = out_gate[0]
                        _tmp = gate_id_set[out_gate.name]
                        gate_id_set[out_gate.name] = _tmp - 1
                        if _tmp == 1 : 
                            clear_gate_list.append(out_gate)
                            if out_gate.name in replace_gate_set : 
                                # gate has been replace
                                # undo the replace
                                replace_gate_set.pop(out_gate.name)
                            else : 
                                clearGate(out_gate)
        for g in replace_gate_list : 
            if gate_id_set[g.name] == 0:
                continue
            replace_gate_set[g.name] = g
            clearGate(g)
        for g in replace_gate_set.values() : 
            gain = self.getPowerGain(g)
            cost = self.getPowerCost(g)
            stats_cost = stats_cost + cost
            stats_gain = stats_gain + gain
        
        for g in clear_gate_list : 
            gain = self.getPowerGain(g)
            stats_gain = stats_gain + gain
                

        replece_gain = 0
        stats_fgate_num = len(replace_gate_set)
        for g in replace_gate_set.values() : 
            replece_gain = replece_gain + self.getPowerGain(g)

        
        # test
        influ_node_set = {}
        def set_influence_node(g):
            influ_node_set[g.name] = 1
            for port_list in g.output_port_load.values() :
                for gate_out in port_list : 
                    gate_out = gate_out[0] 
                    set_influence_node(gate_out)
        for g in replace_gate_set.values() :
            set_influence_node(g)

        print('total_tr, total_glitch, stats_cost, stats_gain, replece_gain, fgate_num, clear_gate, influenced gate, gate list')
        print(total_tr)
        print(total_glitch)
        print(stats_cost)
        print(stats_gain)
        print(replece_gain)
        print(stats_fgate_num)
        print(len(clear_gate_list))
        print(len(influ_node_set))
        print([x.name for x in replace_gate_set.values()])

        opt_design = self.circuit_design

        module_tree = opt_design.getModuleTree()
        fen_port_list = {k : [] for k in module_tree.keys()}


        # time calculate
        # def min_time_dfs(gate) : 



        for gate in replace_gate_set.values() : 
            gate_name = gate.name
            module_name = gate_name.split('.')[0]
            gate_name = gate_name.split('.')[1]
            unfreezing_time = 0 # calculate time
            for t in gate.attr.outport_delay_in_network.values() : 
                unfreezing_time = max(unfreezing_time, t)
            fen_port_list[module_name].append([gate_name, unfreezing_time])
        
        def update_pos_info(module_name) :
            unfreezing_time_list = []
            port_wire_connect = []
            enable_port_width = 0

            if not module_name in opt_design.modules : 
                print(f'Error : Module {module_name} not in Lib.')
                return
            module = opt_design.modules[module_name]
            
            for gate_info in fen_port_list[module_name] : 
                unfreezing_time_list.append(gate_info[1])
                port_wire_connect.append([gate_info[0], 1])
                enable_port_width = enable_port_width + 1

            for inst in module.inst_dict.values() : 
                inst_module_name = inst.module
                if inst_module_name in opt_design.modules : 
                    inst_time_list, inst_enport_width = update_pos_info(inst_module_name)
                    enable_port_width = enable_port_width + inst_enport_width
                    port_wire_connect.append([inst.name, inst_enport_width])
                    unfreezing_time_list.extend(inst_time_list)
            

            if enable_port_width == 0 : 
                return unfreezing_time_list, enable_port_width
            # update Inst Module
            # FGATE 
            # Inst Module
            
            for gate_info in fen_port_list[module_name] : 
                gate_inst_name = gate_info[0]
                inst = module.inst_dict[gate_inst_name]
                inst_name = inst.name
                inst_module = inst.module
                fgate_module = 'F' + inst_module
                opt_design.modifyModuleInst(module_name, 
                                            inst_name,
                                            fgate_module,
                                            inst.getPortConnectDict())
            
            for inst in module.inst_dict.values() : 
                inst_module_name = inst.module
                if inst_module_name in opt_design.modules : 
                    opt_design.modifyModuleInst(module_name, 
                                                inst.name,
                                                inst.module,
                                                inst.getPortConnectDict())


            # update Module Design
            # 1. add Port fgate_en in Module
            # 2. connect Port to Inst Port

            opt_design.addModulePort(module_name=module_name, 
                                     port_name='en',
                                     direction=0, # input port
                                     lsb=0,
                                     msb=enable_port_width-1)
            
            port_pos = 0
            for connect_info in port_wire_connect : 
                inst_name = connect_info[0]
                port_width = connect_info[1]
                for i in range(port_width) : 
                    opt_design.connectPortToPort(module_name=module_name,
                                                 a_port_name='self.en',
                                                 a_port_pos=port_pos+i,
                                                 b_port_name=inst_name + '.en',
                                                 b_port_pos=i)
                port_pos = port_pos + port_width
            


            return unfreezing_time_list, enable_port_width

        time_list, _ = update_pos_info(opt_design.top_design)

        def genDelayModule(module_name, clk_period, del_time) :
            new_module = Module(module_name, 
                        port_dict={}, 
                        inst_dict={}, 
                        wire_dict={})
            # in port
            clk_port = Port('clked', 0, 1)
            # out port
            delen_port = Port('del_en', 1, 1)
            new_module.port_dict['clked'] = clk_port
            new_module.port_dict['del_en'] = delen_port
            
            opt_design.modules[module_name] = new_module
            #inst DEL025D1BWP30P140
            # nclked INVD1BWP30P140

            opt_design.addModuleInst(module_name, 'U0', 'INVD1BWP30P140', {})
            opt_design.connectPortToPort(module_name, 'self.clked', 0, 'U0.I', 0)

            half_clk = clk_period // 2
            del_time_per_unit = 15
            if del_time > half_clk :
                del_time = del_time - half_clk
                del_cnt = 2
                opt_design.addModuleInst(module_name, 'U1', 'DEL025D1BWP30P140', {})
                opt_design.connectPortToPort(module_name, 'U0.ZN', 0, 'U1.I', 0)
                del_time = del_time - del_time_per_unit
                while del_time > 0 : 
                    opt_design.addModuleInst(module_name, f'U{del_cnt}', 'DEL025D1BWP30P140', {})
                    opt_design.connectPortToPort(module_name, f'U{del_cnt-1}.Z', 0, f'U{del_cnt}.I', 0)
                    del_time = del_time - del_time_per_unit
                    del_cnt = del_cnt + 1
                opt_design.addModuleInst(module_name, f'U{del_cnt}', 'AN2D1BWP30P140', {})
                opt_design.connectPortToPort(module_name, f'U{del_cnt-1}.Z', 0, f'U{del_cnt}.A1', 0)
                opt_design.connectPortToPort(module_name, 'U0.ZN', 0, f'U{del_cnt}.A2', 0)
                opt_design.connectPortToPort(module_name, f'U{del_cnt}.Z', 0, 'self.del_en', 0)

            else : 
                del_cnt = 2
                opt_design.addModuleInst(module_name, 'U1', 'DEL025D1BWP30P140', {})
                opt_design.connectPortToPort(module_name, 'self.clked', 0, 'U1.I', 0)
                del_time = del_time - del_time_per_unit
                while del_time > 0 : 
                    opt_design.addModuleInst(module_name, f'U{del_cnt}', 'DEL025D1BWP30P140', {})
                    opt_design.connectPortToPort(module_name, f'U{del_cnt-1}.Z', 0, f'U{del_cnt}.I', 0)
                    del_time = del_time - del_time_per_unit
                    del_cnt = del_cnt + 1
                opt_design.addModuleInst(module_name, f'U{del_cnt}', 'OR2D1BWP30P140', {})
                opt_design.connectPortToPort(module_name, f'U{del_cnt-1}.Z', 0, f'U{del_cnt}.A1', 0)
                opt_design.connectPortToPort(module_name, 'U0.ZN', 0, f'U{del_cnt}.A2', 0)
                opt_design.connectPortToPort(module_name, f'U{del_cnt}.Z', 0, 'self.del_en', 0)
            
        with open('time.rpt', 'w') as f: 
            for t in time_list : 
                f.write('{}\n'.format(t))
        
        # Top
        new_top_module = Module(opt_design.top_design + '_opt', 
                        port_dict={}, 
                        inst_dict={}, 
                        wire_dict={})
        for port in opt_design.modules[opt_design.top_design].port_dict.values() :
            new_top_module.port_dict[port.name] = Port(port.name, port.direction, port.type, port.lsb, port.msb) 
        new_top_module.port_dict['clked'] = Port('clked', 0, 1)
        new_top_module.port_dict.pop('en', None)
        opt_design.modules[new_top_module.name] = new_top_module
        opt_design.addModuleInst(new_top_module.name, 'U0', opt_design.top_design, {})
        for port in opt_design.modules[opt_design.top_design].port_dict.values() :
            if port.name in new_top_module.port_dict : 
                for i in range(port.lsb, port.msb + 1) : 
                    opt_design.connectPortToPort(new_top_module.name, 
                                                 f'self.{port.name}', i,
                                                 f'U0.{port.name}', i)

        for i in range(len(time_list)) :
            t = time_list[i]
            genDelayModule(f'delay_unit_{i}', 1100, t)
            opt_design.addModuleInst(new_top_module.name, f'U{i+1}', f'delay_unit_{i}', {})
            opt_design.connectPortToPort(new_top_module.name,
                                         'self.clked', 0,
                                         f'U{i+1}.clked', 0)
            opt_design.connectPortToPort(new_top_module.name, 
                                         f'U{i+1}.del_en', 0,
                                         'U0.en', i)
        opt_design.setTopDesign(new_top_module.name)
        return opt_design

        
        

