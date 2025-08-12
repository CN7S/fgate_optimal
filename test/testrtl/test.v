module foo_A (a,b,c,z);

input [2:0] a;
input [1:0] b;
output [2:0] c;
output z;
wire [1:0] d;
    foo_B F0 (.a(a), .b(d), .c(c));

    XOR2UD1BWP30P140 U1 ( .A1(a[0]), .A2(b[0]), .Z(d[0]));
    XOR2UD1BWP30P140 U2 ( .A1(a[1]), .A2(b[1]), .Z(d[1]));
    XOR2UD1BWP30P140 U3 ( .A1(c[1]), .A2(c[0]), .Z(z));

endmodule

module foo_B (a,b,c);

input [2:0] a;
input [1:0] b;
output [2:0] c;

wire n1;

    assign c[1] = b[1];
    assign c[2] = b[0];

    XOR2UD1BWP30P140 U1 ( .A1(a[0]), .A2(a[1]), .Z(n1));
    XOR2UD1BWP30P140 U2 ( .A1(n1), .A2(a[2]), .Z(c[0]));

endmodule
