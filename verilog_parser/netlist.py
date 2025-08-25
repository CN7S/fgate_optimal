import json
def custom_json_dump(obj):
    if(isinstance(obj, Port)):
        return {'name': obj.name, 'dir': obj.direction, 'lsb':obj.lsb, 'msb':obj.msb, 'connect':obj.wire_connect}
    elif (isinstance(obj, Wire)):
        return {'name': obj.name, 'lsb':obj.lsb, 'msb':obj.msb, 'connect':obj.connect}
    elif isinstance(obj, Instance):
        return {'name': obj.name, 'module':obj.module, 'port':obj.port_dict}
    elif isinstance(obj, Module):
        return {'name': obj.name, 'port':obj.port_dict, 'wire':obj.wire_dict, 'inst':obj.inst_dict}

class CellAttribute:
    def __init__(self):
        self.delay = 0
        self.area = 0
        self.resistance = 0
        self.capacitance = 0
        self.glitch_tr = 0
        self.func_tr = 0
    
    def readFromDict(self, attr_dict : dict):
        if 'delay' in attr_dict :
            self.delay = attr_dict['delay']
        if 'area' in attr_dict :
            self.area = attr_dict['area']
        if 'resistance' in attr_dict :
            self.resistance = attr_dict['resistance']
        if 'capacitance' in attr_dict :
            self.capacitance = attr_dict['capacitance']
        if 'glitch_tr' in attr_dict :
            self.glitch_tr = attr_dict['glitch_tr']
        if 'func_tr' in attr_dict :
            self.func_tr = attr_dict['func_tr']

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
    
    def addWire(self, name : str, msb : int = 0, lsb : int = 0):
        if name in self.wire_dict.keys() :
            print('Warning (01) : Wire {} already exists in module {}.'.format(name, self.name))
            return self.wire_dict[name]
        wire = Wire(name, lsb, msb)
        self.wire_dict[name] = wire
        return wire

    def dumpjson(self, path):
        with open(path, 'w') as f:
            json.dump(self, f, default=custom_json_dump, indent=4)
    
class StdCell (Module) :
    def __init__(self, name : str, 
                 port_dict : dict, 
                 inst_dict : dict, 
                 wire_dict : dict, 
                 cell_attr : CellAttribute):
        super().__init__(name, port_dict, inst_dict, wire_dict)
        self.attr = cell_attr 


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

class GateAttr (CellAttribute) :
    def __init__(self, cell_attr : CellAttribute = None):
        super().__init__()
        if cell_attr is not None :
            self.delay = cell_attr.delay
            self.area = cell_attr.area
            self.resistance = cell_attr.resistance
            self.capacitance = cell_attr.capacitance
            self.glitch_tr = cell_attr.glitch_tr
            self.func_tr = cell_attr.func_tr
        self.delay_in_network = 0

    def readFromDict(self, attr_dict : dict):
        super().readFromDict(attr_dict)

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