#!/usr/bin/env python3

from .netlist import Wire, Module, Port, Instance
from .units import portNameFormat, portNameParse, instFirstUpdate,wireConnect,wireAssign,uniquePortWire
import ply.yacc as yacc
import json
from .vlex import tokens

module_list = []

def custom_json_dump(obj):
    if(isinstance(obj, Port)):
        return {'name': obj.name, 'dir': obj.direction, 'lsb':obj.lsb, 'msb':obj.msb}
    elif (isinstance(obj, Wire)):
        return {'name': obj.name, 'lsb':obj.lsb, 'msb':obj.msb, 'connect':obj.connect}
    elif isinstance(obj, Instance):
        return {'name': obj.name, 'module':obj.module, 'port':obj.port_dict}

def p_netlist_file(p):
    '''netlist_file : module
                    | netlist_file module'''
    if len(p) == 2:
        module_list.append(p[1])
    else:
        module_list.append(p[2])


def p_module(p):
    '''module : MODULE STRING LPAR portlist RPAR SEMICOLON module_body ENDMODULE
              | MODULE STRING LPAR namelist RPAR SEMICOLON module_body ENDMODULE'''
    port_dict = {}
    wire_dict = {}
    inst_dict = {}

    assign_list = [] # assign op [wireA_name, lsb, msb, wireB_name, lsb, msb]
    connect_list = [] # connect op [port_name, lsb, msb, wire_name, lsb, msb]

    portheader = p[4]
    if isinstance(portheader[0], Port) :
        for t in portheader:
            port_dict[t.name] = t
            wire_dict[t.name] = Wire(t.name, t.lsb, t.msb)
            t_connect = ['self.'+t.name, t.lsb, t.msb, t.name, t.lsb, t.msb]
            connect_list.append(t_connect)
    
    for op in p[7] :
        op_type = op[0]
        op_val = op[1]
        if op_type == 'port' :
            for i in op_val:
                port_dict[i.name] = i
                wire_dict[i.name] = Wire(i.name, i.lsb, i.msb)

                t_connect = ['self.'+i.name, i.lsb, i.msb, i.name, i.lsb, i.msb]
                connect_list.append(t_connect)

        elif op_type == 'wire' :
            for i in op_val:
                wire_dict[i.name] = i
        elif op_type == 'inst' :
            t_inst = op_val[0]
            inst_dict[t_inst.name] = t_inst

            for i in op_val[1]:
                t_connect = i
                t_connect[0] = t_inst.name + '.' + t_connect[0]
                connect_list.append(t_connect)

        elif op_type == 'assign':
            assign_list.append(op_val)

    instFirstUpdate(inst_dict, wire_dict, connect_list)
    wireConnect(wire_dict, connect_list)
    wireAssign(wire_dict, assign_list)
    uniquePortWire(port_dict, wire_dict)
    p[0] = Module(p[2], port_dict=port_dict, inst_dict=inst_dict, wire_dict=wire_dict)

    
    log = {
        'wire': wire_dict,
        'port': port_dict,
        'inst': inst_dict,
        'assign' : assign_list,
        'connect_list':connect_list
    }
    with open('testdata.json', 'w') as f:
        json.dump(log, f, default=custom_json_dump, indent=4)
        

def p_namelist(p):
    '''namelist : STRING COMMA STRING 
                 | namelist COMMA STRING'''
    if isinstance(p[1], list):
        p[0] = p[1]
        p[0].append(p[3])
    else:
        p[0] = [p[1], p[3]]
    
def p_portlist(p):
    '''portlist : module_port 
                 | portlist COMMA module_port'''
    if isinstance(p[1], Port):
        p[0] = [p[1]]
    else:
        p[0] = p[1]
        p[0].append(p[3])


def p_module_port(p): # Check Done
    '''module_port : INPUT STRING
            | OUTPUT STRING
            | INPUT LBRA NUMBER COLON NUMBER RBRA STRING
            | OUTPUT LBRA NUMBER COLON NUMBER RBRA STRING'''
    lsb = 0
    msb = 0
    direction = 0
    name = p[2]
    if p[1] == 'output' :
        direction = 1
    
    if len(p) != 3:
        name = p[7]
        if p[3] > p[5]:
            lsb = p[5]
            msb = p[3]
        else :
            lsb = p[3]
            msb = p[5]
    p[0] = Port(name, direction, 1, lsb, msb)


