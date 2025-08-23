module gf_mul_128_0 ( a, b, C_g1, rst_n, c );
input [127:0] a;
input [127:0] b;
input [21:0] C_g1;
input rst_n;
output [127:0] c;
wire [254:0] d;
assign _a = a;
assign _b = b;
assign _C_g1 = C_g1;
assign _rst_n = rst_n;
assign c = _c;
OKA_128bit_0 mul_128_x ( .a( _a ), 
.b( _b ), 
.y( d ), 
.C_g1( _C_g1 ), 
.rst_n( _rst_n ) );
reduction_0 reduction_x ( .a( d ), 
.C_g1( _C_g1 ), 
.rst_n( _rst_n ), 
.b( _c ) );
endmodule
