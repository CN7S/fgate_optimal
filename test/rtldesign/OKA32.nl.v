
// KA 32 type , 2-term
module OKA_32bit
(
   input [31:0] a,
   input [31:0] b,
   output [62:0] y
);
// wire 
wire [15:0] aa;
wire [15:0] bb;
wire [15:0] al;
wire [15:0] ah;
wire [15:0] bl;
wire [15:0] bh;
wire [30:0] z0;
wire [30:0] z1;
wire [30:0] z2;
wire [30:0] o1;
assign al[0] = a[0];
assign al[1] = a[1];
assign al[2] = a[2];
assign al[3] = a[3];
assign al[4] = a[4];
assign al[5] = a[5];
assign al[6] = a[6];
assign al[7] = a[7];
assign al[8] = a[8];
assign al[9] = a[9];
assign al[10] = a[10];
assign al[11] = a[11];
assign al[12] = a[12];
assign al[13] = a[13];
assign al[14] = a[14];
assign al[15] = a[15];
assign ah[0] = a[16];
assign ah[1] = a[17];
assign ah[2] = a[18];
assign ah[3] = a[19];
assign ah[4] = a[20];
assign ah[5] = a[21];
assign ah[6] = a[22];
assign ah[7] = a[23];
assign ah[8] = a[24];
assign ah[9] = a[25];
assign ah[10] = a[26];
assign ah[11] = a[27];
assign ah[12] = a[28];
assign ah[13] = a[29];
assign ah[14] = a[30];
assign ah[15] = a[31];
assign bl[0] = b[0];
assign bl[1] = b[1];
assign bl[2] = b[2];
assign bl[3] = b[3];
assign bl[4] = b[4];
assign bl[5] = b[5];
assign bl[6] = b[6];
assign bl[7] = b[7];
assign bl[8] = b[8];
assign bl[9] = b[9];
assign bl[10] = b[10];
assign bl[11] = b[11];
assign bl[12] = b[12];
assign bl[13] = b[13];
assign bl[14] = b[14];
assign bl[15] = b[15];
assign bh[0] = b[16];
assign bh[1] = b[17];
assign bh[2] = b[18];
assign bh[3] = b[19];
assign bh[4] = b[20];
assign bh[5] = b[21];
assign bh[6] = b[22];
assign bh[7] = b[23];
assign bh[8] = b[24];
assign bh[9] = b[25];
assign bh[10] = b[26];
assign bh[11] = b[27];
assign bh[12] = b[28];
assign bh[13] = b[29];
assign bh[14] = b[30];
assign bh[15] = b[31];
s_32bit s32_u
(
   .a(a),
   .b(b),
   .aa(aa),
   .bb(bb)
);
OKA_16bit mul16_0
(
.a(al),
.b(bl),
.y(z0)
);
OKA_16bit mul16_1
(
.a(aa),
.b(bb),
.y(z1)
);
OKA_16bit mul16_2
(
.a(ah),
.b(bh),
.y(z2)
);
os_32bit os32_u
(
   .z0(z0),
   .z1(z1),
   .z2(z2),
   .y(y[46:16])
);
assign y[0] = z0[0];
assign y[1] = z0[1];
assign y[2] = z0[2];
assign y[3] = z0[3];
assign y[4] = z0[4];
assign y[5] = z0[5];
assign y[6] = z0[6];
assign y[7] = z0[7];
assign y[8] = z0[8];
assign y[9] = z0[9];
assign y[10] = z0[10];
assign y[11] = z0[11];
assign y[12] = z0[12];
assign y[13] = z0[13];
assign y[14] = z0[14];
assign y[15] = z0[15];
assign y[47] = z2[15];
assign y[48] = z2[16];
assign y[49] = z2[17];
assign y[50] = z2[18];
assign y[51] = z2[19];
assign y[52] = z2[20];
assign y[53] = z2[21];
assign y[54] = z2[22];
assign y[55] = z2[23];
assign y[56] = z2[24];
assign y[57] = z2[25];
assign y[58] = z2[26];
assign y[59] = z2[27];
assign y[60] = z2[28];
assign y[61] = z2[29];
assign y[62] = z2[30];
endmodule
// slice 
module s_32bit
(
   input [31:0] a,
   input [31:0] b,
   output [15:0] aa,
   output [15:0] bb
);
XOR2UD1BWP30P140 U0 ( .A1(a[0]), .A2(a[16]), .Z(aa[0]) );
XOR2UD1BWP30P140 U1 ( .A1(a[1]), .A2(a[17]), .Z(aa[1]) );
XOR2UD1BWP30P140 U2 ( .A1(a[2]), .A2(a[18]), .Z(aa[2]) );
XOR2UD1BWP30P140 U3 ( .A1(a[3]), .A2(a[19]), .Z(aa[3]) );
XOR2UD1BWP30P140 U4 ( .A1(a[4]), .A2(a[20]), .Z(aa[4]) );
XOR2UD1BWP30P140 U5 ( .A1(a[5]), .A2(a[21]), .Z(aa[5]) );
XOR2UD1BWP30P140 U6 ( .A1(a[6]), .A2(a[22]), .Z(aa[6]) );
XOR2UD1BWP30P140 U7 ( .A1(a[7]), .A2(a[23]), .Z(aa[7]) );
XOR2UD1BWP30P140 U8 ( .A1(a[8]), .A2(a[24]), .Z(aa[8]) );
XOR2UD1BWP30P140 U9 ( .A1(a[9]), .A2(a[25]), .Z(aa[9]) );
XOR2UD1BWP30P140 U10 ( .A1(a[10]), .A2(a[26]), .Z(aa[10]) );
XOR2UD1BWP30P140 U11 ( .A1(a[11]), .A2(a[27]), .Z(aa[11]) );
XOR2UD1BWP30P140 U12 ( .A1(a[12]), .A2(a[28]), .Z(aa[12]) );
XOR2UD1BWP30P140 U13 ( .A1(a[13]), .A2(a[29]), .Z(aa[13]) );
XOR2UD1BWP30P140 U14 ( .A1(a[14]), .A2(a[30]), .Z(aa[14]) );
XOR2UD1BWP30P140 U15 ( .A1(a[15]), .A2(a[31]), .Z(aa[15]) );
XOR2UD1BWP30P140 U16 ( .A1(b[0]), .A2(b[16]), .Z(bb[0]) );
XOR2UD1BWP30P140 U17 ( .A1(b[1]), .A2(b[17]), .Z(bb[1]) );
XOR2UD1BWP30P140 U18 ( .A1(b[2]), .A2(b[18]), .Z(bb[2]) );
XOR2UD1BWP30P140 U19 ( .A1(b[3]), .A2(b[19]), .Z(bb[3]) );
XOR2UD1BWP30P140 U20 ( .A1(b[4]), .A2(b[20]), .Z(bb[4]) );
XOR2UD1BWP30P140 U21 ( .A1(b[5]), .A2(b[21]), .Z(bb[5]) );
XOR2UD1BWP30P140 U22 ( .A1(b[6]), .A2(b[22]), .Z(bb[6]) );
XOR2UD1BWP30P140 U23 ( .A1(b[7]), .A2(b[23]), .Z(bb[7]) );
XOR2UD1BWP30P140 U24 ( .A1(b[8]), .A2(b[24]), .Z(bb[8]) );
XOR2UD1BWP30P140 U25 ( .A1(b[9]), .A2(b[25]), .Z(bb[9]) );
XOR2UD1BWP30P140 U26 ( .A1(b[10]), .A2(b[26]), .Z(bb[10]) );
XOR2UD1BWP30P140 U27 ( .A1(b[11]), .A2(b[27]), .Z(bb[11]) );
XOR2UD1BWP30P140 U28 ( .A1(b[12]), .A2(b[28]), .Z(bb[12]) );
XOR2UD1BWP30P140 U29 ( .A1(b[13]), .A2(b[29]), .Z(bb[13]) );
XOR2UD1BWP30P140 U30 ( .A1(b[14]), .A2(b[30]), .Z(bb[14]) );
XOR2UD1BWP30P140 U31 ( .A1(b[15]), .A2(b[31]), .Z(bb[15]) );
endmodule
module os_32bit
(
   input [30:0] z0,
   input [30:0] z1,
   input [30:0] z2,
   output [30:0] y
);

