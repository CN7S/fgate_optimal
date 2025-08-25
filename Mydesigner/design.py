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
        if not port_name in module.port_dict :
            print(f'Error : Port {port_name} not in Module {module_name}.')
            return
        port = module.port_dict[port_name]
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
        if not port_name in module.port_dict :
            print(f'Error : Port {port_name} not in Module {module_name}.')
            return
        port = module.port_dict[port_name]

        if port_pos == None :
            if len(wire_connect_list) != (port.msb - port.lsb + 1) :
                print(f'Error : Port {port_name} connect length error.')
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
                    print(f'Error : Port {port_name}[{port_pos}] already connected.')
                    continue
                port.wire_connect[port_pos] = [wire_name, wire_pos]
                wire.connect[wire_pos].append( ['self.'+port.name, port_pos] )
        else :
            if port_pos < port.lsb or port_pos > port.msb :
                print(f'Error : Port {port_name} pos {port_pos} out of range.')
                return
            if len(wire_connect_list) != 1 :
                print(f'Error : Port {port_name} connect length error.')
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
                print(f'Error : Port {port_name}[{port_pos}] already connected.')
                return
            port.wire_connect[port_pos] = [wire_name, wire_pos]
            wire.connect[wire_pos].append( ['self.'+port.name, port_pos] )

    # Gate NetWork Operation
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
                    gate_module = self.gate_lib[module_name]
                    gate_name = m.name + '.' + inst.name
                    new_gate = Gate(name=gate_name, 
                                    module=module_name,
                                    loc=m,
                                    connect_in=[],
                                    connect_out=[],
                                    gate_attr=GateAttr(gate_module.attr)) 
                    self.gate_net.addGate(new_gate)
                    
                    # port-gate connect update
                    _t_iport_c = {}
                    _t_oport_c = {}
                    for _port in gate_module.port_dict.values():
                        port_name = inst.name + '.' + _port.name + f'[0]'
                        if _port.direction :
                            _t_oport_c[port_name] = [gate_name]
                        else :
                            _t_iport_c[port_name] = [gate_name]

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
        print(f'Gate Network Generated, Total {self.gate_net.getSize()} Gates.')


    def netAnnotation(self, saifpath, inst_path):
        '''
        Annotate the gate network with the saif file information.
            saifpath : the path of the saif file folder, should contain func.saif and glitch.saif
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
        


                    


               

            

                



