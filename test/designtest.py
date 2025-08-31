import sys
sys.path.append('./')

from Mydesigner.design import Design
from Mydesigner.optimization import OptEngine

gatelib_path = 'test/gatelib'
# modulelib_path = 'test/testrtl'
# top_design = 'foo_A'

# modulelib_path = 'test/rtldesign'
# modulelib_path = 'test/testrtl2' 
modulelib_path = './test/original_rtl'
top_design = 'gf_mul_128'
saif_path = 'test/saif'


mydesign = Design()
mydesign.addGateLibFromFloder(gatelib_path)

# dump json lib file
lib_dict = {}
for gate_module in mydesign.gate_lib.values() : 
    gate_module.selfUpdated()
    lib_dict[gate_module.name] = gate_module.attr.dumpToDict()
import json
with open('./gate.json', 'w') as f:
    json.dump(lib_dict, f, indent=4)


mydesign.addModuleFromFloder(modulelib_path)
mydesign.setTopDesign(top_design)
mydesign.uniqueModules()
mydesign.linkModuleInst()

#remove some module ports
# remove_ports = ['clk', 'rst_n', 'C_g1']
# for modulename in mydesign.modules:
#     module = mydesign.modules[modulename]
#     for portname in remove_ports:
#         if portname in module.port_dict:
#             mydesign.removeModulePort(modulename, portname)

# input('Press Enter to continue...')
# mydesign.linkModuleInst()

# mydesign.dumpAllModule('./test/original_rtl')

# for modulename in mydesign.modules:
#     mydesign.modules[modulename].dumpjson(f'test/debug/{modulename}.json')

# mydesign.modules[mydesign.top_design].dumpjson('log')
mydesign.genGateNetwork()
mydesign.checkGateNetwork()
mydesign.runSTA(result_log=False)
delay_dict = mydesign.getMoudleOutputDelay('OKA_16bit_0')
ypoints = []
for k, v in delay_dict.items():
    ypoints.append(v)
    print(f'Output {k} : Delay = {v:.2e}')

mydesign.gate_net.printStatus()
import matplotlib.pyplot as plt
xpoints = [x for x in range(len(delay_dict))]
plt.scatter(xpoints, ypoints)
plt.show()


# mydesign.gate_net.gate_dict['OKA_8bit_0_0.U22'].status()
# mydesign.gate_net.gate_dict['OKA_8bit_2_0.U22'].status()

# input('Press Enter to continue...')
# mydesign.printWireDriver()
# mydesign.printModulePortDriver('OKA_128bit_0')
# input('Press Enter to continue...')
# mydesign.gate_net.staticTimingAnalysis()
# mydesign.gate_net.printStatus()

# mydesign.netAnnotation(saif_path, 'gfmul_tb/mul_x/mul_x')

# engine = OptEngine(mydesign)
# engine.fgate_cutset_opt()



