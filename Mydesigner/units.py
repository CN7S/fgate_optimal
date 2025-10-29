from verilog_parser.netlist import Module
import os


def dumpModule(module : Module, filepath : str, filename = None) :

    
    module_name = module.name
    if filename is None : 
        filepath = os.path.join(filepath, f'{module_name}.v')
    else : 
        filepath = os.path.join(filepath, filename)

    # module.dumpjson(filepath + '.json')

    module_port_list = [x for x in module.port_dict.keys()]
    module_port_header = ''
    for port in module_port_list : 
        module_port_header = module_port_header + f', {port}'
    module_port_header = module_port_header[2:]
    module_header = f'module {module_name} ( {module_port_header} );\n'
    module_end = 'endmodule\n'
    
    module_port_define = ''
    for port in module.port_dict.values() : 
        port_width = port.msb - port.lsb + 1
        port_direction = 'output' if port.direction else 'input'
        if port_width == 1 :
            portdef = f'{port_direction} {port.name};\n'
        else :
            portdef = f'{port_direction} [{port_width-1}:0] {port.name};\n'
        module_port_define = module_port_define + portdef
    
    module_wire_define = ''
    wire_str = ''
    for wire in module.wire_dict.values() : 
        wire_width = wire.msb - wire.lsb + 1
        wiredef = ''
        if wire_width == 1 :
            wire_str = wire_str + wire.name + ', '
        else :
            wiredef = f'wire [{wire_width-1}:0] {wire.name};\n'
        module_wire_define = module_wire_define + wiredef
    if wire_str != '':
        wire_str = wire_str[0:len(wire_str)-2]
        wiredef = f'wire {wire_str};\n'
        module_wire_define = module_wire_define + wiredef


    module_assign_define = ''
    for port in module.port_dict.values() : 
        wire_list = []
        port_width_list = []
        wire_name = ''
        wire_lsb = 0
        wire_msb = 0
        for i in range(port.lsb, port.msb + 1) : 
            _connect = port.wire_connect[i]
            if wire_name == _connect[0] : 
                if wire_msb + 1 == _connect[1] : 
                    wire_msb = _connect[1]
                else :

                    if wire_name != '' : 
                        if module.wire_dict[wire_name].lsb == wire_lsb \
                            and module.wire_dict[wire_name].msb == wire_msb : 
                            wire_list.append(f'{wire_name}')
                        else :
                            if wire_lsb == wire_msb : 
                                wire_list.append(f'{wire_name}[{wire_lsb}]')
                            else : 
                                wire_list.append(f'{wire_name}[{wire_msb}:{wire_lsb}]')
                        port_width_list.append(wire_msb - wire_lsb + 1)

                    wire_name = ''
                    wire_lsb = 0
                    wire_msb = 0
            else :
                if wire_name != '' : 
                    if module.wire_dict[wire_name].lsb == wire_lsb \
                        and module.wire_dict[wire_name].msb == wire_msb : 
                        wire_list.append(f'{wire_name}')
                    else :
                        if wire_lsb == wire_msb : 
                            wire_list.append(f'{wire_name}[{wire_lsb}]')
                        else : 
                            wire_list.append(f'{wire_name}[{wire_msb}:{wire_lsb}]')
                    port_width_list.append(wire_msb - wire_lsb + 1)
                wire_name = _connect[0]
                wire_lsb = _connect[1]
                wire_msb = _connect[1]
        if wire_name != '' : 
            if module.wire_dict[wire_name].lsb == wire_lsb \
                and module.wire_dict[wire_name].msb == wire_msb : 
                wire_list.append(f'{wire_name}')
            else :
                if wire_lsb == wire_msb : 
                    wire_list.append(f'{wire_name}[{wire_lsb}]')
                else : 
                    wire_list.append(f'{wire_name}[{wire_msb}:{wire_lsb}]')    
            port_width_list.append(wire_msb - wire_lsb + 1)
        
        assign_str = ''
        if port.direction : 
            if len(wire_list) == 1 : 
                wire_str =  wire_list[0]
            else : 
                wire_str = ''
                for i in range(0, len(wire_list)) : 
                    wire_str = wire_str + ', ' + wire_list[len(wire_list)-1-i]
                wire_str = f'{{ {wire_str[2:]} }}' 
            assign_str = f'assign {port.name} = {wire_str};\n'
        else : 
            if len(wire_list) == 1 : 
                wire_str =  wire_list[0]
                assign_str = f'assign {wire_str} = {port.name};\n'
            else : 
                port_lsb = 0
                for i in range(0, len(wire_list)):
                    port_msb = port_width_list[i] + port_lsb - 1
                    if port_msb == port_lsb : 
                        assign_str = assign_str + \
                            f'assign {wire_list[i]} = {port.name}[{port_msb}];\n'
                    else : 
                        assign_str = assign_str + \
                            f'assign {wire_list[i]} = {port.name}[{port_msb}:{port_lsb}];\n'
                    port_lsb = port_msb + 1
            
        module_assign_define = module_assign_define + assign_str

    module_inst_define = ''
    for inst in module.inst_dict.values() : 

        inst_port_str = ''
        for port in inst.port_dict.values() : 
            wire_list = []
            wire_name = ''
            wire_lsb = 0
            wire_msb = 0
            for i in range(port.lsb, port.msb + 1) : 
                _connect = port.wire_connect[i]
                if wire_name == _connect[0] : 
                    if wire_msb + 1 == _connect[1] : 
                        wire_msb = _connect[1]
                    else :
                        if module.wire_dict[wire_name].lsb == wire_lsb \
                            and module.wire_dict[wire_name].msb == wire_msb : 
                            wire_list.append(f'{wire_name}')
                        else :
                            if wire_lsb == wire_msb : 
                                wire_list.append(f'{wire_name}[{wire_lsb}]')
                            else : 
                                wire_list.append(f'{wire_name}[{wire_msb}:{wire_lsb}]')

                        wire_name = _connect[0]
                        wire_lsb = _connect[1]
                        wire_msb = _connect[1]
                else :
                    if wire_name != '' : 
                        if module.wire_dict[wire_name].lsb == wire_lsb \
                            and module.wire_dict[wire_name].msb == wire_msb : 
                            wire_list.append(f'{wire_name}')
                        else :
                            if wire_lsb == wire_msb : 
                                wire_list.append(f'{wire_name}[{wire_lsb}]')
                            else : 
                                wire_list.append(f'{wire_name}[{wire_msb}:{wire_lsb}]')
                    wire_name = _connect[0]
                    wire_lsb = _connect[1]
                    wire_msb = _connect[1]
            if wire_name != '' : 
                if module.wire_dict[wire_name].lsb == wire_lsb \
                    and module.wire_dict[wire_name].msb == wire_msb : 
                    wire_list.append(f'{wire_name}')
                else :
                    if wire_lsb == wire_msb : 
                        wire_list.append(f'{wire_name}[{wire_lsb}]')
                    else : 
                        wire_list.append(f'{wire_name}[{wire_msb}:{wire_lsb}]')
            
            if len(wire_list) == 1 : 
                port_str = f'.{port.name}( {wire_list[0]} ), '
            else : 
                wire_str = ''
                for i in range(0, len(wire_list)) : 
                    wire_str = wire_str + ', ' + wire_list[len(wire_list)-1-i]
                wire_str = f'{{ {wire_str[2:]} }}' 
                port_str = f'.{port.name}( {wire_str} ), '
            inst_port_str = inst_port_str + port_str
        
        inst_port_str = inst_port_str[0 : len(inst_port_str)-2]

        inst_str = f'{inst.module} {inst.name} ( {inst_port_str} );\n'
        module_inst_define = module_inst_define + inst_str

    if filename is None :
        with open(filepath, 'w') as f :
            f.write(module_header)
            f.write(module_port_define)
            f.write(module_wire_define)
            f.write(module_assign_define)
            f.write(module_inst_define)
            f.write(module_end)
    else : 
        with open(filepath, 'a') as f :
            f.write(module_header)
            f.write(module_port_define)
            f.write(module_wire_define)
            f.write(module_assign_define)
            f.write(module_inst_define)
            f.write(module_end)