wire n0, n1, n2, n3, n4, n5, n6, n7, n8, n9,
   n10,n11,n12,n13,n14;

XOR2UD1BWP30P140 U0 ( .A1(z2[0]), .A2(z0[16]), .Z(n0) );
XOR2UD1BWP30P140 U1 ( .A1(z2[1]), .A2(z0[17]), .Z(n1) );
XOR2UD1BWP30P140 U2 ( .A1(z2[2]), .A2(z0[18]), .Z(n2) );
XOR2UD1BWP30P140 U3 ( .A1(z2[3]), .A2(z0[19]), .Z(n3) );
XOR2UD1BWP30P140 U4 ( .A1(z2[4]), .A2(z0[20]), .Z(n4) );
XOR2UD1BWP30P140 U5 ( .A1(z2[5]), .A2(z0[21]), .Z(n5) );
XOR2UD1BWP30P140 U6 ( .A1(z2[6]), .A2(z0[22]), .Z(n6) );
XOR2UD1BWP30P140 U7 ( .A1(z2[7]), .A2(z0[23]), .Z(n7) );
XOR2UD1BWP30P140 U8 ( .A1(z2[8]), .A2(z0[24]), .Z(n8) );
XOR2UD1BWP30P140 U9 ( .A1(z2[9]), .A2(z0[25]), .Z(n9) );
XOR2UD1BWP30P140 U10 ( .A1(z2[10]), .A2(z0[26]), .Z(n10) );
XOR2UD1BWP30P140 U11 ( .A1(z2[11]), .A2(z0[27]), .Z(n11) );
XOR2UD1BWP30P140 U12 ( .A1(z2[12]), .A2(z0[28]), .Z(n12) );
XOR2UD1BWP30P140 U13 ( .A1(z2[13]), .A2(z0[29]), .Z(n13) );
XOR2UD1BWP30P140 U14 ( .A1(z2[14]), .A2(z0[30]), .Z(n14) );

