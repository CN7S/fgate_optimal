import sys
sys.path.append('./')

from Mydesigner.design import Design

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

# for modulename in mydesign.modules:
#     mydesign.modules[modulename].dumpjson(f'test/debug/{modulename}.json')

# mydesign.modules[mydesign.top_design].dumpjson('log')
mydesign.genGateNetwork()

# mydesign.netAnnotation(saif_path, 'gfmul_tb/mul_x/mul_x')


