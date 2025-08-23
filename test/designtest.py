import sys
sys.path.append('./')

from Mydesigner.design import Design
from Mydesigner.optimization import OptEngine

gatelib_path = 'test/gatelib'
# modulelib_path = 'test/testrtl'
# top_design = 'foo_A'

modulelib_path = 'test/rtldesign'
top_design = 'gf_mul_128'
saif_path = 'test/saif'


mydesign = Design()
mydesign.addGateLibFromFloder(gatelib_path)
mydesign.addModuleFromFloder(modulelib_path)
mydesign.setTopDesign(top_design)
mydesign.uniqueModules()
mydesign.updateModuleInst()
mydesign.dumpAllModule('./test/dumprtl_test')

# for modulename in mydesign.modules:
#     mydesign.modules[modulename].dumpjson(f'test/debug/{modulename}.json')

# mydesign.modules[mydesign.top_design].dumpjson('log')
mydesign.genGateNetwork()

# mydesign.netAnnotation(saif_path, 'gfmul_tb/mul_x/mul_x')

# engine = OptEngine(mydesign)
# engine.fgate_cutset_opt()



