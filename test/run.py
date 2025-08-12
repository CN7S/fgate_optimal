from verilog_parser import parser 

with open('test.v', 'r') as f:
    input = f.read()

modulelist = parser.parse(input)
print(modulelist)