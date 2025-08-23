def portNameParse(name : str):
    t = name.split('.')
    port_name = t[-1]
    inst_name = name.split('.'+port_name)[0]
    return inst_name, port_name

def portNameFormat(inst_name : str, port_name : str):
    return inst_name + '.' + port_name

def instFirstUpdate(inst_dict : dict, wire_dict : dict, connect_list : list):
    # connect_list
    # [port_name, lsb, msb, wire_name, lsb, msb]
    for i in connect_list:
        inst_name, port_name = portNameParse(i[0])
        try:
            if inst_name != 'self' : 
                lsb = wire_dict[i[3]].lsb
                msb = wire_dict[i[3]].msb
                if i[4] != -1 :
                    lsb = 0
                    msb = i[5]-i[4]
                inst_dict[inst_name].port_dict[port_name].lsb = lsb
                inst_dict[inst_name].port_dict[port_name].msb = msb                
        except:
            print(f'Error: inst name {inst_name} is not in instance list')

def wireConnect(wire_dict : dict, connect_list : list):
    for con_op in connect_list:
        portname = con_op[0]
        if con_op[1] != -1:
            port_lsb = con_op[1]
        else:
            port_lsb = 0
        wirename = con_op[3]
        if con_op[4] != -1:
            wire_lsb = con_op[4]
            wire_msb = con_op[5]
        else:
            wire_lsb = wire_dict[wirename].lsb
            wire_msb = wire_dict[wirename].msb

        for i in range(wire_lsb, wire_msb+1):
            wire_dict[wirename].connect[i].append([portname, port_lsb + i - wire_lsb])   
    
def wireAssign(wire_dict : dict, assign_list : list):
    for op in assign_list:
        wireA_name = op[0]
        if op[1] != -1:
            wireA_lsb = op[1]
            wireA_msb = op[2]
        else:
            wireA_lsb = wire_dict[wireA_name].lsb
            wireA_msb = wire_dict[wireA_name].msb

        wireB_name = op[3]
        if op[4] != -1:
            wireB_lsb = op[4]
            wireB_msb = op[5]
        else:
            wireB_lsb = wire_dict[wireB_name].lsb
            wireB_msb = wire_dict[wireB_name].msb

        for i in range(0, wireA_msb-wireA_lsb+1):
            # print(i, wireA_name, wireB_name)
            # print(wireA_lsb, wireA_msb)
            # print(wireB_lsb, wireB_msb)
            # print(wire_dict[wireA_name].connect[wireA_lsb + i])
            # print(wire_dict[wireB_name].connect[wireB_lsb + i])
            wire_dict[wireA_name].connect[wireA_lsb + i].extend(wire_dict[wireB_name].connect[wireB_lsb + i])
            wire_dict[wireB_name].connect[wireB_lsb + i].clear()
            # input()
    
    w_key = [x for x in wire_dict.keys()]
    for w in w_key:
        _tmp = wire_dict[w]
        empty = 1
        for connect in _tmp.connect : 
            if( len( connect ) ) != 0 : 
                empty = 0
                break
        if(empty) : 
            wire_dict.pop(w)

def uniquePortWire(port_dict : dict, wire_dict : dict) :
    wire_list = [x for x in wire_dict.values()]
    wire_dict.clear()

    for wire in wire_list :
        wire_name = wire.name
        if wire_name in port_dict : 
            wire.name = '_' + wire_name
        while ( wire.name in wire_dict ) : 
            wire.name = '_' + wire.name
        
        wire_dict[wire.name] = wire