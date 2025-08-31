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
        self.i2o_intrinsic_delay = {} # input_name : { output_name : delay }
        self.i2o_load_delay = {}      # input_name : { output_name : delay_per_load }
        self.intrinsic_power = 0
        self.power_per_load = 0

        self.area = 0
        self.resistance = 0
        self.capacitance = 0
        self.glitch_tr = 0.0 # glitch transition rate
        self.func_tr = 0.0 # functional transition rate

    def readFromDict(self, attr_dict : dict):
        if 'i2o_intrinsic_delay' in attr_dict.keys() :
            self.i2o_intrinsic_delay = attr_dict['i2o_intrinsic_delay']
        if 'i2o_load_delay' in attr_dict.keys() :
            self.i2o_load_delay = attr_dict['i2o_load_delay']
        if 'intrinsic_power' in attr_dict.keys() :
            self.intrinsic_power = attr_dict['intrinsic_power']
        if 'power_per_load' in attr_dict.keys() :
            self.power_per_load = attr_dict['power_per_load']
        if 'area' in attr_dict.keys() :
            self.area = attr_dict['area']
        if 'resistance' in attr_dict.keys() :
            self.resistance = attr_dict['resistance']
        if 'capacitance' in attr_dict.keys() :
            self.capacitance = attr_dict['capacitance']
        if 'glitch_tr' in attr_dict.keys() :
            self.glitch_tr = attr_dict['glitch_tr']
        if 'func_tr' in attr_dict.keys() :
            self.func_tr = attr_dict['func_tr']
        
    def dumpToDict(self):
        return {
            'i2o_intrinsic_delay' : self.i2o_intrinsic_delay,
            'i2o_load_delay' : self.i2o_load_delay,
            'intrinsic_power' : self.intrinsic_power,
            'power_per_load' : self.power_per_load,
            'area' : self.area,
            'resistance' : self.resistance,
            'capacitance' : self.capacitance,
            'glitch_tr' : self.glitch_tr,
            'func_tr' : self.func_tr
        }

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
    
    def selfUpdated(self) : 
        # updated attr
        inport_list = []
        outport_list = []
        for port in self.port_dict.values() : 
            if port.direction :
                outport_list.append(port.name)
            else:
                inport_list.append(port.name)
        for inport in inport_list :
            if inport not in self.attr.i2o_intrinsic_delay : 
                self.attr.i2o_intrinsic_delay[inport] = {}
            if inport not in self.attr.i2o_load_delay : 
                self.attr.i2o_load_delay[inport] = {}
            i2o_intrinsic_delay = self.attr.i2o_intrinsic_delay[inport]
            i2o_load_delay = self.attr.i2o_load_delay[inport]
            for outport in outport_list : 
                if outport not in i2o_intrinsic_delay:
                    i2o_intrinsic_delay[outport] = 0
                if outport not in i2o_load_delay : 
                    i2o_load_delay[outport] = 0


class Instance:
    def __init__(self, name : str, module : str, port_dict : dict):
        self.name = name
        self.module = module
        self.port_dict = port_dict
    
    def getPortConnectDict(self) : 
        port_connect = {} # {port_name : wire_connect_list}
        for port in self.port_dict.values() : 
            connect_list = []
            for i in range(port.lsb, port.msb + 1) : 
                connect_list.append(port.wire_connect[i])
            port_connect[port.name] = connect_list
        return port_connect
        

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
            self.readFromDict(cell_attr.dumpToDict())
        self.outport_delay_in_network = {} # output_port : delay 

    def readFromDict(self, attr_dict : dict):
        super().readFromDict(attr_dict)
    
    def dumpToDict(self):
        return super().dumpToDict()

class Gate:
    def __init__(self, name : str, module : Module, loc : Module,
                 gate_attr : GateAttr):
        self.name = name
        self.module = module.name
        self.loc = loc

        # port
        self.input_port_driver = {} #port_name : [Gate, Port]
        self.output_port_load = {} #port_name : [[Gate, Port], ...]
        for port in module.port_dict.values() : 
            if port.direction : 
                self.output_port_load[port.name] = []
            else:
                self.input_port_driver[port.name] = None
        self.attr = gate_attr
    
    def addOutPortLoad(self, port_name, load_gate, load_port):
        if port_name not in self.output_port_load.keys() :
            print('Error : Gate {} dont have port {}.'.format(self.name, port_name))
        self.output_port_load[port_name].append([load_gate, load_port])
    
    def addInPortDriver(self, port_name, driver_gate, driver_port):
        if port_name not in self.input_port_driver.keys() :
            print('Error : Gate {} dont have port {}.'.format(self.name, port_name))
        if self.input_port_driver[port_name] != None : 
            print('Error : Gate {} Port {} already have driver {}.'.format(self.name, port_name, self.input_port_driver[port_name]))
            return
        self.input_port_driver[port_name] = [driver_gate, driver_port]

    def status(self):
        for inport in self.input_port_driver : 
            gate_info = self.input_port_driver[inport]
            if gate_info != None : 
                print(f'{self.name}.{inport} drived by {gate_info[0].name}.{gate_info[1]}.')
            else : 
                print(f'{self.name}.{inport} drived by IDEAL_INPUT.')
        for outport in self.output_port_load : 
            for gate_info in self.output_port_load[outport] : 
                print(f'{self.name}.{outport} drive {gate_info[0].name}.{gate_info[1]}.')

    def getDelayFromInputToOutput(self, input_name, output_name):
        delay = 0
        load_count = 0
        if output_name in self.output_port_load.keys() :
            load_count = len(self.output_port_load[output_name])
        if input_name in self.attr.i2o_intrinsic_delay.keys() :
            if output_name in self.attr.i2o_intrinsic_delay[input_name].keys() :
                delay += self.attr.i2o_intrinsic_delay[input_name][output_name]
        if input_name in self.attr.i2o_load_delay.keys() :
            if output_name in self.attr.i2o_load_delay[input_name].keys() :
                delay += self.attr.i2o_load_delay[input_name][output_name] * load_count
        return delay

    def getFuncPower(self):
        load_count = 0
        for port_name in self.output_port_load.keys() :
            load_count += len(self.output_port_load[port_name])
        power = self.attr.intrinsic_power + self.attr.power_per_load * load_count
        return power * self.attr.func_tr / 0.5
    
    def getGlitchPower(self):
        load_count = 0
        for port_name in self.output_port_load.keys() :
            load_count += len(self.output_port_load[port_name])
        power = self.attr.intrinsic_power + self.attr.power_per_load * load_count
        return power * self.attr.glitch_tr / 0.5
    