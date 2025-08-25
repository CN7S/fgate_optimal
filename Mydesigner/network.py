from verilog_parser.netlist import Gate

class NetWork():
    
    def __init__(self):
        self.gate_dict = {} # name : Gate
        self.max_delay = 0
    
    def clear(self):
        self.gate_dict = {}

    def printStatus(self):
        print(f'Network Size : {self.getSize()} gates.')
        print(f'Max Delay : {self.max_delay} .')


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
                path.append(gate.name)
                for g in gate.connect_out:
                    if g.name not in visited:
                        dfs(g, visited, rec_stack, path, circulars)
                    elif g.name in rec_stack:
                        # found a back edge
                        cycle_start_index = path.index(g.name)
                        circulars.append(path[cycle_start_index:] + [g.name])
            rec_stack.pop(gate.name, None)
            path.pop()
        
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

    def staticTimingAnalysis(self):
        '''
        Do static timing analysis for the network
        Use Dijkstra algorithm to find the longest path delay
        '''
        def dijistra(gate : Gate, visited : dict, time_dict : dict):
            if gate.name in visited:
                return
            visited[gate.name] = True
            max_delay = 0
            for g in gate.connect_in:
                if g.name not in time_dict:
                    dijistra(g, visited, time_dict)
                if time_dict[g.name] > max_delay:
                    max_delay = time_dict[g.name]
            time_dict[gate.name] = max_delay + gate.attr.delay
        
        visited = {}
        time_dict = {}
        for g in self.gate_dict.values():
            if g.name not in visited:
                dijistra(g, visited, time_dict)
        for gname in time_dict:
            self.gate_dict[gname].attr.delay_in_network = time_dict[gname]

        self.max_delay = 0
        for g in self.gate_dict.values():
            if g.attr.delay_in_network > self.max_delay:
                self.max_delay = g.attr.delay_in_network
        
        print('Static Timing Analysis Result:')
        for g in self.gate_dict.values():
            print(f'Gate {g.name} : Delay in network = {g.attr.delay_in_network}')


    def getSize(self):
        return len(self.gate_dict)

    def addGate(self, g : Gate):
        self.gate_dict[g.name] = g
    
    def addConnectAB(self, gateA : str, gateB : str):
        gA = self.gate_dict[gateA]
        gB = self.gate_dict[gateB]
        gA.addout(gB)
        gB.addin(gA)

