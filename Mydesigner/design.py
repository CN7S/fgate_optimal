from verilog_parser import parser
from verilog_parser.netlist import Instance, Wire, StdCell, Port, Gate, GateAttr, CellAttribute, Module
from saif_parser import saifparse
from .network import NetWork
from . import units
import os
import queue
import copy
import json
class Design : 
    def __init__(self):
        self.modules = {}
        self.gate_lib = {}
        
        self.gate_net = NetWork()
        self.wire_driver = {} # wire_name : [driver_gate_name]

        self.top_design = ''

    def printModulesLib(self):
        for modules in self.modules : 
            print(modules)

    def addModuleFromFile(self, module_dict, filepath):
        # print(f'Read File {filepath} ......')
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
        cell_attr = {}
        for f in files : 
            if f.split('.')[-1] == 'v' :
                self.addModuleFromFile(self.gate_lib, os.path.join(path, f))
            if f.split('.')[-1] == 'json' :
                # read StdCell Attr
                with open(os.path.join(path, f), 'r') as jf:
                    jdata = json.load(jf)
                for cell in jdata:
                    cell_attr[cell] = jdata[cell]
        
        # Module to StdCell and add Attr to gate lib
        for g in self.gate_lib.values() :
            if g.name in cell_attr :
                attrdict = cell_attr[g.name]
            else :
                attrdict = {}
                print(f'Warning : Cell {g.name} have no Attr Info.')
            attr = CellAttribute()
            attr.readFromDict(attrdict)
            stdcell = StdCell(name=g.name, 
                              port_dict=g.port_dict, 
                              inst_dict=g.inst_dict, 
                              wire_dict=g.wire_dict, 
                              cell_attr=attr)
            self.gate_lib[g.name] = stdcell
        

    def dumpModule(self, modulename, path) : 
        units.dumpModule(self.modules[modulename], path)
    
    def dumpAllModule(self, path) : 
        if not os.path.exists(path) :
            os.makedirs(path)
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

    def linkModuleInst(self):
        for module in self.modules.values() : 
            for inst in module.inst_dict.values() : 
                inst_module = inst.module
                if inst_module in self.modules :
                    inst.port_dict = {}
                    for p in self.modules[inst_module].port_dict.values() :
                        inst.port_dict[p.name] = Port(name=p.name, direction=p.direction, type=p.type, lsb=p.lsb, msb=p.msb)
                elif inst_module in self.gate_lib :
                    inst.port_dict = {}
                    for p in self.gate_lib[inst_module].port_dict.values() :
                        inst.port_dict[p.name] = Port(name=p.name, direction=p.direction, type=p.type, lsb=p.lsb, msb=p.msb)
                else : 
                    print(f'Error (06) : module {inst_module} is not in work lib.')
            
            for wire in module.wire_dict.values() :
                for i in range(wire.lsb, wire.msb+1) :
                    wire_con = [wire.name, i]
                    for p in wire.connect[i] : 
                        port_name = p[0]
                        port_pos = p[1]
                        inst_name = port_name.split('.')[0]
                        port_name = port_name.split('.')[1]
                        if inst_name == 'self' : 
                            if not port_name in module.port_dict :
                                print(f'Error (07) : port {module.name}.{port_name} is not in port dict.')
                                continue
                            port = module.port_dict[port_name]
                        else :
                            if not inst_name in module.inst_dict :
                                print(f'Error (08) : inst {module.name}.{inst_name} is not in inst dict.')
                                continue
                            inst = module.inst_dict[inst_name]
                            if not port_name in inst.port_dict :
                                print(f'Error (09) : port {module.name}.{inst_name}.{port_name} is not in port dict.')
                                continue
                            port = inst.port_dict[port_name]
                        if port_pos < port.lsb or port_pos > port.msb :
                            print(f'Error (10) : port {module.name}.{inst_name}.{port_name} pos {port_pos} out of range.')
                            continue
                        # print(f'Connect {module.name}.{inst_name}.{port_name}[{port_pos}] to {wire.name}[{i}]')
                        port.wire_connect[port_pos] = wire_con
            
            # updated new wire connect
            for wire in module.wire_dict.values() :
                for i in range(wire.lsb, wire.msb+1) :
                    wire.connect[i] = []
            for port in module.port_dict.values() : 
                for i in range(port.lsb, port.msb+1) :
                    if port.wire_connect[i] != None :
                        wire_name = port.wire_connect[i][0]
                        wire_pos = port.wire_connect[i][1]
                        if not wire_name in module.wire_dict :
                            print(f'Error (11) : Wire {wire_name} not in Module {module.name}.')
                            continue
                        wire = module.wire_dict[wire_name]
                        if wire_pos < wire.lsb or wire_pos > wire.msb :
                            print(f'Error (12) : Wire {wire_name} pos {wire_pos} out of range.')
                            continue
                        if [ 'self.'+port.name, i ] not in wire.connect[wire_pos] :
                            wire.connect[wire_pos].append( [ 'self.'+port.name, i ] )
            for inst in module.inst_dict.values():
                for port in inst.port_dict.values():
                    for i in range(port.lsb, port.msb+1) :
                        if port.wire_connect[i] != None :
                            wire_name = port.wire_connect[i][0]
                            wire_pos = port.wire_connect[i][1]
                            if not wire_name in module.wire_dict :
                                print(f'Error (11) : Wire {wire_name} not in Module {module.name}.')
                                continue
                            wire = module.wire_dict[wire_name]
                            if wire_pos < wire.lsb or wire_pos > wire.msb :
                                print(f'Error (12) : Wire {wire_name} pos {wire_pos} out of range.')
                                continue
                            if [ inst.name+'.'+port.name, i ] not in wire.connect[wire_pos] :
                                wire.connect[wire_pos].append( [ inst.name+'.'+port.name, i ] )
            
            #delete unused wire
            unused_wire = []
            for wire in module.wire_dict.values() :
                used_flag = 0
                for i in range(wire.lsb, wire.msb+1) :
                    if len(wire.connect[i]) > 0 :
                        used_flag = 1
                        break
                if not used_flag :
                    unused_wire.append(wire.name)
            for w in unused_wire :
                module.wire_dict.pop(w)
                print(f'Warning : Remove Unused Wire {module.name}.{w}.')

            # check connect status
            unconnected_port = []
            for port in module.port_dict.values() :
                for i in range(port.lsb, port.msb+1) :
                    if port.wire_connect[i] == None :
                        unconnected_port.append(f'{module.name}.self.{port.name}[{i}]')
            for inst in module.inst_dict.values() :
                for port in inst.port_dict.values() :
                    for i in range(port.lsb, port.msb+1) :
                        if port.wire_connect[i] == None :
                            unconnected_port.append(f'{module.name}.{inst.name}.{port.name}[{i}]')
            for p in unconnected_port :
                print(f'Warning : Unconnected Port {p}.')

    def getModuleTopoList(self):
        '''
        Get the module inst topological list of the design.
        return : [module_name_list]
        '''
        module_tree = self.getModuleTree()
        indegree = {}
        for m in module_tree :
            indegree[m] = len(module_tree[m][1])
        
        module_queue = queue.Queue()
        for m in indegree :
            if indegree[m] == 0 :
                module_queue.put(m)
        
        topo_list = []
        while not module_queue.empty() :
            m = module_queue.get()
            topo_list.append(m)
            for son in module_tree[m][0] :
                indegree[son] = indegree[son] - 1
                if indegree[son] == 0 :
                    module_queue.put(son)
        
        if len(topo_list) != len(self.modules) :
            print('Error : Module Topological Sort Error, Maybe Have Circle Inst.')
        
        return topo_list

    def getModuleTree(self):
        '''
        Get the module inst tree of the design.
        return : {module_name : [son_module_list, father_module_list]}
        '''
        module_tree = {}
        def buildTree(m : Module):
            if m.name in module_tree :
                return
            sons = []
            father = []
            for inst in m.inst_dict.values() : 
                if inst.module in self.modules :
                    sons.append(inst.module)
                    buildTree(self.modules[inst.module])
                    module_tree[inst.module][1].append(m.name)
                elif inst.module in self.gate_lib :
                    continue
                else :
                    print(f'Error : Module {inst.module} not in Lib.')
            module_tree[m.name] = [sons, father]
        buildTree(self.modules[self.top_design])
        return module_tree



    # Module Netlist Operation
    def addModuleWire(self, module_name, wire_name, msb, lsb):
        if not module_name in self.modules :
            print(f'Error : Module {module_name} not in Lib.')
            return
        module = self.modules[module_name]
        if wire_name in module.wire_dict :
            print(f'Error : Wire {wire_name} already in Module {module_name}.')
            return
        module.addWire(wire_name, msb, lsb)

    def removeModuleWire(self, module_name, wire_name):
        if not module_name in self.modules :
            print(f'Error : Module {module_name} not in Lib.')
            return
        module = self.modules[module_name]
        if not wire_name in module.wire_dict :
            print(f'Error : Wire {wire_name} not in Module {module_name}.')
            return
        wire = module.wire_dict[wire_name]
        for i in range(wire.lsb, wire.msb+1) :
            for port in wire.connect[i] :
                port_name = port[0]
                port_pos = port[1]
                inst_name = port_name.split('.')[0]
                port_name = port_name.split('.')[1]
                if inst_name == 'self' : 
                    port = module.port_dict[port_name]
                else :
                    port = module.inst_dict[inst_name].port_dict[port_name]

                if port.wire_connect[port_pos] != None :
                    if port.wire_connect[port_pos][0] == wire.name and port.wire_connect[port_pos][1] == i :
                        port.wire_connect[port_pos] = None
                    else :
                        print(f'Error : Port {port_name} Connect Error.')
                else :
                    print(f'Error : Port {port_name} Already Disconnected.')
        module.wire_dict.pop(wire_name)

    def removeModuleInst(self, module_name, inst_name):
        if not module_name in self.modules :
            print(f'Error : Module {module_name} not in Lib.')
            return
        module = self.modules[module_name]
        if not inst_name in module.inst_dict :
            print(f'Error : Inst {inst_name} not in Module {module_name}.')
            return
        inst = module.inst_dict[inst_name]

        # remove wire connect
        for port in inst.port_dict.values() : 
            for wire_con in port.wire_connect :
                if wire_con != None :
                    wire_name = wire_con[0]
                    wire_pos = wire_con[1]
                    if not wire_name in module.wire_dict :
                        print(f'Error : Wire {wire_name} not in Module {module_name}.')
                        continue
                    wire = module.wire_dict[wire_name]
                    if wire_pos < wire.lsb or wire_pos > wire.msb :
                        print(f'Error : Wire {wire_name} pos {wire_pos} out of range.')
                        continue
                    new_connect = []
                    for p in wire.connect[wire_pos] :
                        if p[0] != inst_name+'.'+port.name or p[1] != port.wire_connect.index(wire_con) :
                            new_connect.append(p)
                    wire.connect[wire_pos] = new_connect
        
        # remove inst
        module.inst_dict.pop(inst_name)
    
    def addModuleInst(self, module_name, inst_name, inst_module, port_connect):
        '''
        Add an instance to the module.
            module_name : the module to add the instance
            inst_name : the name of the instance
            inst_module : the module of the instance
            port_connect : {port_name : wire_connect_list}
        '''

        if not module_name in self.modules :
            print(f'Error : Module {module_name} not in Lib.')
            return
        module = self.modules[module_name]
        if inst_name in module.inst_dict :      
            print(f'Error : Inst {inst_name} already in Module {module_name}.')
            return
        if not inst_module in self.modules and not inst_module in self.gate_lib :
            print(f'Error : Inst Module {inst_module} not in Lib.')
            return
        inst_port_dict = {}
        if inst_module in self.modules :
            for p in self.modules[inst_module].port_dict.values() :
                inst_port_dict[p.name] = Port(name=p.name, direction=p.direction, type=p.type, lsb=p.lsb, msb=p.msb)
        else :
            for p in self.gate_lib[inst_module].port_dict.values() :
                inst_port_dict[p.name] = Port(name=p.name, direction=p.direction, type=p.type, lsb=p.lsb, msb=p.msb)

        new_inst = Instance(name=inst_name, module=inst_module, port_dict=inst_port_dict)
        module.inst_dict[inst_name] = new_inst
        for port_name in port_connect :
            if not port_name in new_inst.port_dict :
                print(f'Error : Port {port_name} not in Inst {inst_name}.')
                continue
            port = new_inst.port_dict[port_name]
            wire_list = port_connect[port_name]
            if len(wire_list) != (port.msb - port.lsb + 1) :
                print(f'Error : Port {port_name} connect length error.')
                continue
            for i in range(port.lsb, port.msb+1) :
                wire_con = wire_list[i - port.lsb]
                wire_name = wire_con[0]
                wire_pos = wire_con[1]
                if not wire_name in module.wire_dict :
                    print(f'Error : Wire {wire_name} not in Module {module_name}.')
                    continue
                wire = module.wire_dict[wire_name]
                if wire_pos < wire.lsb or wire_pos > wire.msb :
                    print(f'Error : Wire {wire_name} pos {wire_pos} out of range.')
                    continue
                if port.wire_connect[i] != None :
                    print(f'Error : Port {port_name}[{i}] already connected.')
                    continue
                port.wire_connect[i] = [wire_name, wire_pos]
                wire.connect[wire_pos].append( [inst_name+'.'+port.name, i] )

    # def modifyModuleInst(self, module_name, inst_name, new_inst_module, new_port_connect):
    def modifyModuleInst(self, module_name, inst_name, new_inst_module, new_port_connect):
        '''
            Modify an instance in the module.
            args:
                module_name : the module to modify the instance
                inst_name : the name of the instance
                new_inst_module : the new module of the instance
                new_port_connect : {port_name : wire_connect_list}
        '''
        if not module_name in self.modules :
            print(f'Error : Module {module_name} not in Lib.')
            return
        module = self.modules[module_name]
        if not inst_name in module.inst_dict :
            print(f'Error : Inst {inst_name} not in Module {module_name}.')
            return
        inst = module.inst_dict[inst_name]
        if not new_inst_module in self.modules and not new_inst_module in self.gate_lib :
            print(f'Error : Inst Module {new_inst_module} not in Lib.')
            return
        
        # remove old wire connect
        for port in inst.port_dict.values() : 
            for wire_con in port.wire_connect :
                if wire_con != None :
                    wire_name = wire_con[0]
                    wire_pos = wire_con[1]
                    if not wire_name in module.wire_dict :
                        print(f'Error : Wire {wire_name} not in Module {module_name}.')
                        continue
                    wire = module.wire_dict[wire_name]
                    if wire_pos < wire.lsb or wire_pos > wire.msb :
                        print(f'Error : Wire {wire_name} pos {wire_pos} out of range.')
                        continue
                    new_connect = []
                    for p in wire.connect[wire_pos] :
                        if p[0] != inst_name+'.'+port.name or p[1] != port.wire_connect.index(wire_con) :
                            new_connect.append(p)
                    wire.connect[wire_pos] = new_connect
        
        # modify inst
        inst.module = new_inst_module
        inst_port_dict = {}
        if new_inst_module in self.modules :
            for p in self.modules[new_inst_module].port_dict.values() :
                inst_port_dict[p.name] = Port(name=p.name, direction=p.direction, type=p.type, lsb=p.lsb, msb=p.msb)
        else :
            for p in self.gate_lib[new_inst_module].port_dict.values() :
                inst_port_dict[p.name] = Port(name=p.name, direction=p.direction, type=p.type, lsb=p.lsb, msb=p.msb)
        inst.port_dict = inst_port_dict

        # add new wire connect
        for port_name in new_port_connect :
            if not port_name in inst.port_dict :
                print(f'Error : Port {port_name} not in Inst {inst_name}.')
                continue
            port = inst.port_dict[port_name]
            wire_list = new_port_connect[port_name]
            if len(wire_list) != (port.msb - port.lsb + 1) :
                print(f'Error : Port {port_name} connect length error.')
                continue
            for i in range(port.lsb, port.msb+1) :
                wire_con = wire_list[i - port.lsb]
                wire_name = wire_con[0]
                wire_pos = wire_con[1]
                if not wire_name in module.wire_dict :
                    print(f'Error : Wire {wire_name} not in Module {module_name}.')
                    continue
                wire = module.wire_dict[wire_name]
                if wire_pos < wire.lsb or wire_pos > wire.msb :
                    print(f'Error : Wire {wire_name} pos {wire_pos} out of range.')
                    continue
                if port.wire_connect[i] != None :
                    print(f'Error : Port {port_name}[{i}] already connected.')
                    continue
                port.wire_connect[i] = [wire_name, wire_pos]
                wire.connect[wire_pos].append( [inst_name+'.'+port.name, i] )
    
    # def modifyModulePort(self, module_name, port_name, new_direction, new_msb, new_lsb):
    def addModulePort(self, module_name, port_name, direction, msb, lsb):
        if not module_name in self.modules :
            print(f'Error : Module {module_name} not in Lib.')
            return
        module = self.modules[module_name]
        if port_name in module.port_dict :
            print(f'Error : Port {port_name} already in Module {module_name}.')
            return
        new_port = Port(name=port_name, direction=direction, type=1, lsb=lsb, msb=msb)
        module.port_dict[port_name] = new_port

    # def removeModulePort(self, module_name, port_name):
    def removeModulePort(self, module_name, port_name):
        print(f'Remove Port {module_name}.{port_name}')
        if not module_name in self.modules :
            print(f'Error : Module {module_name} not in Lib.')
            return
        module = self.modules[module_name]
        if not port_name in module.port_dict :
            print(f'Error : Port {port_name} not in Module {module_name}.')
            return
        port = module.port_dict[port_name]
        for i in range(port.lsb, port.msb+1) :
            wire_con = port.wire_connect[i]
            if wire_con != None :
                wire_name = wire_con[0]
                wire_pos = wire_con[1]
                if not wire_name in module.wire_dict :
                    print(f'Error : Wire {wire_name} not in Module {module_name}.')
                    continue
                wire = module.wire_dict[wire_name]
                if wire_pos < wire.lsb or wire_pos > wire.msb :
                    print(f'Error : Wire {wire_name} pos {wire_pos} out of range.')
                    continue
                new_connect = []
                for p in wire.connect[wire_pos]:
                    # p[1] is the bit index of the port, wire_con is at index i
                    if not (p[0] == 'self.'+port.name and p[1] == i):
                        new_connect.append(p)
                wire.connect[wire_pos] = new_connect
        module.port_dict.pop(port_name)
    # def modifyModuleWire(self, module_name, wire_name, new_msb, new_lsb):

    def disconnectPortFromWire(self, module_name, port_name, port_pos=None):
        '''disconnect port from wire
            module_name : the module to operate
            port_name : the port to disconnect
            port_pos : the position of the port to disconnect, if None, disconnect all positions'''
        if not module_name in self.modules :
            print(f'Error : Module {module_name} not in Lib.')
            return
        module = self.modules[module_name]
        inst_name = port_name.split('.')[0]
        port_name = port_name.split('.')[1]
        if inst_name == 'self' : 
            if not port_name in module.port_dict :
                print(f'Error : Port {port_name} not in Module {module_name}.')
                return
            port = module.port_dict[port_name]
        else : 
            if not inst_name in module.inst_dict : 
                print(f'Error : Inst {inst_name} not in Module {module_name}.')
                return
            inst = module.inst_dict[inst_name]
            if not port_name in inst.port_dict :
                print(f'Error : Port {port_name} not in Inst {module_name}.{inst.name}')
                return
            port = inst.port_dict[port_name]
        if port_pos == None :
            for port_pos in range(port.lsb, port.msb+1) :
                if port.wire_connect[port_pos] != None :
                    wire_name = port.wire_connect[port_pos][0]
                    wire_pos = port.wire_connect[port_pos][1]
                    if not wire_name in module.wire_dict :
                        print(f'Error : Wire {wire_name} not in Module {module_name}.')
                        continue
                    wire = module.wire_dict[wire_name]
                    if wire_pos < wire.lsb or wire_pos > wire.msb :
                        print(f'Error : Wire {wire_name} pos {wire_pos} out of range.')
                        continue
                    new_connect = []
                    for p in wire.connect[wire_pos] :
                        if p[0] != 'self.'+port.name or p[1] != port_pos :
                            new_connect.append(p)
                    wire.connect[wire_pos] = new_connect
                    port.wire_connect[port_pos] = None
        else :
            if port_pos < port.lsb or port_pos > port.msb :
                print(f'Error : Port {port_name} pos {port_pos} out of range.')
                return
            if port.wire_connect[port_pos] == None :
                print(f'Error : Port {port_name}[{port_pos}] already disconnected.')
                return
            wire_name = port.wire_connect[port_pos][0]
            wire_pos = port.wire_connect[port_pos][1]
            if not wire_name in module.wire_dict :
                print(f'Error : Wire {wire_name} not in Module {module_name}.')
                return
            wire = module.wire_dict[wire_name]
            if wire_pos < wire.lsb or wire_pos > wire.msb :
                print(f'Error : Wire {wire_name} pos {wire_pos} out of range.')
                return
            new_connect = []
            for p in wire.connect[wire_pos] :
                if p[0] != 'self.'+port.name or p[1] != port_pos :
                    new_connect.append(p)
            wire.connect[wire_pos] = new_connect
            port.wire_connect[port_pos] = None

    def connectPortToWire(self, module_name, port_name, wire_connect_list, port_pos=None):
        '''connect port to wire
            module_name : the module to operate
            port_name : the port to connect
            wire_connect_list : [[wire_name, wire_pos], ...] 
            port_pos : the position of the port to connect, if None, connect all positions'''
        if not module_name in self.modules :
            print(f'Error : Module {module_name} not in Lib.')
            return
        module = self.modules[module_name]

        inst_name = port_name.split('.')[0]
        port_name = port_name.split('.')[1]
        if inst_name == 'self' : 
            if not port_name in module.port_dict :
                print(f'Error : Port {inst_name}.{port_name} not in Module {module_name}.')
                return
            port = module.port_dict[port_name]
        else : 
            if not inst_name in module.inst_dict : 
                print(f'Error : Inst {inst_name} not in Module {module_name}.')
                return
            inst = module.inst_dict[inst_name]
            if not port_name in inst.port_dict :
                print(f'Error : Port {inst_name}.{port_name} not in Inst {module_name}.{inst.name}')
                return
            port = inst.port_dict[port_name]


        if port_pos == None :
            if len(wire_connect_list) != (port.msb - port.lsb + 1) :
                print(f'Error : Port {inst_name}.{port_name} connect length error.')
                return
            for port_pos in range(port.lsb, port.msb+1) :
                wire_con = wire_connect_list[port_pos - port.lsb]
                wire_name = wire_con[0]
                wire_pos = wire_con[1]
                if not wire_name in module.wire_dict :
                    print(f'Error : Wire {wire_name} not in Module {module_name}.')
                    continue
                wire = module.wire_dict[wire_name]
                if wire_pos < wire.lsb or wire_pos > wire.msb :
                    print(f'Error : Wire {wire_name} pos {wire_pos} out of range.')
                    continue
                if port.wire_connect[port_pos] != None :
                    print(f'Error : Port {inst_name}.{port_name}[{port_pos}] already connected.')
                    continue
                port.wire_connect[port_pos] = [wire_name, wire_pos]
                wire.connect[wire_pos].append( [inst_name+'.'+port.name, port_pos] )
        else :
            if port_pos < port.lsb or port_pos > port.msb :
                print(f'Error : Port {inst_name}.{port_name} pos {port_pos} out of range.')
                return
            if len(wire_connect_list) != 1 :
                print(f'Error : Port {inst_name}.{port_name} connect length error.')
                return
            wire_con = wire_connect_list[0]
            wire_name = wire_con[0]
            wire_pos = wire_con[1]
            if not wire_name in module.wire_dict :
                print(f'Error : Wire {wire_name} not in Module {module_name}.')
                return
            wire = module.wire_dict[wire_name]
            if wire_pos < wire.lsb or wire_pos > wire.msb : 
                print(f'Error : Wire {wire_name} pos {wire_pos} out of range.')
                return
            if port.wire_connect[port_pos] != None :
                print(f'Error : Port {inst_name}.{port_name}[{port_pos}] already connected : {port.wire_connect[port_pos]}.')
                return
            port.wire_connect[port_pos] = [wire_name, wire_pos]
            wire.connect[wire_pos].append( [inst_name+'.'+port.name, port_pos] )
        # print(f'{module_name}.{inst_name}.{port_name}[{port_pos}] connected : {port.wire_connect[port_pos]}.')

    def connectPortToPort(self, module_name, a_port_name, a_port_pos, b_port_name, b_port_pos) :
        if not module_name in self.modules :
            print(f'Error : Module {module_name} not in Lib.')
            return
        module = self.modules[module_name]

        a_port_inst = a_port_name.split('.')[0]
        a_port_name = a_port_name.split('.')[1]
        if a_port_inst == 'self' : 
            if not a_port_name in module.port_dict :
                print(f'Error : Port {a_port_name} not in Module {module.name}.')
                return
            a_port = module.port_dict[a_port_name] 
        else :      
            if not a_port_inst in module.inst_dict :
                    print(f'Error : Inst {a_port_inst} not in Module {module_name}.')
                    return
            a_inst = module.inst_dict[a_port_inst]        
            if not a_port_name in a_inst.port_dict :
                print(f'Error : Port {a_port_name} not in Inst {module.name}.{a_inst.name}[{a_inst.module}].')
                return
            a_port = a_inst.port_dict[a_port_name]        

        b_port_inst = b_port_name.split('.')[0]
        b_port_name = b_port_name.split('.')[1]
        if b_port_inst == 'self' :       
            if not b_port_name in module.port_dict :
                print(f'Error : Port {b_port_name} not in Module {module.name}.')
                return
            b_port = module.port_dict[b_port_name] 
        else : 
            if not b_port_inst in module.inst_dict :
                print(f'Error : Inst {b_port_inst} not in Module {module_name}.')
                return
            b_inst = module.inst_dict[b_port_inst]        
            if not b_port_name in b_inst.port_dict :
                print(f'Error : Port {b_port_name} not in Inst {module.name}.{b_inst.name}[{b_inst.module}].')
                return
            b_port = b_inst.port_dict[b_port_name] 

        a_wire = a_port.wire_connect[a_port_pos]
        b_wire = b_port.wire_connect[b_port_pos]

        connect_wire = None
        if a_wire != None and b_wire != None : 
            print(f'Error : Port {a_port_name}[{a_port_pos}] and Port {b_port_name}{b_port_pos} conflict.')
            return

        if a_wire != None : 
            connect_wire = a_wire
        if b_wire != None : 
            connect_wire = b_wire
        
        if connect_wire == None : 
            # Add New Wire
            new_wire_name = ''
            for i in range(1000) : 
                _tmp = f'n{i}'
                if not _tmp in module.wire_dict : 
                    new_wire_name = _tmp
                    break
            if new_wire_name == '' : 
                print('Error : Cant find new wire name.')
                return
            self.addModuleWire(module_name=module_name,
                               wire_name=new_wire_name,
                               msb=0,
                               lsb=0)
            connect_wire = [new_wire_name, 0]
        if a_wire == None : 
            self.connectPortToWire(module_name=module_name,
                               port_name=a_port_inst+'.'+a_port_name,
                               wire_connect_list=[connect_wire],
                               port_pos=a_port_pos)
        if b_wire == None : 
            self.connectPortToWire(module_name=module_name,
                               port_name=b_port_inst+'.'+b_port_name,
                               wire_connect_list=[connect_wire],
                               port_pos=b_port_pos)
        # print(f'connect {module_name}.{a_port_inst}.{a_port_name}[{a_port_pos}] -> {module_name}.{b_port_inst}.{b_port_name}[{b_port_pos}]')
        # input('Waiting...')

    # Gate NetWork Operation
    def getGateNetwork(self) :
        return self.gate_net

    def genGateNetwork(self) :

        self.gate_net.clear()

        def gatesearch(m : Module):

            # init
            iport_c = {} # input port connect : {port_name : [[gate, port], ...]}
            oport_c = {} # output port connect : {port_name : [[gate, port], ...]}
            cport = [] # connect port : [[iport, oport], ...]
            iport_loadwire = {} # input port load wire : {port_name : [wire, ...]}
            inst_iport_c = {} # instance input port connect : {port_name : [[gate, port], ...]}
            inst_oport_c = {} # instance output port connect : {port_name : [[gate, port], ...]}
            inst_iport_loadwire = {} # instance input port load wire : {port_name : [wire, ...]}
            inst_cport = [] # instance connect port : [[iport, oport], ...]
            # search inst
            
            for inst in m.inst_dict.values() : 
                module_name = inst.module
                if module_name in self.modules:
                    _t_iport_c, _t_oport_c, _t_cport, _t_iport_loadwire = gatesearch(self.modules[module_name])
                    
                    
                    _t_oport_c = {inst.name + '.' + k: v for k, v in _t_oport_c.items()}
                    _t_iport_c = {inst.name + '.' + k: v for k, v in _t_iport_c.items()}
                    _t_cport = [ [inst.name + '.' + k[0], inst.name + '.' + k[1]] for k in _t_cport ]
                    _t_iport_loadwire = {inst.name + '.' + k: v for k, v in _t_iport_loadwire.items()}

                    inst_iport_c = {**inst_iport_c, **_t_iport_c}
                    inst_oport_c = {**inst_oport_c, **_t_oport_c}
                    inst_iport_loadwire = {**inst_iport_loadwire, **_t_iport_loadwire}
                    inst_cport.extend(_t_cport)

                elif module_name in self.gate_lib:
                    # Add Gate
                    gate_module = self.gate_lib[module_name]
                    gate_name = m.name + '.' + inst.name
                    new_gate = Gate(name=gate_name, 
                                    module=gate_module,
                                    loc=m,
                                    gate_attr=GateAttr(gate_module.attr)) 
                    self.gate_net.addGate(new_gate)
                    
                    # port-gate connect update
                    _t_iport_c = {}
                    _t_oport_c = {}
                    for _port in gate_module.port_dict.values():
                        # single bit port only
                        port_name = inst.name + '.' + _port.name + f'[0]'
                        if _port.direction :
                            _t_oport_c[port_name] = [[gate_name, _port.name]]
                        else :
                            _t_iport_c[port_name] = [[gate_name, _port.name]]

                    inst_iport_c = {**inst_iport_c, **_t_iport_c}
                    inst_oport_c = {**inst_oport_c, **_t_oport_c}
                else :
                    print(f'Error (01) : module {module_name} is not in work lib.')
            
            # init port connect dict
            for selfport in m.port_dict.values() :
                if selfport.direction == 0 :
                    #input port
                    for i in range(selfport.lsb, selfport.msb+1):
                        port_name = 'self.'+selfport.name+f'[{i}]'
                        inst_oport_c[port_name] = []
                        iport_c[port_name] = []
                else:
                    #output port
                    for i in range(selfport.lsb, selfport.msb+1):
                        port_name = 'self.'+selfport.name+f'[{i}]'
                        inst_iport_c[port_name] = []
                        oport_c[port_name] = []


            # port connect
            oport_loading_port = {}
            iport_driving_port = {}

            #init
            for i in inst_iport_c : 
                iport_driving_port[i] = None
            for i in inst_oport_c : 
                oport_loading_port[i] = []

            for w in m.wire_dict.values():
                for i in range(w.lsb, w.msb+1) :
                    self.wire_driver[f'{m.name}.{w.name}[{i}]'] = None   # add Wire to Wire driver dict
                for _ in w.connect:
                    iport_list = []
                    oport_list = []
                    if len(_) == 0:
                        continue
                    for _p in _ : 
                        pname = _p[0]+f'[{_p[1]}]'
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
                        if op in oport_loading_port:  
                            oport_loading_port[op].extend( iport_list )
                        else:
                            oport_loading_port[op] = iport_list
                    
                        for ip in iport_list : 
                            iport_driving_port[ip] = op
                    
            
            # Add Connect to Port Tree
            
            for i in inst_cport :
                # cport : [iport, oport]
                iport_driving_port[i[1]] = i[0]

            # maintain port driving/loading
            def update_driving_port(port_name):
                driving_port = iport_driving_port[port_name]
                if driving_port not in iport_driving_port :
                    return driving_port
                iport_driving_port[port_name] = update_driving_port(driving_port)
                return iport_driving_port[port_name]
            for i in iport_driving_port :
                driving_port =  update_driving_port(i)
                if i in oport_loading_port :
                    oport_loading_port[driving_port].extend( oport_loading_port[i] )
            
            # Add Gate Connect
            for driving_port in oport_loading_port :
                inst_name = driving_port.split('.')[0]
                if inst_name == 'self' :
                    # Add connect from output port to input port
                    continue
                else : 
                    if len(inst_oport_c[driving_port]) > 1 :
                        print('Error : Too Many Driving Gates for a out port.')
                        print(f'Driving Gates: {inst_oport_c[driving_port]}')
                    elif len(inst_oport_c[driving_port]) == 0 :
                        continue
                    else:
                        driver_gate_name = inst_oport_c[driving_port][0][0]
                        driver_port_name = inst_oport_c[driving_port][0][1]
                        for loading_port in oport_loading_port[driving_port] :
                            if len(inst_iport_c[loading_port]) == 0 :
                                continue
                            for gate_attr in inst_iport_c[loading_port] :
                                load_gate_name = gate_attr[0]
                                load_port_name = gate_attr[1]
                                self.gate_net.addConnectA2B(gateA=driver_gate_name, 
                                                      gateB=load_gate_name, 
                                                      a_port_name=driver_port_name, 
                                                      b_port_name=load_port_name)

            # Updated wire driver
            for w in m.wire_dict.values():
                for i in range(w.lsb, w.msb+1) :
                    wire_name = f'{m.name}.{w.name}[{i}]'
                    if w.connect[i] == [] :
                        # print(f'Warning : Wire {wire_name} No Connect.')
                        self.wire_driver[wire_name] = None
                    else :
                        port_name = w.connect[i][0][0] + f'[{w.connect[i][0][1]}]'
                        if port_name in iport_driving_port :
                            driving_port = iport_driving_port[port_name]
                        else : 
                            driving_port = port_name
                        if driving_port in inst_oport_c :
                            if len(inst_oport_c[driving_port]) > 1 :
                                print('Error : Too Many Driving Gates for a out port.')
                                print(f'Driving Gates: {inst_oport_c[driving_port]}')
                            elif len(inst_oport_c[driving_port]) == 0 :
                                # print(f'Warning : Wire {wire_name} Driven by Port {driving_port} No Connect Gate.')
                                self.wire_driver[wire_name] = None
                            else :
                                self.wire_driver[wire_name] = inst_oport_c[driving_port][0] # [gate_name, port_name]
                        else :
                            self.wire_driver[wire_name] = None
            
            # update Inst wire driver
            for inst in m.inst_dict.values() :
                for port in inst.port_dict.values() :
                    if port.direction == 1 :
                        # output port
                        continue
                    for i in range(port.lsb, port.msb+1) :
                        port_name = inst.name + '.' + port.name + f'[{i}]'
                        driver_gate = None
                        if port.wire_connect[i] != None :
                            wire_name = port.wire_connect[i][0]
                            wire_pos = port.wire_connect[i][1]
                            wire_name = f'{m.name}.{wire_name}[{wire_pos}]'
                            driver_gate = self.wire_driver[wire_name]
                        if port_name in inst_iport_loadwire :
                            for wire in inst_iport_loadwire[port_name] :
                                self.wire_driver[wire] = driver_gate



            # Update I/O Port Gate
            for iport in iport_c:
                driving_port_list = oport_loading_port[iport]
                for dp in driving_port_list :
                    iport_c[iport].extend( inst_iport_c[dp] )
            
            for oport in oport_c:
                driving_port = iport_driving_port[oport]
                oport_c[oport] = inst_oport_c[driving_port]
                
                inst_name = driving_port.split('.')[0]
                if inst_name == 'self' :
                    cport.append( [driving_port, oport] )

            
            # update input port load wire
            for iport in iport_c :
                wire_list = []
                # add straight inst load wire
                for lport in oport_loading_port[iport] :
                    if lport in inst_iport_loadwire :
                        wire_list.extend( inst_iport_loadwire[lport] )
                # add self load wire
                port_name = iport.split('.')[1].split('[')[0]
                port_pos = int(iport.split('[')[1].split(']')[0])
                if port_name in m.port_dict :
                    port = m.port_dict[port_name]
                    if port.wire_connect[port_pos] != None :
                        wire_list.append(f"{m.name}.{port.wire_connect[port_pos][0]}[{port.wire_connect[port_pos][1]}]")
                iport_loadwire[iport] = wire_list
            

            # remove self. from port name
            iport_c = {k[5:]: v for k, v in iport_c.items()} 
            oport_c = {k[5:]: v for k, v in oport_c.items()}
            iport_loadwire = {k[5:]: v for k, v in iport_loadwire.items()}
            cport = [ [k[5:], v[5:]] for k, v in cport ]

            



            return iport_c, oport_c, cport, iport_loadwire

        iport_c, oport_c, cport, iport_loadwire = gatesearch(self.modules[self.top_design])

        for iport in iport_loadwire :
            for wire in iport_loadwire[iport] :
                self.wire_driver[wire] = ['IDEAL_INPUT', None] # set ideal input gate as driver

        print(f'Gate Network Generated, Total {self.gate_net.getSize()} Gates.')
        print(f'Total wire Info: {len(self.wire_driver)} Wires.')
    
    def checkGateNetwork(self):
        if self.gate_net.checkCircular() :
            print('Error : Gate Network has Circular Connection.')

        error_cnt = 0
        for w in self.wire_driver :
            if self.wire_driver[w] == None :
                module_name = w.split('.')[0]
                wire_name = w.split('.')[1].split('[')[0]
                wire_pos = int(w.split('[')[1].split(']')[0])
                if not module_name in self.modules :
                    print(f'Error : Wire {w} in Module {module_name} not in Lib.')
                    error_cnt = error_cnt + 1
                    continue
                module = self.modules[module_name]
                if not wire_name in module.wire_dict :
                    print(f'Error : Wire {w} in Module {module_name} not in Lib.')
                    error_cnt = error_cnt + 1
                    continue
                wire = module.wire_dict[wire_name]
                if wire_pos < wire.lsb or wire_pos > wire.msb :
                    print(f'Error : Wire {w} pos {wire_pos} out of range.')
                    error_cnt = error_cnt + 1
                    continue
                if wire.connect[wire_pos] == [] :
                    print(f'Warning : Wire {w} No Connect.')
                    continue
        if error_cnt == 0 :
            print('Gate Network Check Passed.')
        else :
            print(f'Gate Network Check Found {error_cnt} Errors.')
    
    def printWireDriver(self):
        for w in self.wire_driver :
            print(f'Wire {w} Driver Gate: {self.wire_driver[w]}')
    
    def printModulePortDriver(self, module_name):
        if not module_name in self.modules :
            print(f'Error : Module {module_name} not in Lib.')
            return
        module = self.modules[module_name]
        for port in module.port_dict.values() :
            for i in range(port.lsb, port.msb+1) :
                port_name = module.name+'.'+port.name+f'[{i}]'
                driver_gate = None
                if port.wire_connect[i] != None :
                    wire_name = port.wire_connect[i][0]
                    wire_pos = port.wire_connect[i][1]
                    wire_name = f'{module.name}.{wire_name}[{wire_pos}]'
                    driver_gate = self.wire_driver[wire_name]
                print(f'Port {port_name} Driver Gate: {driver_gate}')

    def runSTA(self, result_log : bool = False):
        self.gate_net.staticTimingAnalysis(result_log)
    
    def getMoudleOutputDelay(self, module_name, port_name=None, port_pos=None):
        if not module_name in self.modules :
            print(f'Error : Module {module_name} not in Lib.')
            return
        module = self.modules[module_name]
        if port_name == None :
            delay_dict = {}
            for port in module.port_dict.values() :
                if port.direction == 1 :
                    for i in range(port.lsb, port.msb+1) :
                        gate_port_name = module.name+'.'+port.name+f'[{i}]'
                        wire_con = port.wire_connect[i]
                        wire_name = f'{module.name}.{wire_con[0]}[{wire_con[1]}]'
                        if wire_name in self.wire_driver :
                            drive_gate = self.wire_driver[wire_name][0]
                            drive_port = self.wire_driver[wire_name][1]
                            drive_gate = self.gate_net.gate_dict.get(drive_gate, None)
                            delay_dict[gate_port_name] = \
                                drive_gate.attr.outport_delay_in_network[drive_port] if drive_gate != None else None
                        else :
                            delay_dict[gate_port_name] = None
            return delay_dict
        else :
            if not port_name in module.port_dict :
                print(f'Error : Port {port_name} not in Module {module_name}.')
                return
            port = module.port_dict[port_name]
            if port.direction != 1 :
                print(f'Error : Port {port_name} is not output port.')
                return
            if port_pos == None :
                delay_dict = {}
                for i in range(port.lsb, port.msb+1) :
                    gate_port_name = module.name+'.'+port.name+f'[{i}]'
                    wire_con = port.wire_connect[i]
                    wire_name = f'{module.name}.{wire_con[0]}[{wire_con[1]}]'
                    if wire_name in self.wire_driver :
                        drive_gate = self.wire_driver[wire_name][0]
                        drive_port = self.wire_driver[wire_name][1]
                        drive_gate = self.gate_net.gate_dict.get(drive_gate, None)
                        delay_dict[gate_port_name] = \
                            drive_gate.attr.outport_delay_in_network[drive_port] if drive_gate != None else None
                    else :
                        delay_dict[gate_port_name] = None
                return delay_dict
            else :
                if port_pos < port.lsb or port_pos > port.msb :
                    print(f'Error : Port {port_name} pos {port_pos} out of range.')
                    return
                gate_port_name = module.name+'.'+port.name+f'[{port_pos}]'
                wire_con = port.wire_connect[port_pos]
                wire_name = f'{module.name}.{wire_con[0]}[{wire_con[1]}]'
                if wire_name in self.wire_driver :
                    drive_gate = self.wire_driver[wire_name][0]
                    drive_port = self.wire_driver[wire_name][1]
                    drive_gate = self.gate_net.gate_dict.get(drive_gate, None)
                    return drive_gate.attr.outport_delay_in_network[drive_port] \
                        if drive_gate != None else None
                else :
                    return None

    def netAnnotation(self, saifpath, inst_path, cycles):
        '''
        Annotate the gate network with the saif file information.
            saifpath : the path of the saif file folder, should contain func.saif and glitch.saif
                func.saif : the saif file of the functional simulation
                glitch.saif : the saif file of the glitch simulation
            inst_path : the path of the top module instance in the saif file
                e.g. gfmul_tb/mul_x/mul_x
        '''
        if not os.path.exists(saifpath):
            print('Error (05) : SAIF Path Not Exist.')
            return
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
                        g.attr.func_tr = funcnet['Z']['tc'] / cycles
                        g.attr.glitch_tr = glitchnet['Z']['tc'] / cycles
                        g.attr.glitch_tr = g.attr.glitch_tr - g.attr.func_tr
                    else :
                        g.attr.func_tr = funcnet['ZN']['tc'] / cycles
                        g.attr.glitch_tr = glitchnet['ZN']['tc'] / cycles
                        g.attr.glitch_tr = g.attr.glitch_tr - g.attr.func_tr
                    
                    annotate_cnt = annotate_cnt + 1
            return annotate_cnt
        
        annotated_gate_num = annotateModule(self.modules[self.top_design], 
                                            func_saifinfo, 
                                            glitch_saifinfo)
        
        print(f'Annotated {annotated_gate_num} Gate in Total {totalnet} Gate. ({annotated_gate_num/totalnet})')
        


                    


               

            

                



