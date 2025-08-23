from .design import Design
from verilog_parser.netlist import Gate
import queue
import time

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
    
    @staticmethod
    def getPowerCost(gate : Gate) :
        return 100

    @staticmethod
    def getPowerGain(gate : Gate) : 
        return gate.attr.glitch_tr

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
            gate_id_set[g.name] =  len(g.connect_in)
            cost = self.getPowerCost(g)
            gain = self.getPowerGain(g)

            total_glitch = total_glitch + g.attr.glitch_tr
            total_tr = total_tr + g.attr.func_tr

            opt_gain = gain - cost
            if opt_gain > 0 :
                replace_gate_list.append( g )
        
        for g in replace_gate_list : 
            if gate_id_set[g.name] == 0:
                continue
            def clearGate(g):
                cost = 0
                gain = 0
                for out_gate in g.connect_out : 
                    _tmp = gate_id_set[out_gate.name]
                    gate_id_set[out_gate.name] = _tmp - 1
                    if _tmp == 1 : 
                        clear_gate_list.append(out_gate)
                        gain, cost = clearGate(out_gate)
                        if out_gate.name in replace_gate_set : 
                            # gate has been replace
                            # undo the replace
                            replace_gate_set.pop(out_gate.name)
                            cost = cost - self.getPowerCost(out_gate)
                        else : 
                            # new gain
                            gain = gain + self.getPowerGain(out_gate)
                return gain, cost

            gain, cost = clearGate(g)
            cost = cost + self.getPowerCost(g)
            gain = gain + self.getPowerGain(g)
            replace_gate_set[g.name] = g
            stats_cost = stats_cost + cost
            stats_gain = stats_gain + gain
                

        replece_gain = 0
        stats_fgate_num = len(replace_gate_set)
        for g in replace_gate_set.values() : 
            replece_gain = replece_gain + self.getPowerGain(g)

        
        # test
        influ_node_set = {}
        def set_influence_node(g):
            influ_node_set[g.name] = 1
            for gate_out in g.connect_out : 
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

        
        

