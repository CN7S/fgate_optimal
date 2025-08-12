from verilog_parser.netlist import Gate

class NetWork():
    
    def __init__(self):
        self.gate_dict = {}
    
    def clear(self):
        self.gate_dict = {}

    def print(self):
        for g in self.gate_dict.values():
            g.print()

    def getSize(self):
        return len(self.gate_dict)

    def addGate(self, g : Gate):
        self.gate_dict[g.name] = g
    
    def addConnectAB(self, gateA : str, gateB : str):
        gA = self.gate_dict[gateA]
        gB = self.gate_dict[gateB]
        gA.addout(gB)
        gB.addin(gA)