def p_module_body(p) :
    '''module_body : op
                    | module_body op'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1]
        p[0].append(p[2])


def p_op(p) :
    '''op : inport
          | outport
          | wire
          | assign
          | inst'''
    p[0] = p[1]
    

def p_inport(p):
    '''inport : INPUT STRING SEMICOLON
            | INPUT namelist SEMICOLON
            | INPUT LBRA NUMBER COLON NUMBER RBRA STRING SEMICOLON
            | INPUT LBRA NUMBER COLON NUMBER RBRA namelist SEMICOLON'''
    lsb = 0
    msb = 0
    if isinstance(p[3], int) :
        if p[3] > p[5]:
            lsb = p[5]
            msb = p[3]
        else :
            lsb = p[3]
            msb = p[5]

    p[0] = ['port',[]]
    if len(p) == 4:
        if isinstance(p[2], list) : 
            for i in p[2]:
                p[0][1].append(Port(i, 0, 1, lsb, msb))
        else :
            p[0][1].append(Port(p[2], 0, 1, lsb, msb))
    else:
        if isinstance(p[7], list) : 
            for i in p[7]:
                p[0][1].append(Port(i, 0, 1, lsb, msb))
        else :
            p[0][1].append(Port(p[7], 0, 1, lsb, msb))

    
def p_outport(p):
    '''outport : OUTPUT STRING SEMICOLON
            | OUTPUT namelist SEMICOLON
            | OUTPUT LBRA NUMBER COLON NUMBER RBRA STRING SEMICOLON
            | OUTPUT LBRA NUMBER COLON NUMBER RBRA namelist SEMICOLON'''
    lsb = 0
    msb = 0
    if isinstance(p[3], int) :
        if p[3] > p[5]:
            lsb = p[5]
            msb = p[3]
        else :
            lsb = p[3]
            msb = p[5]


    p[0] = ['port',[]]
    if len(p) == 4:
        if isinstance(p[2], list) : 
            for i in p[2]:
                p[0][1].append(Port(i, 1, 1, lsb, msb))
        else :
            p[0][1].append(Port(p[2], 1, 1, lsb, msb))
    else:
        if isinstance(p[7], list) : 
            for i in p[7]:
                p[0][1].append(Port(i, 1, 1, lsb, msb))
        else :
            p[0][1].append(Port(p[7], 1, 1, lsb, msb))

def p_wire(p):
    '''wire : WIRE STRING SEMICOLON
            | WIRE namelist SEMICOLON
            | WIRE LBRA NUMBER COLON NUMBER RBRA STRING SEMICOLON
            | WIRE LBRA NUMBER COLON NUMBER RBRA namelist SEMICOLON'''
    lsb = 0
    msb = 0
    if isinstance(p[3], int) :
        if p[3] > p[5]:
            lsb = p[5]
            msb = p[3]
        else :
            lsb = p[3]
            msb = p[5]


    p[0] = ['wire',[]]
    if len(p) == 4:
        if isinstance(p[2], list) : 
            for i in p[2]:
                p[0][1].append(Wire(i, lsb, msb))
        else :
            p[0][1].append(Wire(p[2], lsb, msb))
    else:
        if isinstance(p[7], list) : 
            for i in p[7]:
                p[0][1].append(Wire(i, lsb, msb))
        else :
            p[0][1].append(Wire(p[7], lsb, msb))
    
def p_assign(p):
    '''assign : ASSIGN STRING EQUAL STRING SEMICOLON
            | ASSIGN STRING LBRA NUMBER RBRA EQUAL STRING SEMICOLON
            | ASSIGN STRING EQUAL STRING LBRA NUMBER RBRA SEMICOLON
            | ASSIGN STRING LBRA NUMBER RBRA EQUAL STRING LBRA NUMBER RBRA SEMICOLON'''
    if len(p) == 6 :
        op = [p[2], -1, -1, p[4], -1, -1]
    elif len(p) == 9 :
        if p[3] == '=':
            op = [p[2], -1, -1, p[4], p[6], p[6]]
        else :
            op = [p[2], p[4], p[4], p[7], -1, -1]
    else :
        op = [p[2], p[4], p[4], p[7], p[9], p[9]]
    p[0] = ['assign', op]
    

def p_inst(p):
    '''inst : STRING STRING LPAR inst_port_list RPAR SEMICOLON'''
    pdict = {}
    for i in p[4]:
        pdict[i[0]] = Port(i[0], 0, 1, 0, 0)
    p[0] = ['inst', [Instance(p[2], p[1], pdict), p[4]]]

def p_inst_port_list(p):
    '''inst_port_list : inst_port
                      | inst_port_list COMMA inst_port'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1]
        p[0].append(p[3])

def p_inst_port(p):
    '''inst_port : DOT STRING LPAR STRING RPAR
                 | DOT STRING LPAR STRING LBRA NUMBER RBRA RPAR
                 | DOT STRING LPAR STRING LBRA NUMBER COLON NUMBER RBRA RPAR'''
    if len(p) == 6:
        p[0] = [p[2], -1, -1, p[4], -1, -1]
    elif len(p) == 9:
        p[0] = [p[2], -1, -1, p[4], p[6], p[6]]
    else:
        if p[6] > p[8]:
            lsb = p[8]
            msb = p[6]
        else :
            lsb = p[6]
            msb = p[8]
        p[0] = [p[2], -1, -1, p[4], lsb, msb]

    


def p_error(p):
    raise Exception("Syntax error at '%s' line: %d" % (p.value, p.lineno))


parser = yacc.yacc(debug=False, write_tables=False)
