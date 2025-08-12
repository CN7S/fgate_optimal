
// KA 64 type , 2-term
module OKA_64bit
(
   input [63:0] a,
   input [63:0] b,
   output [126:0] y,
   input [21:0] C_g1,
   input rst_n
);
// wire 
wire [31:0] aa;
wire [31:0] bb;
wire [31:0] al;
wire [31:0] ah;
wire [31:0] bl;
wire [31:0] bh;
wire [62:0] z0;
wire [62:0] z1;
wire [62:0] z2;
wire [62:0] o1;
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
assign al[16] = a[16];
assign al[17] = a[17];
assign al[18] = a[18];
assign al[19] = a[19];
assign al[20] = a[20];
assign al[21] = a[21];
assign al[22] = a[22];
assign al[23] = a[23];
assign al[24] = a[24];
assign al[25] = a[25];
assign al[26] = a[26];
assign al[27] = a[27];
assign al[28] = a[28];
assign al[29] = a[29];
assign al[30] = a[30];
assign al[31] = a[31];
assign ah[0] = a[32];
assign ah[1] = a[33];
assign ah[2] = a[34];
assign ah[3] = a[35];
assign ah[4] = a[36];
assign ah[5] = a[37];
assign ah[6] = a[38];
assign ah[7] = a[39];
assign ah[8] = a[40];
assign ah[9] = a[41];
assign ah[10] = a[42];
assign ah[11] = a[43];
assign ah[12] = a[44];
assign ah[13] = a[45];
assign ah[14] = a[46];
assign ah[15] = a[47];
assign ah[16] = a[48];
assign ah[17] = a[49];
assign ah[18] = a[50];
assign ah[19] = a[51];
assign ah[20] = a[52];
assign ah[21] = a[53];
assign ah[22] = a[54];
assign ah[23] = a[55];
assign ah[24] = a[56];
assign ah[25] = a[57];
assign ah[26] = a[58];
assign ah[27] = a[59];
assign ah[28] = a[60];
assign ah[29] = a[61];
assign ah[30] = a[62];
assign ah[31] = a[63];
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
assign bl[16] = b[16];
assign bl[17] = b[17];
assign bl[18] = b[18];
assign bl[19] = b[19];
assign bl[20] = b[20];
assign bl[21] = b[21];
assign bl[22] = b[22];
assign bl[23] = b[23];
assign bl[24] = b[24];
assign bl[25] = b[25];
assign bl[26] = b[26];
assign bl[27] = b[27];
assign bl[28] = b[28];
assign bl[29] = b[29];
assign bl[30] = b[30];
assign bl[31] = b[31];
assign bh[0] = b[32];
assign bh[1] = b[33];
assign bh[2] = b[34];
assign bh[3] = b[35];
assign bh[4] = b[36];
assign bh[5] = b[37];
assign bh[6] = b[38];
assign bh[7] = b[39];
assign bh[8] = b[40];
assign bh[9] = b[41];
assign bh[10] = b[42];
assign bh[11] = b[43];
assign bh[12] = b[44];
assign bh[13] = b[45];
assign bh[14] = b[46];
assign bh[15] = b[47];
assign bh[16] = b[48];
assign bh[17] = b[49];
assign bh[18] = b[50];
assign bh[19] = b[51];
assign bh[20] = b[52];
assign bh[21] = b[53];
assign bh[22] = b[54];
assign bh[23] = b[55];
assign bh[24] = b[56];
assign bh[25] = b[57];
assign bh[26] = b[58];
assign bh[27] = b[59];
assign bh[28] = b[60];
assign bh[29] = b[61];
assign bh[30] = b[62];
assign bh[31] = b[63];
s_64bit s64_u
(
   .a(a),
   .b(b),
   .aa(aa),
   .bb(bb)
);
OKA_32bit mul32_0
(
.a(al),
.b(bl),
.y(z0)
);
OKA_32bit mul32_1
(
.a(aa),
.b(bb),
.y(z1)
);
OKA_32bit mul32_2
(
.a(ah),
.b(bh),
.y(z2)
);
os_64bit os64_u
(
.rst_n(rst_n),
.C_g1(C_g1),
   .z0(z0),
   .z1(z1),
   .z2(z2),
   .y(y[94:32])
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
assign y[16] = z0[16];
assign y[17] = z0[17];
assign y[18] = z0[18];
assign y[19] = z0[19];
assign y[20] = z0[20];
assign y[21] = z0[21];
assign y[22] = z0[22];
assign y[23] = z0[23];
assign y[24] = z0[24];
assign y[25] = z0[25];
assign y[26] = z0[26];
assign y[27] = z0[27];
assign y[28] = z0[28];
assign y[29] = z0[29];
assign y[30] = z0[30];
assign y[31] = z0[31];
assign y[95] = z2[31];
assign y[96] = z2[32];
assign y[97] = z2[33];
assign y[98] = z2[34];
assign y[99] = z2[35];
assign y[100] = z2[36];
assign y[101] = z2[37];
assign y[102] = z2[38];
assign y[103] = z2[39];
assign y[104] = z2[40];
assign y[105] = z2[41];
assign y[106] = z2[42];
assign y[107] = z2[43];
assign y[108] = z2[44];
assign y[109] = z2[45];
assign y[110] = z2[46];
assign y[111] = z2[47];
assign y[112] = z2[48];
assign y[113] = z2[49];
assign y[114] = z2[50];
assign y[115] = z2[51];
assign y[116] = z2[52];
assign y[117] = z2[53];
assign y[118] = z2[54];
assign y[119] = z2[55];
assign y[120] = z2[56];
assign y[121] = z2[57];
assign y[122] = z2[58];
assign y[123] = z2[59];
assign y[124] = z2[60];
assign y[125] = z2[61];
assign y[126] = z2[62];
endmodule
// slice 
module s_64bit
(
   input [63:0] a,
   input [63:0] b,
   output [31:0] aa,
   output [31:0] bb
);
XOR2UD1BWP30P140 U0 ( .A1(a[0]), .A2(a[32]), .Z(aa[0]) );
XOR2UD1BWP30P140 U1 ( .A1(a[1]), .A2(a[33]), .Z(aa[1]) );
XOR2UD1BWP30P140 U2 ( .A1(a[2]), .A2(a[34]), .Z(aa[2]) );
XOR2UD1BWP30P140 U3 ( .A1(a[3]), .A2(a[35]), .Z(aa[3]) );
XOR2UD1BWP30P140 U4 ( .A1(a[4]), .A2(a[36]), .Z(aa[4]) );
XOR2UD1BWP30P140 U5 ( .A1(a[5]), .A2(a[37]), .Z(aa[5]) );
XOR2UD1BWP30P140 U6 ( .A1(a[6]), .A2(a[38]), .Z(aa[6]) );
XOR2UD1BWP30P140 U7 ( .A1(a[7]), .A2(a[39]), .Z(aa[7]) );
XOR2UD1BWP30P140 U8 ( .A1(a[8]), .A2(a[40]), .Z(aa[8]) );
XOR2UD1BWP30P140 U9 ( .A1(a[9]), .A2(a[41]), .Z(aa[9]) );
XOR2UD1BWP30P140 U10 ( .A1(a[10]), .A2(a[42]), .Z(aa[10]) );
XOR2UD1BWP30P140 U11 ( .A1(a[11]), .A2(a[43]), .Z(aa[11]) );
XOR2UD1BWP30P140 U12 ( .A1(a[12]), .A2(a[44]), .Z(aa[12]) );
XOR2UD1BWP30P140 U13 ( .A1(a[13]), .A2(a[45]), .Z(aa[13]) );
XOR2UD1BWP30P140 U14 ( .A1(a[14]), .A2(a[46]), .Z(aa[14]) );
XOR2UD1BWP30P140 U15 ( .A1(a[15]), .A2(a[47]), .Z(aa[15]) );
XOR2UD1BWP30P140 U16 ( .A1(a[16]), .A2(a[48]), .Z(aa[16]) );
XOR2UD1BWP30P140 U17 ( .A1(a[17]), .A2(a[49]), .Z(aa[17]) );
XOR2UD1BWP30P140 U18 ( .A1(a[18]), .A2(a[50]), .Z(aa[18]) );
XOR2UD1BWP30P140 U19 ( .A1(a[19]), .A2(a[51]), .Z(aa[19]) );
XOR2UD1BWP30P140 U20 ( .A1(a[20]), .A2(a[52]), .Z(aa[20]) );
XOR2UD1BWP30P140 U21 ( .A1(a[21]), .A2(a[53]), .Z(aa[21]) );
XOR2UD1BWP30P140 U22 ( .A1(a[22]), .A2(a[54]), .Z(aa[22]) );
XOR2UD1BWP30P140 U23 ( .A1(a[23]), .A2(a[55]), .Z(aa[23]) );
XOR2UD1BWP30P140 U24 ( .A1(a[24]), .A2(a[56]), .Z(aa[24]) );
XOR2UD1BWP30P140 U25 ( .A1(a[25]), .A2(a[57]), .Z(aa[25]) );
XOR2UD1BWP30P140 U26 ( .A1(a[26]), .A2(a[58]), .Z(aa[26]) );
XOR2UD1BWP30P140 U27 ( .A1(a[27]), .A2(a[59]), .Z(aa[27]) );
XOR2UD1BWP30P140 U28 ( .A1(a[28]), .A2(a[60]), .Z(aa[28]) );
XOR2UD1BWP30P140 U29 ( .A1(a[29]), .A2(a[61]), .Z(aa[29]) );
XOR2UD1BWP30P140 U30 ( .A1(a[30]), .A2(a[62]), .Z(aa[30]) );
XOR2UD1BWP30P140 U31 ( .A1(a[31]), .A2(a[63]), .Z(aa[31]) );
XOR2UD1BWP30P140 U32 ( .A1(b[0]), .A2(b[32]), .Z(bb[0]) );
XOR2UD1BWP30P140 U33 ( .A1(b[1]), .A2(b[33]), .Z(bb[1]) );
XOR2UD1BWP30P140 U34 ( .A1(b[2]), .A2(b[34]), .Z(bb[2]) );
XOR2UD1BWP30P140 U35 ( .A1(b[3]), .A2(b[35]), .Z(bb[3]) );
XOR2UD1BWP30P140 U36 ( .A1(b[4]), .A2(b[36]), .Z(bb[4]) );
XOR2UD1BWP30P140 U37 ( .A1(b[5]), .A2(b[37]), .Z(bb[5]) );
XOR2UD1BWP30P140 U38 ( .A1(b[6]), .A2(b[38]), .Z(bb[6]) );
XOR2UD1BWP30P140 U39 ( .A1(b[7]), .A2(b[39]), .Z(bb[7]) );
XOR2UD1BWP30P140 U40 ( .A1(b[8]), .A2(b[40]), .Z(bb[8]) );
XOR2UD1BWP30P140 U41 ( .A1(b[9]), .A2(b[41]), .Z(bb[9]) );
XOR2UD1BWP30P140 U42 ( .A1(b[10]), .A2(b[42]), .Z(bb[10]) );
XOR2UD1BWP30P140 U43 ( .A1(b[11]), .A2(b[43]), .Z(bb[11]) );
XOR2UD1BWP30P140 U44 ( .A1(b[12]), .A2(b[44]), .Z(bb[12]) );
XOR2UD1BWP30P140 U45 ( .A1(b[13]), .A2(b[45]), .Z(bb[13]) );
XOR2UD1BWP30P140 U46 ( .A1(b[14]), .A2(b[46]), .Z(bb[14]) );
XOR2UD1BWP30P140 U47 ( .A1(b[15]), .A2(b[47]), .Z(bb[15]) );
XOR2UD1BWP30P140 U48 ( .A1(b[16]), .A2(b[48]), .Z(bb[16]) );
XOR2UD1BWP30P140 U49 ( .A1(b[17]), .A2(b[49]), .Z(bb[17]) );
XOR2UD1BWP30P140 U50 ( .A1(b[18]), .A2(b[50]), .Z(bb[18]) );
XOR2UD1BWP30P140 U51 ( .A1(b[19]), .A2(b[51]), .Z(bb[19]) );
XOR2UD1BWP30P140 U52 ( .A1(b[20]), .A2(b[52]), .Z(bb[20]) );
XOR2UD1BWP30P140 U53 ( .A1(b[21]), .A2(b[53]), .Z(bb[21]) );
XOR2UD1BWP30P140 U54 ( .A1(b[22]), .A2(b[54]), .Z(bb[22]) );
XOR2UD1BWP30P140 U55 ( .A1(b[23]), .A2(b[55]), .Z(bb[23]) );
XOR2UD1BWP30P140 U56 ( .A1(b[24]), .A2(b[56]), .Z(bb[24]) );
XOR2UD1BWP30P140 U57 ( .A1(b[25]), .A2(b[57]), .Z(bb[25]) );
XOR2UD1BWP30P140 U58 ( .A1(b[26]), .A2(b[58]), .Z(bb[26]) );
XOR2UD1BWP30P140 U59 ( .A1(b[27]), .A2(b[59]), .Z(bb[27]) );
XOR2UD1BWP30P140 U60 ( .A1(b[28]), .A2(b[60]), .Z(bb[28]) );
XOR2UD1BWP30P140 U61 ( .A1(b[29]), .A2(b[61]), .Z(bb[29]) );
XOR2UD1BWP30P140 U62 ( .A1(b[30]), .A2(b[62]), .Z(bb[30]) );
XOR2UD1BWP30P140 U63 ( .A1(b[31]), .A2(b[63]), .Z(bb[31]) );
endmodule

module os_64bit
(
   input [62:0] z0,
   input [62:0] z1,
   input [62:0] z2,
   output [62:0] y,
   input [21:0] C_g1,
   input rst_n
);

wire n0, n1, n2, n3, n4, n5, n6, n7, n8, n9,
   n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20,
   n21,n22,n23,n24,n25,n26,n27,n28,n29,n30;
XOR2UD1BWP30P140 U0 ( .A1(z2[0]), .A2(z0[32]), .Z(n0) );
XOR2UD1BWP30P140 U1 ( .A1(z2[1]), .A2(z0[33]), .Z(n1) );
XOR2UD1BWP30P140 U2 ( .A1(z2[2]), .A2(z0[34]), .Z(n2) );
XOR2UD1BWP30P140 U3 ( .A1(z2[3]), .A2(z0[35]), .Z(n3) );
XOR2UD1BWP30P140 U4 ( .A1(z2[4]), .A2(z0[36]), .Z(n4) );
XOR2UD1BWP30P140 U5 ( .A1(z2[5]), .A2(z0[37]), .Z(n5) );
XOR2UD1BWP30P140 U6 ( .A1(z2[6]), .A2(z0[38]), .Z(n6) );
XOR2UD1BWP30P140 U7 ( .A1(z2[7]), .A2(z0[39]), .Z(n7) );
XOR2UD1BWP30P140 U8 ( .A1(z2[8]), .A2(z0[40]), .Z(n8) );
XOR2UD1BWP30P140 U9 ( .A1(z2[9]), .A2(z0[41]), .Z(n9) );
XOR2UD1BWP30P140 U10 ( .A1(z2[10]), .A2(z0[42]), .Z(n10) );
XOR2UD1BWP30P140 U11 ( .A1(z2[11]), .A2(z0[43]), .Z(n11) );
XOR2UD1BWP30P140 U12 ( .A1(z2[12]), .A2(z0[44]), .Z(n12) );
XOR2UD1BWP30P140 U13 ( .A1(z2[13]), .A2(z0[45]), .Z(n13) );
XOR2UD1BWP30P140 U14 ( .A1(z2[14]), .A2(z0[46]), .Z(n14) );
XOR2UD1BWP30P140 U15 ( .A1(z2[15]), .A2(z0[47]), .Z(n15) );
XOR2UD1BWP30P140 U16 ( .A1(z2[16]), .A2(z0[48]), .Z(n16) );
XOR2UD1BWP30P140 U17 ( .A1(z2[17]), .A2(z0[49]), .Z(n17) );
XOR2UD1BWP30P140 U18 ( .A1(z2[18]), .A2(z0[50]), .Z(n18) );
XOR2UD1BWP30P140 U19 ( .A1(z2[19]), .A2(z0[51]), .Z(n19) );
XOR2UD1BWP30P140 U20 ( .A1(z2[20]), .A2(z0[52]), .Z(n20) );
XOR2UD1BWP30P140 U21 ( .A1(z2[21]), .A2(z0[53]), .Z(n21) );
XOR2UD1BWP30P140 U22 ( .A1(z2[22]), .A2(z0[54]), .Z(n22) );
XOR2UD1BWP30P140 U23 ( .A1(z2[23]), .A2(z0[55]), .Z(n23) );
XOR2UD1BWP30P140 U24 ( .A1(z2[24]), .A2(z0[56]), .Z(n24) );
XOR2UD1BWP30P140 U25 ( .A1(z2[25]), .A2(z0[57]), .Z(n25) );
XOR2UD1BWP30P140 U26 ( .A1(z2[26]), .A2(z0[58]), .Z(n26) );
XOR2UD1BWP30P140 U27 ( .A1(z2[27]), .A2(z0[59]), .Z(n27) );
XOR2UD1BWP30P140 U28 ( .A1(z2[28]), .A2(z0[60]), .Z(n28) );
XOR2UD1BWP30P140 U29 ( .A1(z2[29]), .A2(z0[61]), .Z(n29) );
XOR2UD1BWP30P140 U30 ( .A1(z2[30]), .A2(z0[62]), .Z(n30) );
XOR3UD1BWP30P140 U31 ( .A1(z1[0]), .A2(z0[0]), .A3(n0), .Z(y[0]) );
XOR3UD1BWP30P140 U32 ( .A1(z1[1]), .A2(z0[1]), .A3(n1), .Z(y[1]) );
XOR3UD1BWP30P140 U33 ( .A1(z1[2]), .A2(z0[2]), .A3(n2), .Z(y[2]) );
XOR3UD1BWP30P140 U34 ( .A1(z1[3]), .A2(z0[3]), .A3(n3), .Z(y[3]) );
XOR3UD1BWP30P140 U35 ( .A1(z1[4]), .A2(z0[4]), .A3(n4), .Z(y[4]) );
XOR3UD1BWP30P140 U36 ( .A1(z1[5]), .A2(z0[5]), .A3(n5), .Z(y[5]) );
XOR3UD1BWP30P140 U37 ( .A1(z1[6]), .A2(z0[6]), .A3(n6), .Z(y[6]) );
XOR3UD1BWP30P140 U38 ( .A1(z1[7]), .A2(z0[7]), .A3(n7), .Z(y[7]) );
XOR3UD1BWP30P140 U39 ( .A1(z1[8]), .A2(z0[8]), .A3(n8), .Z(y[8]) );
XOR3UD1BWP30P140 U40 ( .A1(z1[9]), .A2(z0[9]), .A3(n9), .Z(y[9]) );
XOR3UD1BWP30P140 U41 ( .A1(z1[10]), .A2(z0[10]), .A3(n10), .Z(y[10]) );
XOR3UD1BWP30P140 U42 ( .A1(z1[11]), .A2(z0[11]), .A3(n11), .Z(y[11]) );
XOR3UD1BWP30P140 U43 ( .A1(z1[12]), .A2(z0[12]), .A3(n12), .Z(y[12]) );
XOR3UD1BWP30P140 U44 ( .A1(z1[13]), .A2(z0[13]), .A3(n13), .Z(y[13]) );
XOR3UD1BWP30P140 U45 ( .A1(z1[14]), .A2(z0[14]), .A3(n14), .Z(y[14]) );
XOR3UD1BWP30P140 U46 ( .A1(z1[15]), .A2(z0[15]), .A3(n15), .Z(y[15]) );
XOR3UD1BWP30P140 U47 ( .A1(z1[16]), .A2(z0[16]), .A3(n16), .Z(y[16]) );
XOR3UD1BWP30P140 U48 ( .A1(z1[17]), .A2(z0[17]), .A3(n17), .Z(y[17]) );
XOR3UD1BWP30P140 U49 ( .A1(z1[18]), .A2(z0[18]), .A3(n18), .Z(y[18]) );
XOR3UD1BWP30P140 U50 ( .A1(z1[19]), .A2(z0[19]), .A3(n19), .Z(y[19]) );
XOR3UD1BWP30P140 U51 ( .A1(z1[20]), .A2(z0[20]), .A3(n20), .Z(y[20]) );
XOR3UD1BWP30P140 U52 ( .A1(z1[21]), .A2(z0[21]), .A3(n21), .Z(y[21]) );
XOR3UD1BWP30P140 U53 ( .A1(z1[22]), .A2(z0[22]), .A3(n22), .Z(y[22]) );
XOR3UD1BWP30P140 U54 ( .A1(z1[23]), .A2(z0[23]), .A3(n23), .Z(y[23]) );
XOR3UD1BWP30P140 U55 ( .A1(z1[24]), .A2(z0[24]), .A3(n24), .Z(y[24]) );
XOR3UD1BWP30P140 U56 ( .A1(z1[25]), .A2(z0[25]), .A3(n25), .Z(y[25]) );
XOR3UD1BWP30P140 U57 ( .A1(z1[26]), .A2(z0[26]), .A3(n26), .Z(y[26]) );
XOR3UD1BWP30P140 U58 ( .A1(z1[27]), .A2(z0[27]), .A3(n27), .Z(y[27]) );
XOR3UD1BWP30P140 U59 ( .A1(z1[28]), .A2(z0[28]), .A3(n28), .Z(y[28]) );
XOR3UD1BWP30P140 U60 ( .A1(z1[29]), .A2(z0[29]), .A3(n29), .Z(y[29]) );
XOR3UD1BWP30P140 U61 ( .A1(z1[30]), .A2(z0[30]), .A3(n30), .Z(y[30]) );
XOR3UD1BWP30P140 U62 ( .A1(z2[31]), .A2(z1[31]), .A3(z0[31]), .Z(y[31]) );
XOR3UD1BWP30P140 U63 ( .A1(z1[32]), .A2(z2[32]), .A3(n0), .Z(y[32]) );
XOR3UD1BWP30P140 U64 ( .A1(z1[33]), .A2(z2[33]), .A3(n1), .Z(y[33]) );
XOR3UD1BWP30P140 U65 ( .A1(z1[34]), .A2(z2[34]), .A3(n2), .Z(y[34]) );
XOR3UD1BWP30P140 U66 ( .A1(z1[35]), .A2(z2[35]), .A3(n3), .Z(y[35]) );
XOR3UD1BWP30P140 U67 ( .A1(z1[36]), .A2(z2[36]), .A3(n4), .Z(y[36]) );
XOR3UD1BWP30P140 U68 ( .A1(z1[37]), .A2(z2[37]), .A3(n5), .Z(y[37]) );
XOR3UD1BWP30P140 U69 ( .A1(z1[38]), .A2(z2[38]), .A3(n6), .Z(y[38]) );
XOR3UD1BWP30P140 U70 ( .A1(z1[39]), .A2(z2[39]), .A3(n7), .Z(y[39]) );
XOR3UD1BWP30P140 U71 ( .A1(z1[40]), .A2(z2[40]), .A3(n8), .Z(y[40]) );
XOR3UD1BWP30P140 U72 ( .A1(z1[41]), .A2(z2[41]), .A3(n9), .Z(y[41]) );
XOR3UD1BWP30P140 U73 ( .A1(z1[42]), .A2(z2[42]), .A3(n10), .Z(y[42]) );
XOR3UD1BWP30P140 U74 ( .A1(z1[43]), .A2(z2[43]), .A3(n11), .Z(y[43]) );
XOR3UD1BWP30P140 U75 ( .A1(z1[44]), .A2(z2[44]), .A3(n12), .Z(y[44]) );
XOR3UD1BWP30P140 U76 ( .A1(z1[45]), .A2(z2[45]), .A3(n13), .Z(y[45]) );
XOR3UD1BWP30P140 U77 ( .A1(z1[46]), .A2(z2[46]), .A3(n14), .Z(y[46]) );
XOR3UD1BWP30P140 U78 ( .A1(z1[47]), .A2(z2[47]), .A3(n15), .Z(y[47]) );
XOR3UD1BWP30P140 U79 ( .A1(z1[48]), .A2(z2[48]), .A3(n16), .Z(y[48]) );
XOR3UD1BWP30P140 U80 ( .A1(z1[49]), .A2(z2[49]), .A3(n17), .Z(y[49]) );
XOR3UD1BWP30P140 U81 ( .A1(z1[50]), .A2(z2[50]), .A3(n18), .Z(y[50]) );
XOR3UD1BWP30P140 U82 ( .A1(z1[51]), .A2(z2[51]), .A3(n19), .Z(y[51]) );
XOR3UD1BWP30P140 U83 ( .A1(z1[52]), .A2(z2[52]), .A3(n20), .Z(y[52]) );
XOR3UD1BWP30P140 U84 ( .A1(z1[53]), .A2(z2[53]), .A3(n21), .Z(y[53]) );
XOR3UD1BWP30P140 U85 ( .A1(z1[54]), .A2(z2[54]), .A3(n22), .Z(y[54]) );
XOR3UD1BWP30P140 U86 ( .A1(z1[55]), .A2(z2[55]), .A3(n23), .Z(y[55]) );
XOR3UD1BWP30P140 U87 ( .A1(z1[56]), .A2(z2[56]), .A3(n24), .Z(y[56]) );
XOR3UD1BWP30P140 U88 ( .A1(z1[57]), .A2(z2[57]), .A3(n25), .Z(y[57]) );
XOR3UD1BWP30P140 U89 ( .A1(z1[58]), .A2(z2[58]), .A3(n26), .Z(y[58]) );
XOR3UD1BWP30P140 U90 ( .A1(z1[59]), .A2(z2[59]), .A3(n27), .Z(y[59]) );
XOR3UD1BWP30P140 U91 ( .A1(z1[60]), .A2(z2[60]), .A3(n28), .Z(y[60]) );
XOR3UD1BWP30P140 U92 ( .A1(z1[61]), .A2(z2[61]), .A3(n29), .Z(y[61]) );
XOR3UD1BWP30P140 U93 ( .A1(z1[62]), .A2(z2[62]), .A3(n30), .Z(y[62]) );

endmodule