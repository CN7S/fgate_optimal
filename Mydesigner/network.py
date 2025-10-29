from verilog_parser.netlist import Gate

class NetWork():
    
    def __init__(self):
        self.gate_dict = {} # name : Gate
        self.max_delay = 0
    
    def clear(self):
        self.gate_dict = {}

    def getGateTr(self):
        total_tr = 0
        for gate in self.gate_dict.values() : 
            total_tr = total_tr + gate.attr.glitch_tr
        return total_tr

    def netStatistic(self):
        def getGateType(net : NetWork):
            s = {}
            g_dict = net.gate_dict
            for g in g_dict.values():
                if g.module in s : 
                    s[g.module] = s[g.module] + 1
                else:
                    s[g.module] = 1
            return s
        def getGlitch(net: NetWork, step_len):
            s = {}
            g_dict = net.gate_dict
            for g in g_dict.values():
                glitch_attr = g.attr.glitch_tr
                gtype = f'level{int(glitch_attr // step_len)}'
                if gtype in s : 
                    s[gtype][0] = s[gtype][0] + 1
                    s[gtype][1] = s[gtype][1] + glitch_attr
                else:
                    s[gtype] = [1, glitch_attr]
            return s
        
            
        total_gate = len(self.gate_dict)
        gate_type_state = getGateType(self)
        glitch_state = getGlitch(self, 50)
        state_dict = {
            'total_gate' : total_gate,
            'gate_type_state': gate_type_state,
            'glitch_state': glitch_state
        }
        return state_dict

    def printStatus(self):
        print(f'Network Size : {self.getSize()} gates.')
        print(f'Max Delay : {self.max_delay} .')
        print(f'Total transition rate : {self.getGateTr()}.')


    def findAllCircular(self) -> list:
        '''
        Find all circular in the network
        Use DFS to find all back edges
        Return a list of circular paths
        '''
        def dfs(gate : Gate, visited : dict, rec_stack : dict, path : list, circulars : list):
            if gate.name not in visited:
                visited[gate.name] = True
                rec_stack[gate.name] = True
                for oport in gate.output_port_load:
                    for gate_attr in gate.output_port_load[oport]:
                        next_gate = gate_attr[0]
                        next_port = gate_attr[1]
                        path_node = gate.name + '.' + oport + '->' + next_gate.name + '.' + next_port
                        path.append(path_node)
                        if next_gate.name not in visited:
                            dfs(next_gate, visited, rec_stack, path, circulars)
                        elif next_gate.name in rec_stack:
                            # Found a back edge, record the circular path
                            cycle_start_index = None
                            for idx, p in enumerate(path):
                                if p.startswith(next_gate.name + '.'):
                                    cycle_start_index = idx
                                    break
                            if cycle_start_index is not None:
                                circular_path = path[cycle_start_index:]
                                circulars.append(circular_path)
                        path.pop()
            rec_stack.pop(gate.name, None)
        
        visited = {}
        rec_stack = {}
        circulars = []
        for g in self.gate_dict.values():
            if g.name not in visited:
                dfs(g, visited, rec_stack, [], circulars)
        return circulars

    def checkCircular(self):
        '''
        Check if there is circular in the network
        Use DFS to find if there is a back edge
        True if there is circular, False otherwise
        '''
        circulars = self.findAllCircular()
        if len(circulars) > 0:
            print('Error: Circular detected in the network!')
            print('Circular paths:')
            for cycle in circulars:
                print(' -> '.join(cycle))
            return True
        return False

    def staticTimingAnalysis(self, result_log : bool = False):
        '''
        Do static timing analysis for the network
        Only to calculate gate delay in network
        '''
        # Initialize delays
        for gate in self.gate_dict.values() :
            for oport in gate.output_port_load : 
                gate.attr.outport_delay_in_network[oport] = 0

        # Process gates in topological order
        processed = set()
        
        def process_gate(gate_name):
            if gate_name in processed:
                return self.gate_dict[gate_name].attr.outport_delay_in_network
            
            gate = self.gate_dict[gate_name]
            max_delay = self.gate_dict[gate_name].attr.outport_delay_in_network

            # Check all input ports
            for inport in gate.input_port_driver:
                gate_info =  gate.input_port_driver[inport]
                if gate_info != None : 
                    driver_gate = gate_info[0]
                    driver_port = gate_info[1]
                    input_delay = process_gate(driver_gate.name)
                    input_delay = input_delay[driver_port]
                else:
                    input_delay = 0
                for oport in gate.output_port_load : 
                    output_delay = input_delay + gate.getDelayFromInputToOutput(inport, oport)
                    max_delay[oport] = max(max_delay[oport], output_delay)

            processed.add(gate_name)
            return max_delay
        
        # Process all gates
        for gate_name in self.gate_dict:
            delay = process_gate(gate_name)
            for dt in delay.values() : 
                self.max_delay = max(self.max_delay, dt)
        
        if result_log:
            print("Static Timing Analysis Results:")


    def getSize(self):
        return len(self.gate_dict)

    def addGate(self, g : Gate):
        self.gate_dict[g.name] = g
    
    def addConnectA2B(self, gateA: str, gateB: str, a_port_name: str, b_port_name: str):
        gA = self.gate_dict[gateA]
        gB = self.gate_dict[gateB]
        gA.addOutPortLoad(a_port_name, gB, b_port_name)
        gB.addInPortDriver(b_port_name, gA, a_port_name)

