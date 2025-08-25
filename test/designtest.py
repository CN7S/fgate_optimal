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
print(mydesign.gate_net.checkCircular())
input('Press Enter to continue...')
mydesign.gate_net.staticTimingAnalysis()
mydesign.gate_net.printStatus()

# mydesign.netAnnotation(saif_path, 'gfmul_tb/mul_x/mul_x')

# engine = OptEngine(mydesign)
# engine.fgate_cutset_opt()



