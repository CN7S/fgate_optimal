module gf_mul_128 ( a, b, c, C_g1, rst_n );
  input [127:0] a;
  input [127:0] b;
  input [21:0] C_g1;
  input rst_n;
  output [127:0] c;

  wire   [254:0] d;

  OKA_128bit mul_128_x ( .a(a), .b(b), .y(d), .C_g1(C_g1), .rst_n(rst_n) );

  reduction reduction_x ( .a(d), .b(c), .C_g1(C_g1), .rst_n(rst_n) );
endmodule
