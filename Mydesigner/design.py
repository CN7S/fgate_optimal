from verilog_parser import parser
from verilog_parser.netlist import Gate, GateAttr, Module
from saif_parser import saifparse
from .network import NetWork
from . import units
import os
import queue
import copy
class Design : 
    def __init__(self):
        self.modules = {}
        self.gate_lib = {}
        self.gate_net = NetWork()
        self.top_design = ''

    def printModulesLib(self):
        for modules in self.modules : 
            print(modules)

    def addModuleFromFile(self, module_dict, filepath):
        with open(filepath, 'r') as f:
            modulelist = parser.parse(f.read())
        for m in modulelist:
            if m.name in module_dict :
                print(f'Error : Module {m.name} have 1 design in the LIBARAY.')
            else:
                module_dict[m.name] = m
                print(f'Add Module {m.name} Successfully.')
        
    def addModuleFromFloder(self, path):
        files = os.listdir(path)
        for f in files : 
            if f.split('.')[-1] == 'v' :
                self.addModuleFromFile(self.modules, os.path.join(path, f))

    def addGateLibFromFloder(self, path):
        files = os.listdir(path)
        for f in files : 
            if f.split('.')[-1] == 'v' :
                self.addModuleFromFile(self.gate_lib, os.path.join(path, f))

    def dumpModule(self, modulename, path) : 
        units.dumpModule(self.modules[modulename], path)
    
    def dumpAllModule(self, path) : 
        for module in self.modules.values() : 
            units.dumpModule(module=module, filepath=path)


    def setTopDesign(self, top_design):
        self.top_design = top_design
        if not (top_design in self.modules) : 
            print('Error : top_design set error, this design not in the modules lib.')
    
    def uniqueModules(self):
        unique_modules = {}
        unique_modules_cnt = {}
        module_queue = queue.Queue()

        for m in self.modules :
            unique_modules_cnt[m] = 0

        unique_modules_cnt[self.top_design] = 1
        _tmp = copy.deepcopy(self.modules[self.top_design])
        _tmp.name = _tmp.name+f'_0'
        self.top_design = _tmp.name
        module_queue.put(_tmp)

        
        while not module_queue.empty() :
            m = module_queue.get()
            for inst in m.inst_dict.values() :
                inst_module = inst.module
                if inst_module in self.modules :
                    inst_cnt = unique_modules_cnt[inst_module]
                    inst.module = inst_module + f'_{inst_cnt}'
                    unique_modules_cnt[inst_module] = inst_cnt + 1
                    _tmp = copy.deepcopy(self.modules[inst_module])
                    _tmp.name = inst.module
                    module_queue.put(_tmp)
            unique_modules[m.name] = m
        
        self.modules = unique_modules
        #log
        for i in unique_modules_cnt:
            print(f'Unique {unique_modules_cnt[i]} {i} Module.')

    def updateModuleInst(self):
        for module in self.modules.values() : 
            for inst in module.inst_dict.values() : 
                inst_module = inst.module
                if inst_module in self.modules : 
                    inst.port_dict = copy.deepcopy(self.modules[inst_module].port_dict)
                elif inst_module in self.gate_lib : 
                    inst.port_dict = copy.deepcopy(self.gate_lib[inst_module].port_dict)
                else : 
                    print('Error (06) : Cant find Inst Module in Module Lib, Updated Error.')
            
            for wire in module.wire_dict.values() :
                for i in range(wire.lsb, wire.msb+1) :
                    wire_con = [wire.name, i]
                    for p in wire.connect[i] : 
                        port_name = p[0]
                        port_pos = p[1]
                        inst_name = port_name.split('.')[0]
                        port_name = port_name.split('.')[1]
                        if inst_name == 'self' : 
                            port = module.port_dict[port_name]
                        else :
                            port = module.inst_dict[inst_name].port_dict[port_name]

                        try:
                            port.wire_connect[port_pos] = wire_con
                        except Exception as e:
                            print(f'Error (07) : Port {p[0]} / Wire {wire_con} Connect Error. {len(port.wire_connect)} {port_pos} {e}')
                            input()

            # check connect status
            check_flag = 1
            for port in module.port_dict.values() : 
                for _ in port.wire_connect : 
                    if _ == None :
                        check_flag = 0
                        break
                if not check_flag :
                    break
            
            for inst in module.inst_dict.values() : 
                for port in inst.port_dict.values() : 
                    for _ in port.wire_connect : 
                        if _ == None :
                            check_flag = 0
                            break
                    if not check_flag :
                        break
                if not check_flag : 
                    break
            if not check_flag : 
                print('Error (08) : Some Ports are not connected.')


    def getGateNetwork(self) :
        return self.gate_net

    def genGateNetwork(self) :

        self.gate_net.clear()

        def gatesearch(m : Module):

            iport_c = {}
            oport_c = {}
            cport = []
            inst_iport_c = {}
            inst_oport_c = {}
            inst_cport = []
            # search inst
            for inst in m.inst_dict.values() : 
                module_name = inst.module
                #port_connect : {port_name : gate_list}
                if module_name in self.modules:
                    _t_iport_c, _t_oport_c, _t_cport = gatesearch(self.modules[module_name])
                    
                    _tmp = [x for x in _t_oport_c.keys()]
                    for k in _tmp:
                        _t_oport_c[inst.name+'.'+k] = _t_oport_c.pop(k)
                    _tmp = [x for x in _t_iport_c.keys()]
                    for k in _tmp:
                        _t_iport_c[inst.name+'.'+k] = _t_iport_c.pop(k)
                    
                    for k in _t_cport:
                        for i in range(len(k)):
                            k[i] = inst.name + '.' + k[i]

                    inst_iport_c = {**inst_iport_c, **_t_iport_c}
                    inst_oport_c = {**inst_oport_c, **_t_oport_c}
                    inst_cport.extend(_t_cport)

                elif module_name in self.gate_lib:
                    # Add Gate
                    gate_name = m.name + '.' + inst.name
                    new_gate = Gate(name=gate_name, 
                                    module=module_name,
                                    loc=m,
                                    connect_in=[],
                                    connect_out=[],
                                    gate_attr=GateAttr()) 
                    self.gate_net.addGate(new_gate)
                    
                    # port-gate connect update
                    gate_module = self.gate_lib[module_name]
                    _t_iport_c = {}
                    _t_oport_c = {}
                    for _port in gate_module.port_dict.values():
                        port_name = inst.name + '.' + _port.name + f'\[0\]'
                        if _port.direction :
                            _t_oport_c[port_name] = [gate_name]
                        else :
                            _t_iport_c[port_name] = [gate_name]

                    inst_iport_c = {**inst_iport_c, **_t_iport_c}
                    inst_oport_c = {**inst_oport_c, **_t_oport_c}
                else :
                    print(f'Error (01) : module {module_name} is not in work lib.')
            
            for selfport in m.port_dict.values() :
                if selfport.direction == 0 :
                    #input port
                    for i in range(selfport.lsb, selfport.msb+1):
                        port_name = 'self.'+selfport.name+f'\[{i}\]'
                        inst_oport_c[port_name] = []
                        iport_c[port_name] = []
                else:
                    #output port
                    for i in range(selfport.lsb, selfport.msb+1):
                        port_name = 'self.'+selfport.name+f'\[{i}\]'
                        inst_iport_c[port_name] = []
                        oport_c[port_name] = []


            # port connect
            oport_connect_tree = {}
            iport_connect_tree = {}

            #init
            for i in inst_iport_c : 
                iport_connect_tree[i] = ''
            for i in inst_oport_c : 
                oport_connect_tree[i] = []

            for w in m.wire_dict.values():
                for _ in w.connect:
                    iport_list = []
                    oport_list = []
                    if len(_) == 0:
                        continue
                    for _p in _ : 
                        pname = _p[0]+f'\[{_p[1]}\]'
                        if pname in inst_iport_c:
                            iport_list.append(pname)
                        elif pname in inst_oport_c:
                            oport_list.append(pname)
                        else :
                            print(f'Error (02) : port {m.name}.{pname} is not in port dict.')
                    
                    if len(oport_list) > 1:
                        print(f'Error (03) : wire {m.name}.{w.name} Multi Driven.')
                    if len(oport_list) == 0:
                        print(f'Error (04) : wire {m.name}.{w.name} No Driven.')

                    for op in oport_list: 
                        if op in oport_connect_tree:  
                            oport_connect_tree[op].extend( iport_list )
                        else:
                            oport_connect_tree[op] = iport_list
                    
                        for ip in iport_list : 
                            iport_connect_tree[ip] = op
                    
            
            # Add Connect to Port Tree
            
            for i in inst_cport :
                # cport : [iport, oport]
                for j in oport_connect_tree.values():
                    if i[0] in j:
                        j.append(i[1])
                iport_connect_tree[i[1]] = i[0]

            # Add Gate Connect

            def find_root_port(g, port_tree):
                if g in port_tree :
                    return find_root_port(port_tree[g], port_tree) 
                else :
                    return g

            def find_gate(g, port_tree, port_gate):
                gate_list = []
                if g in port_tree:
                    port_list = port_tree[g]
                    for p in port_list :
                        gate_list.extend( find_gate(p, port_tree, port_gate) )
                if g in port_gate:
                    gate_list.extend( port_gate[g] )
                return gate_list

            for i in oport_connect_tree : 
                if len(inst_oport_c[i]) != 0 : 
                    if len(inst_oport_c[i]) != 1:
                        print('Error : Too Many Gates for a out port.')
                    else:
                        o_gate = inst_oport_c[i][0]
                        for i_gate in find_gate(i, oport_connect_tree, inst_iport_c) :
                            self.gate_net.addConnectAB(o_gate, i_gate) 

            # Update I/O Port Gate

            for i in iport_c:
                iport_c[i] = find_gate(i, oport_connect_tree, inst_iport_c)
            
            for i in oport_c:
                rp = find_root_port(i, iport_connect_tree)
                oport_c[i] = inst_oport_c[rp]
                if rp in iport_c: 
                    cport.append([rp[5:], i[5:]])
            _tmp = [x for x in iport_c.keys()]
            for _t in _tmp:
                iport_c[_t[5:]] = iport_c.pop(_t)
            _tmp = [x for x in oport_c.keys()]
            for _t in _tmp:
                oport_c[_t[5:]] = oport_c.pop(_t)

            # print(f'module {m.name}')
            # print('iport::\n', iport_connect_tree)
            # print('oport::\n', oport_connect_tree)
            # print(iport_c)
            # print(oport_c)
            # print(cport)
            return iport_c, oport_c, cport

        gatesearch(self.modules[self.top_design])

    def netAnnotation(self, saifpath, inst_path):
        totalnet = self.gate_net.getSize()

        with open(os.path.join(saifpath, 'func.saif'), 'r') as f:
            func_saifinfo = saifparse.parse(f.read())
        with open(os.path.join(saifpath, 'glitch.saif'), 'r') as f:
            glitch_saifinfo = saifparse.parse(f.read())
        inst_path = inst_path.split('/')
        for i in inst_path : 
            func_saifinfo = func_saifinfo['cells'][i]
            glitch_saifinfo = glitch_saifinfo['cells'][i]

        def annotateModule(module : Module, funcinfo, glitchinfo):
            annotate_cnt = 0
            for inst in module.inst_dict.values() : 
                if inst.module in self.modules : 
                    annotate_cnt = annotate_cnt + \
                        annotateModule(self.modules[inst.module], 
                                   funcinfo['cells'][inst.name], 
                                   glitchinfo['cells'][inst.name])
                elif inst.module in self.gate_lib : 
                    gate_name = module.name + '.' + inst.name
                    g:Gate = self.gate_net.gate_dict[gate_name]
                    
                    # get output name
                    funcnet = funcinfo['cells'][inst.name]['net_list']
                    glitchnet = glitchinfo['cells'][inst.name]['net_list']
                    if 'Z' in funcnet : 
                        g.attr.func_tr = funcnet['Z']['tc']
                        g.attr.glitch_tr = glitchnet['Z']['tc']
                        g.attr.glitch_tr = g.attr.glitch_tr - g.attr.func_tr
                    else :
                        g.attr.func_tr = funcnet['ZN']['tc']
                        g.attr.glitch_tr = glitchnet['ZN']['tc']
                        g.attr.glitch_tr = g.attr.glitch_tr - g.attr.func_tr
                    
                    annotate_cnt = annotate_cnt + 1
            return annotate_cnt
        
        annotated_gate_num = annotateModule(self.modules[self.top_design], 
                                            func_saifinfo, 
                                            glitch_saifinfo)
        
        print(f'Annotated {annotated_gate_num} Gate in Total {totalnet} Gate. ({annotated_gate_num/totalnet})')
        

        


                    


               

            

                



