from verilog_parser.netlist import Module
import os

def dumpModule(module : Module, filepath : str) :

    
    module_name = module.name
    filepath = os.path.join(filepath, f'{module_name}.v')

    # module.dumpjson(filepath)

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
    for wire in module.wire_dict.values() : 
        wire_width = wire.msb - wire.lsb + 1
        if wire_width == 1 :
            wiredef = f'wire {wire.name};\n'
        else :
            wiredef = f'wire [{wire_width-1}:0] {wire.name};\n'
    module_wire_define = module_wire_define + wiredef


    module_assign_define = ''
    for port in module.port_dict.values() : 
        for i in range(port.lsb, port.msb + 1) : 
            _connect = port.wire_connect[i]
            if port.msb == 0 : 
                port_str = f'{port.name}'
            else :
                port_str = f'{port.name}[{i}]'
            
            if module.wire_dict[_connect[0]].msb == 0 :
                wire_str = f'{_connect[0]}'
            else :
                wire_str = f'{_connect[0]}[{_connect[1]}]'
            
            if port.direction : 
                assign_str = f'assign {port_str} = {wire_str};\n'
            else : 
                assign_str = f'assign {wire_str} = {port_str};\n'
            
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

                        if wire_name != '' : 
                            if module.wire_dict[wire_name].lsb == wire_lsb \
                                and module.wire_dict[wire_name].msb == wire_msb : 
                                wire_list.append(f'{wire_name}')
                            else :
                                if wire_lsb == wire_msb : 
                                    wire_list.append(f'{wire_name}[{wire_lsb}]')
                                else : 
                                    wire_list.append(f'{wire_name}[{wire_msb}:{wire_lsb}]')

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
                port_str = f'.{port.name}( {wire_list[0]} ), \n'
            else : 
                wire_str = ''
                for i in wire_list : 
                    wire_str = wire_str + ', ' + i
                wire_str = f'{{ {wire_str[2:]} }}' 
                port_str = f'.{port.name}( {wire_str} ), \n'
            inst_port_str = inst_port_str + port_str
        
        inst_port_str = inst_port_str[0 : len(inst_port_str)-3]

        inst_str = f'{inst.module} {inst.name} ( {inst_port_str} );\n'
        module_inst_define = module_inst_define + inst_str

    with open(filepath, 'w') as f :
        f.write(module_header)
        f.write(module_port_define)
        f.write(module_wire_define)
        f.write(module_assign_define)
        f.write(module_inst_define)
        f.write(module_end)
