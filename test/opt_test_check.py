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
mydesign.linkModuleInst() # connect wire to Port



# mydesign.genGateNetwork()
# mydesign.checkGateNetwork()
# mydesign.runSTA(result_log=False)
# mydesign.netAnnotation(saif_path, 'gfmul_tb/mul_x/mul_x')

engine = OptEngine(mydesign)
mydesign.netAnnotation(saif_path, 'gfmul_tb/mul_x/mul_x', 100)
mydesign.gate_net.printStatus()
mydesign.netAnnotation(saif_path, 'gfmul_tb/mul_x/mul_x', 100, glitch_inst_path='gfmul_tb/mul_x/mul_x/U0', glitch_file_name='opt.saif')
mydesign.gate_net.printStatus()




