import json
def custom_json_dump(obj):
    if(isinstance(obj, Port)):
        return {'name': obj.name, 'dir': obj.direction, 'lsb':obj.lsb, 'msb':obj.msb}
    elif (isinstance(obj, Wire)):
        return {'name': obj.name, 'lsb':obj.lsb, 'msb':obj.msb, 'connect':obj.connect}
    elif isinstance(obj, Instance):
        return {'name': obj.name, 'module':obj.module, 'port':obj.port_dict}
    elif isinstance(obj, Module):
        return {'name': obj.name, 'port':obj.port_dict, 'wire':obj.wire_dict, 'inst':obj.inst_dict}


class Wire:
    def __init__(self, name : str, lsb : int = 0, msb : int = 0):
        self.name = name
        self.lsb = lsb
        self.msb = msb
        self.connect = [] # (pos, port_list)
        for _ in range(self.lsb, self.msb+1):
            self.connect.append([])

class Module:
    def __init__(self, name : str, port_dict : dict, inst_dict : dict, wire_dict : dict):
        self.name = name
        self.port_dict = port_dict
        self.inst_dict = inst_dict
        self.wire_dict = wire_dict
    
    def dumpjson(self, path):
        with open(path, 'w') as f:
            json.dump(self, f, default=custom_json_dump, indent=4)
    
    


class Instance:
    def __init__(self, name : str, module : str, port_dict : dict):
        self.name = name
        self.module = module
        self.port_dict = port_dict
        

class Port:
    def __init__(self, name : str, direction : int, type : int, lsb : int = 0, msb : int = 0):
        self.name = name
        self.direction = direction # { 0:"input", 1:"output" }
        self.type = type # { 0:"reg", 1:"wire" }
        self.lsb = lsb
        self.msb = msb
        self.wire_connect = []
        if self.lsb == 0 :
            for _ in range(lsb, msb + 1) :
                self.wire_connect.append(None)

class GateAttr:
    def __init__(self):
        self.C = 0
        self.R = 0
        self.glitch_tr = 0
        self.func_tr = 0

class Gate:
    def __init__(self, name : str, module : str, loc : Module, connect_in : list, connect_out : list,
                 gate_attr : GateAttr):
        self.name = name
        self.module = module
        self.loc = loc
        self.connect_in = connect_in  # [Gate, Gate]
        self.connect_out = connect_out # [Gate, Gate]

        self.attr = gate_attr
    
    def addout(self, outgate):
        self.connect_out.append(outgate)
    
    def addin(self, ingate):
        self.connect_in.append(ingate)
    
    def print(self):
        print('\[')
        print('Gate Name : ', self.name)
        print('Gate Module : ', self.module)
        print('connect_in : ', [x.name for x in self.connect_in])
        print('connect_out : ', [x.name for x in self.connect_out])
        print('\]')

## assign
## pair (Wire, pos) -- (Wire, pos)