XOR3UD1BWP30P140 U15 ( .A1(z1[0]), .A2(z0[0]), .A3(n0), .Z(y[0]) );
XOR3UD1BWP30P140 U16 ( .A1(z1[1]), .A2(z0[1]), .A3(n1), .Z(y[1]) );
XOR3UD1BWP30P140 U17 ( .A1(z1[2]), .A2(z0[2]), .A3(n2), .Z(y[2]) );
XOR3UD1BWP30P140 U18 ( .A1(z1[3]), .A2(z0[3]), .A3(n3), .Z(y[3]) );
XOR3UD1BWP30P140 U19 ( .A1(z1[4]), .A2(z0[4]), .A3(n4), .Z(y[4]) );
XOR3UD1BWP30P140 U20 ( .A1(z1[5]), .A2(z0[5]), .A3(n5), .Z(y[5]) );
XOR3UD1BWP30P140 U21 ( .A1(z1[6]), .A2(z0[6]), .A3(n6), .Z(y[6]) );
XOR3UD1BWP30P140 U22 ( .A1(z1[7]), .A2(z0[7]), .A3(n7), .Z(y[7]) );
XOR3UD1BWP30P140 U23 ( .A1(z1[8]), .A2(z0[8]), .A3(n8), .Z(y[8]) );
XOR3UD1BWP30P140 U24 ( .A1(z1[9]), .A2(z0[9]), .A3(n9), .Z(y[9]) );
XOR3UD1BWP30P140 U25 ( .A1(z1[10]), .A2(z0[10]), .A3(n10), .Z(y[10]) );
XOR3UD1BWP30P140 U26 ( .A1(z1[11]), .A2(z0[11]), .A3(n11), .Z(y[11]) );
XOR3UD1BWP30P140 U27 ( .A1(z1[12]), .A2(z0[12]), .A3(n12), .Z(y[12]) );
XOR3UD1BWP30P140 U28 ( .A1(z1[13]), .A2(z0[13]), .A3(n13), .Z(y[13]) );
XOR3UD1BWP30P140 U29 ( .A1(z1[14]), .A2(z0[14]), .A3(n14), .Z(y[14]) );
XOR3UD1BWP30P140 U30 ( .A1(z2[15]), .A2(z1[15]), .A3(z0[15]), .Z(y[15]) );
XOR3UD1BWP30P140 U31 ( .A1(z1[16]), .A2(z2[16]), .A3(n0), .Z(y[16]) );
XOR3UD1BWP30P140 U32 ( .A1(z1[17]), .A2(z2[17]), .A3(n1), .Z(y[17]) );
XOR3UD1BWP30P140 U33 ( .A1(z1[18]), .A2(z2[18]), .A3(n2), .Z(y[18]) );
XOR3UD1BWP30P140 U34 ( .A1(z1[19]), .A2(z2[19]), .A3(n3), .Z(y[19]) );
XOR3UD1BWP30P140 U35 ( .A1(z1[20]), .A2(z2[20]), .A3(n4), .Z(y[20]) );
XOR3UD1BWP30P140 U36 ( .A1(z1[21]), .A2(z2[21]), .A3(n5), .Z(y[21]) );
XOR3UD1BWP30P140 U37 ( .A1(z1[22]), .A2(z2[22]), .A3(n6), .Z(y[22]) );
XOR3UD1BWP30P140 U38 ( .A1(z1[23]), .A2(z2[23]), .A3(n7), .Z(y[23]) );
XOR3UD1BWP30P140 U39 ( .A1(z1[24]), .A2(z2[24]), .A3(n8), .Z(y[24]) );
XOR3UD1BWP30P140 U40 ( .A1(z1[25]), .A2(z2[25]), .A3(n9), .Z(y[25]) );
XOR3UD1BWP30P140 U41 ( .A1(z1[26]), .A2(z2[26]), .A3(n10), .Z(y[26]) );
XOR3UD1BWP30P140 U42 ( .A1(z1[27]), .A2(z2[27]), .A3(n11), .Z(y[27]) );
XOR3UD1BWP30P140 U43 ( .A1(z1[28]), .A2(z2[28]), .A3(n12), .Z(y[28]) );
XOR3UD1BWP30P140 U44 ( .A1(z1[29]), .A2(z2[29]), .A3(n13), .Z(y[29]) );
XOR3UD1BWP30P140 U45 ( .A1(z1[30]), .A2(z2[30]), .A3(n14), .Z(y[30]) );
endmodule