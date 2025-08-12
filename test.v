module OKA_128bit
(
   input [127:0] a,
   input [127:0] b,
   output [254:0] y,
   input [21:0] C_g1,
   input rst_n

);
wire [63:0] aa;
wire [63:0] bb;
wire [63:0] al;
wire [63:0] ah;
wire [63:0] bl;
wire [63:0] bh;
wire [126:0] z0;
wire [126:0] z1;
wire [126:0] z2;
assign al[0] = a[0];
assign al[1] = a[2];
assign al[2] = a[4];
assign al[3] = a[6];
assign al[4] = a[8];
assign al[5] = a[10];
assign al[6] = a[12];
assign al[7] = a[14];
assign al[8] = a[16];
assign al[9] = a[18];
assign al[10] = a[20];
assign al[11] = a[22];
assign al[12] = a[24];
assign al[13] = a[26];
assign al[14] = a[28];
assign al[15] = a[30];
assign al[16] = a[32];
assign al[17] = a[34];
assign al[18] = a[36];
assign al[19] = a[38];
assign al[20] = a[40];
assign al[21] = a[42];
assign al[22] = a[44];
assign al[23] = a[46];
assign al[24] = a[48];
assign al[25] = a[50];
assign al[26] = a[52];
assign al[27] = a[54];
assign al[28] = a[56];
assign al[29] = a[58];
assign al[30] = a[60];
assign al[31] = a[62];
assign al[32] = a[64];
assign al[33] = a[66];
assign al[34] = a[68];
assign al[35] = a[70];
assign al[36] = a[72];
assign al[37] = a[74];
assign al[38] = a[76];
assign al[39] = a[78];
assign al[40] = a[80];
assign al[41] = a[82];
assign al[42] = a[84];
assign al[43] = a[86];
assign al[44] = a[88];
assign al[45] = a[90];
assign al[46] = a[92];
assign al[47] = a[94];
assign al[48] = a[96];
assign al[49] = a[98];
assign al[50] = a[100];
assign al[51] = a[102];
assign al[52] = a[104];
assign al[53] = a[106];
assign al[54] = a[108];
assign al[55] = a[110];
assign al[56] = a[112];
assign al[57] = a[114];
assign al[58] = a[116];
assign al[59] = a[118];
assign al[60] = a[120];
assign al[61] = a[122];
assign al[62] = a[124];
assign al[63] = a[126];
assign ah[0] = a[1];
assign ah[1] = a[3];
assign ah[2] = a[5];
assign ah[3] = a[7];
assign ah[4] = a[9];
assign ah[5] = a[11];
assign ah[6] = a[13];
assign ah[7] = a[15];
assign ah[8] = a[17];
assign ah[9] = a[19];
assign ah[10] = a[21];
assign ah[11] = a[23];
assign ah[12] = a[25];
assign ah[13] = a[27];
assign ah[14] = a[29];
assign ah[15] = a[31];
assign ah[16] = a[33];
assign ah[17] = a[35];
assign ah[18] = a[37];
assign ah[19] = a[39];
assign ah[20] = a[41];
assign ah[21] = a[43];
assign ah[22] = a[45];
assign ah[23] = a[47];
assign ah[24] = a[49];
assign ah[25] = a[51];
assign ah[26] = a[53];
assign ah[27] = a[55];
assign ah[28] = a[57];
assign ah[29] = a[59];
assign ah[30] = a[61];
assign ah[31] = a[63];
assign ah[32] = a[65];
assign ah[33] = a[67];
assign ah[34] = a[69];
assign ah[35] = a[71];
assign ah[36] = a[73];
assign ah[37] = a[75];
assign ah[38] = a[77];
assign ah[39] = a[79];
assign ah[40] = a[81];
assign ah[41] = a[83];
assign ah[42] = a[85];
assign ah[43] = a[87];
assign ah[44] = a[89];
assign ah[45] = a[91];
assign ah[46] = a[93];
assign ah[47] = a[95];
assign ah[48] = a[97];
assign ah[49] = a[99];
assign ah[50] = a[101];
assign ah[51] = a[103];
assign ah[52] = a[105];
assign ah[53] = a[107];
assign ah[54] = a[109];
assign ah[55] = a[111];
assign ah[56] = a[113];
assign ah[57] = a[115];
assign ah[58] = a[117];
assign ah[59] = a[119];
assign ah[60] = a[121];
assign ah[61] = a[123];
assign ah[62] = a[125];
assign ah[63] = a[127];
assign bl[0] = b[0];
assign bl[1] = b[2];
assign bl[2] = b[4];
assign bl[3] = b[6];
assign bl[4] = b[8];
assign bl[5] = b[10];
assign bl[6] = b[12];
assign bl[7] = b[14];
assign bl[8] = b[16];
assign bl[9] = b[18];
assign bl[10] = b[20];
assign bl[11] = b[22];
assign bl[12] = b[24];
assign bl[13] = b[26];
assign bl[14] = b[28];
assign bl[15] = b[30];
assign bl[16] = b[32];
assign bl[17] = b[34];
assign bl[18] = b[36];
assign bl[19] = b[38];
assign bl[20] = b[40];
assign bl[21] = b[42];
assign bl[22] = b[44];
assign bl[23] = b[46];
assign bl[24] = b[48];
assign bl[25] = b[50];
assign bl[26] = b[52];
assign bl[27] = b[54];
assign bl[28] = b[56];
assign bl[29] = b[58];
assign bl[30] = b[60];
assign bl[31] = b[62];
assign bl[32] = b[64];
assign bl[33] = b[66];
assign bl[34] = b[68];
assign bl[35] = b[70];
assign bl[36] = b[72];
assign bl[37] = b[74];
assign bl[38] = b[76];
assign bl[39] = b[78];
assign bl[40] = b[80];
assign bl[41] = b[82];
assign bl[42] = b[84];
assign bl[43] = b[86];
assign bl[44] = b[88];
assign bl[45] = b[90];
assign bl[46] = b[92];
assign bl[47] = b[94];
assign bl[48] = b[96];
assign bl[49] = b[98];
assign bl[50] = b[100];
assign bl[51] = b[102];
assign bl[52] = b[104];
assign bl[53] = b[106];
assign bl[54] = b[108];
assign bl[55] = b[110];
assign bl[56] = b[112];
assign bl[57] = b[114];
assign bl[58] = b[116];
assign bl[59] = b[118];
assign bl[60] = b[120];
assign bl[61] = b[122];
assign bl[62] = b[124];
assign bl[63] = b[126];
assign bh[0] = b[1];
assign bh[1] = b[3];
assign bh[2] = b[5];
assign bh[3] = b[7];
assign bh[4] = b[9];
assign bh[5] = b[11];
assign bh[6] = b[13];
assign bh[7] = b[15];
assign bh[8] = b[17];
assign bh[9] = b[19];
assign bh[10] = b[21];
assign bh[11] = b[23];
assign bh[12] = b[25];
assign bh[13] = b[27];
assign bh[14] = b[29];
assign bh[15] = b[31];
assign bh[16] = b[33];
assign bh[17] = b[35];
assign bh[18] = b[37];
assign bh[19] = b[39];
assign bh[20] = b[41];
assign bh[21] = b[43];
assign bh[22] = b[45];
assign bh[23] = b[47];
assign bh[24] = b[49];
assign bh[25] = b[51];
assign bh[26] = b[53];
assign bh[27] = b[55];
assign bh[28] = b[57];
assign bh[29] = b[59];
assign bh[30] = b[61];
assign bh[31] = b[63];
assign bh[32] = b[65];
assign bh[33] = b[67];
assign bh[34] = b[69];
assign bh[35] = b[71];
assign bh[36] = b[73];
assign bh[37] = b[75];
assign bh[38] = b[77];
assign bh[39] = b[79];
assign bh[40] = b[81];
assign bh[41] = b[83];
assign bh[42] = b[85];
assign bh[43] = b[87];
assign bh[44] = b[89];
assign bh[45] = b[91];
assign bh[46] = b[93];
assign bh[47] = b[95];
assign bh[48] = b[97];
assign bh[49] = b[99];
assign bh[50] = b[101];
assign bh[51] = b[103];
assign bh[52] = b[105];
assign bh[53] = b[107];
assign bh[54] = b[109];
assign bh[55] = b[111];
assign bh[56] = b[113];
assign bh[57] = b[115];
assign bh[58] = b[117];
assign bh[59] = b[119];
assign bh[60] = b[121];
assign bh[61] = b[123];
assign bh[62] = b[125];
assign bh[63] = b[127];
s_128bit s128_u
(
   .a(a),
   .b(b),
   .aa(aa),
   .bb(bb)
);
OKA_64bit mul64_0
(
.rst_n(rst_n),
.C_g1(C_g1),
.a(al),
.b(bl),
.y(z0)
);
OKA_64bit mul64_1
(
.rst_n(rst_n),
.C_g1(C_g1),
.a(aa),
.b(bb),
.y(z1)
);
OKA_64bit mul64_2
(
.rst_n(rst_n),
.C_g1(C_g1),
.a(ah),
.b(bh),
.y(z2)
);
os_128bit os128_u
(
.rst_n(rst_n),
.C_g1(C_g1),
   .z0(z0),
   .z1(z1),
   .z2(z2),
   .y(y)
);
endmodule
module s_128bit
(
   input [127:0] a,
   input [127:0] b,
   output [63:0] aa,
   output [63:0] bb
);
XOR2UD1BWP30P140 U0 ( .A1(a[0]), .A2(a[1]), .Z(aa[0]) );
XOR2UD1BWP30P140 U1 ( .A1(a[2]), .A2(a[3]), .Z(aa[1]) );
XOR2UD1BWP30P140 U2 ( .A1(a[4]), .A2(a[5]), .Z(aa[2]) );
XOR2UD1BWP30P140 U3 ( .A1(a[6]), .A2(a[7]), .Z(aa[3]) );
XOR2UD1BWP30P140 U4 ( .A1(a[8]), .A2(a[9]), .Z(aa[4]) );
XOR2UD1BWP30P140 U5 ( .A1(a[10]), .A2(a[11]), .Z(aa[5]) );
XOR2UD1BWP30P140 U6 ( .A1(a[12]), .A2(a[13]), .Z(aa[6]) );
XOR2UD1BWP30P140 U7 ( .A1(a[14]), .A2(a[15]), .Z(aa[7]) );
XOR2UD1BWP30P140 U8 ( .A1(a[16]), .A2(a[17]), .Z(aa[8]) );
XOR2UD1BWP30P140 U9 ( .A1(a[18]), .A2(a[19]), .Z(aa[9]) );
XOR2UD1BWP30P140 U10 ( .A1(a[20]), .A2(a[21]), .Z(aa[10]) );
XOR2UD1BWP30P140 U11 ( .A1(a[22]), .A2(a[23]), .Z(aa[11]) );
XOR2UD1BWP30P140 U12 ( .A1(a[24]), .A2(a[25]), .Z(aa[12]) );
XOR2UD1BWP30P140 U13 ( .A1(a[26]), .A2(a[27]), .Z(aa[13]) );
XOR2UD1BWP30P140 U14 ( .A1(a[28]), .A2(a[29]), .Z(aa[14]) );
XOR2UD1BWP30P140 U15 ( .A1(a[30]), .A2(a[31]), .Z(aa[15]) );
XOR2UD1BWP30P140 U16 ( .A1(a[32]), .A2(a[33]), .Z(aa[16]) );
XOR2UD1BWP30P140 U17 ( .A1(a[34]), .A2(a[35]), .Z(aa[17]) );
XOR2UD1BWP30P140 U18 ( .A1(a[36]), .A2(a[37]), .Z(aa[18]) );
XOR2UD1BWP30P140 U19 ( .A1(a[38]), .A2(a[39]), .Z(aa[19]) );
XOR2UD1BWP30P140 U20 ( .A1(a[40]), .A2(a[41]), .Z(aa[20]) );
XOR2UD1BWP30P140 U21 ( .A1(a[42]), .A2(a[43]), .Z(aa[21]) );
XOR2UD1BWP30P140 U22 ( .A1(a[44]), .A2(a[45]), .Z(aa[22]) );
XOR2UD1BWP30P140 U23 ( .A1(a[46]), .A2(a[47]), .Z(aa[23]) );
XOR2UD1BWP30P140 U24 ( .A1(a[48]), .A2(a[49]), .Z(aa[24]) );
XOR2UD1BWP30P140 U25 ( .A1(a[50]), .A2(a[51]), .Z(aa[25]) );
XOR2UD1BWP30P140 U26 ( .A1(a[52]), .A2(a[53]), .Z(aa[26]) );
XOR2UD1BWP30P140 U27 ( .A1(a[54]), .A2(a[55]), .Z(aa[27]) );
XOR2UD1BWP30P140 U28 ( .A1(a[56]), .A2(a[57]), .Z(aa[28]) );
XOR2UD1BWP30P140 U29 ( .A1(a[58]), .A2(a[59]), .Z(aa[29]) );
XOR2UD1BWP30P140 U30 ( .A1(a[60]), .A2(a[61]), .Z(aa[30]) );
XOR2UD1BWP30P140 U31 ( .A1(a[62]), .A2(a[63]), .Z(aa[31]) );
XOR2UD1BWP30P140 U32 ( .A1(a[64]), .A2(a[65]), .Z(aa[32]) );
XOR2UD1BWP30P140 U33 ( .A1(a[66]), .A2(a[67]), .Z(aa[33]) );
XOR2UD1BWP30P140 U34 ( .A1(a[68]), .A2(a[69]), .Z(aa[34]) );
XOR2UD1BWP30P140 U35 ( .A1(a[70]), .A2(a[71]), .Z(aa[35]) );
XOR2UD1BWP30P140 U36 ( .A1(a[72]), .A2(a[73]), .Z(aa[36]) );
XOR2UD1BWP30P140 U37 ( .A1(a[74]), .A2(a[75]), .Z(aa[37]) );
XOR2UD1BWP30P140 U38 ( .A1(a[76]), .A2(a[77]), .Z(aa[38]) );
XOR2UD1BWP30P140 U39 ( .A1(a[78]), .A2(a[79]), .Z(aa[39]) );
XOR2UD1BWP30P140 U40 ( .A1(a[80]), .A2(a[81]), .Z(aa[40]) );
XOR2UD1BWP30P140 U41 ( .A1(a[82]), .A2(a[83]), .Z(aa[41]) );
XOR2UD1BWP30P140 U42 ( .A1(a[84]), .A2(a[85]), .Z(aa[42]) );
XOR2UD1BWP30P140 U43 ( .A1(a[86]), .A2(a[87]), .Z(aa[43]) );
XOR2UD1BWP30P140 U44 ( .A1(a[88]), .A2(a[89]), .Z(aa[44]) );
XOR2UD1BWP30P140 U45 ( .A1(a[90]), .A2(a[91]), .Z(aa[45]) );
XOR2UD1BWP30P140 U46 ( .A1(a[92]), .A2(a[93]), .Z(aa[46]) );
XOR2UD1BWP30P140 U47 ( .A1(a[94]), .A2(a[95]), .Z(aa[47]) );
XOR2UD1BWP30P140 U48 ( .A1(a[96]), .A2(a[97]), .Z(aa[48]) );
XOR2UD1BWP30P140 U49 ( .A1(a[98]), .A2(a[99]), .Z(aa[49]) );
XOR2UD1BWP30P140 U50 ( .A1(a[100]), .A2(a[101]), .Z(aa[50]) );
XOR2UD1BWP30P140 U51 ( .A1(a[102]), .A2(a[103]), .Z(aa[51]) );
XOR2UD1BWP30P140 U52 ( .A1(a[104]), .A2(a[105]), .Z(aa[52]) );
XOR2UD1BWP30P140 U53 ( .A1(a[106]), .A2(a[107]), .Z(aa[53]) );
XOR2UD1BWP30P140 U54 ( .A1(a[108]), .A2(a[109]), .Z(aa[54]) );
XOR2UD1BWP30P140 U55 ( .A1(a[110]), .A2(a[111]), .Z(aa[55]) );
XOR2UD1BWP30P140 U56 ( .A1(a[112]), .A2(a[113]), .Z(aa[56]) );
XOR2UD1BWP30P140 U57 ( .A1(a[114]), .A2(a[115]), .Z(aa[57]) );
XOR2UD1BWP30P140 U58 ( .A1(a[116]), .A2(a[117]), .Z(aa[58]) );
XOR2UD1BWP30P140 U59 ( .A1(a[118]), .A2(a[119]), .Z(aa[59]) );
XOR2UD1BWP30P140 U60 ( .A1(a[120]), .A2(a[121]), .Z(aa[60]) );
XOR2UD1BWP30P140 U61 ( .A1(a[122]), .A2(a[123]), .Z(aa[61]) );
XOR2UD1BWP30P140 U62 ( .A1(a[124]), .A2(a[125]), .Z(aa[62]) );
XOR2UD1BWP30P140 U63 ( .A1(a[126]), .A2(a[127]), .Z(aa[63]) );
XOR2UD1BWP30P140 U64 ( .A1(b[0]), .A2(b[1]), .Z(bb[0]) );
XOR2UD1BWP30P140 U65 ( .A1(b[2]), .A2(b[3]), .Z(bb[1]) );
XOR2UD1BWP30P140 U66 ( .A1(b[4]), .A2(b[5]), .Z(bb[2]) );
XOR2UD1BWP30P140 U67 ( .A1(b[6]), .A2(b[7]), .Z(bb[3]) );
XOR2UD1BWP30P140 U68 ( .A1(b[8]), .A2(b[9]), .Z(bb[4]) );
XOR2UD1BWP30P140 U69 ( .A1(b[10]), .A2(b[11]), .Z(bb[5]) );
XOR2UD1BWP30P140 U70 ( .A1(b[12]), .A2(b[13]), .Z(bb[6]) );
XOR2UD1BWP30P140 U71 ( .A1(b[14]), .A2(b[15]), .Z(bb[7]) );
XOR2UD1BWP30P140 U72 ( .A1(b[16]), .A2(b[17]), .Z(bb[8]) );
XOR2UD1BWP30P140 U73 ( .A1(b[18]), .A2(b[19]), .Z(bb[9]) );
XOR2UD1BWP30P140 U74 ( .A1(b[20]), .A2(b[21]), .Z(bb[10]) );
XOR2UD1BWP30P140 U75 ( .A1(b[22]), .A2(b[23]), .Z(bb[11]) );
XOR2UD1BWP30P140 U76 ( .A1(b[24]), .A2(b[25]), .Z(bb[12]) );
XOR2UD1BWP30P140 U77 ( .A1(b[26]), .A2(b[27]), .Z(bb[13]) );
XOR2UD1BWP30P140 U78 ( .A1(b[28]), .A2(b[29]), .Z(bb[14]) );
XOR2UD1BWP30P140 U79 ( .A1(b[30]), .A2(b[31]), .Z(bb[15]) );
XOR2UD1BWP30P140 U80 ( .A1(b[32]), .A2(b[33]), .Z(bb[16]) );
XOR2UD1BWP30P140 U81 ( .A1(b[34]), .A2(b[35]), .Z(bb[17]) );
XOR2UD1BWP30P140 U82 ( .A1(b[36]), .A2(b[37]), .Z(bb[18]) );
XOR2UD1BWP30P140 U83 ( .A1(b[38]), .A2(b[39]), .Z(bb[19]) );
XOR2UD1BWP30P140 U84 ( .A1(b[40]), .A2(b[41]), .Z(bb[20]) );
XOR2UD1BWP30P140 U85 ( .A1(b[42]), .A2(b[43]), .Z(bb[21]) );
XOR2UD1BWP30P140 U86 ( .A1(b[44]), .A2(b[45]), .Z(bb[22]) );
XOR2UD1BWP30P140 U87 ( .A1(b[46]), .A2(b[47]), .Z(bb[23]) );
XOR2UD1BWP30P140 U88 ( .A1(b[48]), .A2(b[49]), .Z(bb[24]) );
XOR2UD1BWP30P140 U89 ( .A1(b[50]), .A2(b[51]), .Z(bb[25]) );
XOR2UD1BWP30P140 U90 ( .A1(b[52]), .A2(b[53]), .Z(bb[26]) );
XOR2UD1BWP30P140 U91 ( .A1(b[54]), .A2(b[55]), .Z(bb[27]) );
XOR2UD1BWP30P140 U92 ( .A1(b[56]), .A2(b[57]), .Z(bb[28]) );
XOR2UD1BWP30P140 U93 ( .A1(b[58]), .A2(b[59]), .Z(bb[29]) );
XOR2UD1BWP30P140 U94 ( .A1(b[60]), .A2(b[61]), .Z(bb[30]) );
XOR2UD1BWP30P140 U95 ( .A1(b[62]), .A2(b[63]), .Z(bb[31]) );
XOR2UD1BWP30P140 U96 ( .A1(b[64]), .A2(b[65]), .Z(bb[32]) );
XOR2UD1BWP30P140 U97 ( .A1(b[66]), .A2(b[67]), .Z(bb[33]) );
XOR2UD1BWP30P140 U98 ( .A1(b[68]), .A2(b[69]), .Z(bb[34]) );
XOR2UD1BWP30P140 U99 ( .A1(b[70]), .A2(b[71]), .Z(bb[35]) );
XOR2UD1BWP30P140 U100 ( .A1(b[72]), .A2(b[73]), .Z(bb[36]) );
XOR2UD1BWP30P140 U101 ( .A1(b[74]), .A2(b[75]), .Z(bb[37]) );
XOR2UD1BWP30P140 U102 ( .A1(b[76]), .A2(b[77]), .Z(bb[38]) );
XOR2UD1BWP30P140 U103 ( .A1(b[78]), .A2(b[79]), .Z(bb[39]) );
XOR2UD1BWP30P140 U104 ( .A1(b[80]), .A2(b[81]), .Z(bb[40]) );
XOR2UD1BWP30P140 U105 ( .A1(b[82]), .A2(b[83]), .Z(bb[41]) );
XOR2UD1BWP30P140 U106 ( .A1(b[84]), .A2(b[85]), .Z(bb[42]) );
XOR2UD1BWP30P140 U107 ( .A1(b[86]), .A2(b[87]), .Z(bb[43]) );
XOR2UD1BWP30P140 U108 ( .A1(b[88]), .A2(b[89]), .Z(bb[44]) );
XOR2UD1BWP30P140 U109 ( .A1(b[90]), .A2(b[91]), .Z(bb[45]) );
XOR2UD1BWP30P140 U110 ( .A1(b[92]), .A2(b[93]), .Z(bb[46]) );
XOR2UD1BWP30P140 U111 ( .A1(b[94]), .A2(b[95]), .Z(bb[47]) );
XOR2UD1BWP30P140 U112 ( .A1(b[96]), .A2(b[97]), .Z(bb[48]) );
XOR2UD1BWP30P140 U113 ( .A1(b[98]), .A2(b[99]), .Z(bb[49]) );
XOR2UD1BWP30P140 U114 ( .A1(b[100]), .A2(b[101]), .Z(bb[50]) );
XOR2UD1BWP30P140 U115 ( .A1(b[102]), .A2(b[103]), .Z(bb[51]) );
XOR2UD1BWP30P140 U116 ( .A1(b[104]), .A2(b[105]), .Z(bb[52]) );
XOR2UD1BWP30P140 U117 ( .A1(b[106]), .A2(b[107]), .Z(bb[53]) );
XOR2UD1BWP30P140 U118 ( .A1(b[108]), .A2(b[109]), .Z(bb[54]) );
XOR2UD1BWP30P140 U119 ( .A1(b[110]), .A2(b[111]), .Z(bb[55]) );
XOR2UD1BWP30P140 U120 ( .A1(b[112]), .A2(b[113]), .Z(bb[56]) );
XOR2UD1BWP30P140 U121 ( .A1(b[114]), .A2(b[115]), .Z(bb[57]) );
XOR2UD1BWP30P140 U122 ( .A1(b[116]), .A2(b[117]), .Z(bb[58]) );
XOR2UD1BWP30P140 U123 ( .A1(b[118]), .A2(b[119]), .Z(bb[59]) );
XOR2UD1BWP30P140 U124 ( .A1(b[120]), .A2(b[121]), .Z(bb[60]) );
XOR2UD1BWP30P140 U125 ( .A1(b[122]), .A2(b[123]), .Z(bb[61]) );
XOR2UD1BWP30P140 U126 ( .A1(b[124]), .A2(b[125]), .Z(bb[62]) );
XOR2UD1BWP30P140 U127 ( .A1(b[126]), .A2(b[127]), .Z(bb[63]) );
endmodule

module os_128bit
(
   input [126:0] z0,
   input [126:0] z1,
   input [126:0] z2,
   output [254:0] y,
   input [21:0] C_g1,
   input rst_n
);
wire [126:0] o1;
XOR3UD1BWP30P140 U0 ( .A1(z0[0]), .A2(z1[0]), .A3(z2[0]), .Z(o1[0]) );
XOR3UD1BWP30P140 U1 ( .A1(z0[1]), .A2(z1[1]), .A3(z2[1]), .Z(o1[1]) );
XOR3UD1BWP30P140 U2 ( .A1(z0[2]), .A2(z1[2]), .A3(z2[2]), .Z(o1[2]) );
XOR3UD1BWP30P140 U3 ( .A1(z0[3]), .A2(z1[3]), .A3(z2[3]), .Z(o1[3]) );
XOR3UD1BWP30P140 U4 ( .A1(z0[4]), .A2(z1[4]), .A3(z2[4]), .Z(o1[4]) );
XOR3UD1BWP30P140 U5 ( .A1(z0[5]), .A2(z1[5]), .A3(z2[5]), .Z(o1[5]) );
XOR3UD1BWP30P140 U6 ( .A1(z0[6]), .A2(z1[6]), .A3(z2[6]), .Z(o1[6]) );
XOR3UD1BWP30P140 U7 ( .A1(z0[7]), .A2(z1[7]), .A3(z2[7]), .Z(o1[7]) );
XOR3UD1BWP30P140 U8 ( .A1(z0[8]), .A2(z1[8]), .A3(z2[8]), .Z(o1[8]) );
XOR3UD1BWP30P140 U9 ( .A1(z0[9]), .A2(z1[9]), .A3(z2[9]), .Z(o1[9]) );
XOR3UD1BWP30P140 U10 ( .A1(z0[10]), .A2(z1[10]), .A3(z2[10]), .Z(o1[10]) );
XOR3UD1BWP30P140 U11 ( .A1(z0[11]), .A2(z1[11]), .A3(z2[11]), .Z(o1[11]) );
XOR3UD1BWP30P140 U12 ( .A1(z0[12]), .A2(z1[12]), .A3(z2[12]), .Z(o1[12]) );
XOR3UD1BWP30P140 U13 ( .A1(z0[13]), .A2(z1[13]), .A3(z2[13]), .Z(o1[13]) );
XOR3UD1BWP30P140 U14 ( .A1(z0[14]), .A2(z1[14]), .A3(z2[14]), .Z(o1[14]) );
XOR3UD1BWP30P140 U15 ( .A1(z0[15]), .A2(z1[15]), .A3(z2[15]), .Z(o1[15]) );
XOR3UD1BWP30P140 U16 ( .A1(z0[16]), .A2(z1[16]), .A3(z2[16]), .Z(o1[16]) );
XOR3UD1BWP30P140 U17 ( .A1(z0[17]), .A2(z1[17]), .A3(z2[17]), .Z(o1[17]) );
XOR3UD1BWP30P140 U18 ( .A1(z0[18]), .A2(z1[18]), .A3(z2[18]), .Z(o1[18]) );
XOR3UD1BWP30P140 U19 ( .A1(z0[19]), .A2(z1[19]), .A3(z2[19]), .Z(o1[19]) );
XOR3UD1BWP30P140 U20 ( .A1(z0[20]), .A2(z1[20]), .A3(z2[20]), .Z(o1[20]) );
XOR3UD1BWP30P140 U21 ( .A1(z0[21]), .A2(z1[21]), .A3(z2[21]), .Z(o1[21]) );
XOR3UD1BWP30P140 U22 ( .A1(z0[22]), .A2(z1[22]), .A3(z2[22]), .Z(o1[22]) );
XOR3UD1BWP30P140 U23 ( .A1(z0[23]), .A2(z1[23]), .A3(z2[23]), .Z(o1[23]) );
XOR3UD1BWP30P140 U24 ( .A1(z0[24]), .A2(z1[24]), .A3(z2[24]), .Z(o1[24]) );
XOR3UD1BWP30P140 U25 ( .A1(z0[25]), .A2(z1[25]), .A3(z2[25]), .Z(o1[25]) );
XOR3UD1BWP30P140 U26 ( .A1(z0[26]), .A2(z1[26]), .A3(z2[26]), .Z(o1[26]) );
XOR3UD1BWP30P140 U27 ( .A1(z0[27]), .A2(z1[27]), .A3(z2[27]), .Z(o1[27]) );
XOR3UD1BWP30P140 U28 ( .A1(z0[28]), .A2(z1[28]), .A3(z2[28]), .Z(o1[28]) );
XOR3UD1BWP30P140 U29 ( .A1(z0[29]), .A2(z1[29]), .A3(z2[29]), .Z(o1[29]) );
XOR3UD1BWP30P140 U30 ( .A1(z0[30]), .A2(z1[30]), .A3(z2[30]), .Z(o1[30]) );
XOR3UD1BWP30P140 U31 ( .A1(z0[31]), .A2(z1[31]), .A3(z2[31]), .Z(o1[31]) );
XOR3UD1BWP30P140 U32 ( .A1(z0[32]), .A2(z1[32]), .A3(z2[32]), .Z(o1[32]) );
XOR3UD1BWP30P140 U33 ( .A1(z0[33]), .A2(z1[33]), .A3(z2[33]), .Z(o1[33]) );
XOR3UD1BWP30P140 U34 ( .A1(z0[34]), .A2(z1[34]), .A3(z2[34]), .Z(o1[34]) );
XOR3UD1BWP30P140 U35 ( .A1(z0[35]), .A2(z1[35]), .A3(z2[35]), .Z(o1[35]) );
XOR3UD1BWP30P140 U36 ( .A1(z0[36]), .A2(z1[36]), .A3(z2[36]), .Z(o1[36]) );
XOR3UD1BWP30P140 U37 ( .A1(z0[37]), .A2(z1[37]), .A3(z2[37]), .Z(o1[37]) );
XOR3UD1BWP30P140 U38 ( .A1(z0[38]), .A2(z1[38]), .A3(z2[38]), .Z(o1[38]) );
XOR3UD1BWP30P140 U39 ( .A1(z0[39]), .A2(z1[39]), .A3(z2[39]), .Z(o1[39]) );
XOR3UD1BWP30P140 U40 ( .A1(z0[40]), .A2(z1[40]), .A3(z2[40]), .Z(o1[40]) );
XOR3UD1BWP30P140 U41 ( .A1(z0[41]), .A2(z1[41]), .A3(z2[41]), .Z(o1[41]) );
XOR3UD1BWP30P140 U42 ( .A1(z0[42]), .A2(z1[42]), .A3(z2[42]), .Z(o1[42]) );
XOR3UD1BWP30P140 U43 ( .A1(z0[43]), .A2(z1[43]), .A3(z2[43]), .Z(o1[43]) );
XOR3UD1BWP30P140 U44 ( .A1(z0[44]), .A2(z1[44]), .A3(z2[44]), .Z(o1[44]) );
XOR3UD1BWP30P140 U45 ( .A1(z0[45]), .A2(z1[45]), .A3(z2[45]), .Z(o1[45]) );
XOR3UD1BWP30P140 U46 ( .A1(z0[46]), .A2(z1[46]), .A3(z2[46]), .Z(o1[46]) );
XOR3UD1BWP30P140 U47 ( .A1(z0[47]), .A2(z1[47]), .A3(z2[47]), .Z(o1[47]) );
XOR3UD1BWP30P140 U48 ( .A1(z0[48]), .A2(z1[48]), .A3(z2[48]), .Z(o1[48]) );
XOR3UD1BWP30P140 U49 ( .A1(z0[49]), .A2(z1[49]), .A3(z2[49]), .Z(o1[49]) );
XOR3UD1BWP30P140 U50 ( .A1(z0[50]), .A2(z1[50]), .A3(z2[50]), .Z(o1[50]) );
XOR3UD1BWP30P140 U51 ( .A1(z0[51]), .A2(z1[51]), .A3(z2[51]), .Z(o1[51]) );
XOR3UD1BWP30P140 U52 ( .A1(z0[52]), .A2(z1[52]), .A3(z2[52]), .Z(o1[52]) );
XOR3UD1BWP30P140 U53 ( .A1(z0[53]), .A2(z1[53]), .A3(z2[53]), .Z(o1[53]) );
XOR3UD1BWP30P140 U54 ( .A1(z0[54]), .A2(z1[54]), .A3(z2[54]), .Z(o1[54]) );
XOR3UD1BWP30P140 U55 ( .A1(z0[55]), .A2(z1[55]), .A3(z2[55]), .Z(o1[55]) );
XOR3UD1BWP30P140 U56 ( .A1(z0[56]), .A2(z1[56]), .A3(z2[56]), .Z(o1[56]) );
XOR3UD1BWP30P140 U57 ( .A1(z0[57]), .A2(z1[57]), .A3(z2[57]), .Z(o1[57]) );
XOR3UD1BWP30P140 U58 ( .A1(z0[58]), .A2(z1[58]), .A3(z2[58]), .Z(o1[58]) );
XOR3UD1BWP30P140 U59 ( .A1(z0[59]), .A2(z1[59]), .A3(z2[59]), .Z(o1[59]) );
XOR3UD1BWP30P140 U60 ( .A1(z0[60]), .A2(z1[60]), .A3(z2[60]), .Z(o1[60]) );
XOR3UD1BWP30P140 U61 ( .A1(z0[61]), .A2(z1[61]), .A3(z2[61]), .Z(o1[61]) );
XOR3UD1BWP30P140 U62 ( .A1(z0[62]), .A2(z1[62]), .A3(z2[62]), .Z(o1[62]) );
XOR3UD1BWP30P140 U63 ( .A1(z0[63]), .A2(z1[63]), .A3(z2[63]), .Z(o1[63]) );
XOR3UD1BWP30P140 U64 ( .A1(z0[64]), .A2(z1[64]), .A3(z2[64]), .Z(o1[64]) );
XOR3UD1BWP30P140 U65 ( .A1(z0[65]), .A2(z1[65]), .A3(z2[65]), .Z(o1[65]) );
XOR3UD1BWP30P140 U66 ( .A1(z0[66]), .A2(z1[66]), .A3(z2[66]), .Z(o1[66]) );
XOR3UD1BWP30P140 U67 ( .A1(z0[67]), .A2(z1[67]), .A3(z2[67]), .Z(o1[67]) );
XOR3UD1BWP30P140 U68 ( .A1(z0[68]), .A2(z1[68]), .A3(z2[68]), .Z(o1[68]) );
XOR3UD1BWP30P140 U69 ( .A1(z0[69]), .A2(z1[69]), .A3(z2[69]), .Z(o1[69]) );
XOR3UD1BWP30P140 U70 ( .A1(z0[70]), .A2(z1[70]), .A3(z2[70]), .Z(o1[70]) );
XOR3UD1BWP30P140 U71 ( .A1(z0[71]), .A2(z1[71]), .A3(z2[71]), .Z(o1[71]) );
XOR3UD1BWP30P140 U72 ( .A1(z0[72]), .A2(z1[72]), .A3(z2[72]), .Z(o1[72]) );
XOR3UD1BWP30P140 U73 ( .A1(z0[73]), .A2(z1[73]), .A3(z2[73]), .Z(o1[73]) );
XOR3UD1BWP30P140 U74 ( .A1(z0[74]), .A2(z1[74]), .A3(z2[74]), .Z(o1[74]) );
XOR3UD1BWP30P140 U75 ( .A1(z0[75]), .A2(z1[75]), .A3(z2[75]), .Z(o1[75]) );
XOR3UD1BWP30P140 U76 ( .A1(z0[76]), .A2(z1[76]), .A3(z2[76]), .Z(o1[76]) );
XOR3UD1BWP30P140 U77 ( .A1(z0[77]), .A2(z1[77]), .A3(z2[77]), .Z(o1[77]) );
XOR3UD1BWP30P140 U78 ( .A1(z0[78]), .A2(z1[78]), .A3(z2[78]), .Z(o1[78]) );
XOR3UD1BWP30P140 U79 ( .A1(z0[79]), .A2(z1[79]), .A3(z2[79]), .Z(o1[79]) );
XOR3UD1BWP30P140 U80 ( .A1(z0[80]), .A2(z1[80]), .A3(z2[80]), .Z(o1[80]) );
XOR3UD1BWP30P140 U81 ( .A1(z0[81]), .A2(z1[81]), .A3(z2[81]), .Z(o1[81]) );
XOR3UD1BWP30P140 U82 ( .A1(z0[82]), .A2(z1[82]), .A3(z2[82]), .Z(o1[82]) );
XOR3UD1BWP30P140 U83 ( .A1(z0[83]), .A2(z1[83]), .A3(z2[83]), .Z(o1[83]) );
XOR3UD1BWP30P140 U84 ( .A1(z0[84]), .A2(z1[84]), .A3(z2[84]), .Z(o1[84]) );
XOR3UD1BWP30P140 U85 ( .A1(z0[85]), .A2(z1[85]), .A3(z2[85]), .Z(o1[85]) );
XOR3UD1BWP30P140 U86 ( .A1(z0[86]), .A2(z1[86]), .A3(z2[86]), .Z(o1[86]) );
XOR3UD1BWP30P140 U87 ( .A1(z0[87]), .A2(z1[87]), .A3(z2[87]), .Z(o1[87]) );
XOR3UD1BWP30P140 U88 ( .A1(z0[88]), .A2(z1[88]), .A3(z2[88]), .Z(o1[88]) );
XOR3UD1BWP30P140 U89 ( .A1(z0[89]), .A2(z1[89]), .A3(z2[89]), .Z(o1[89]) );
XOR3UD1BWP30P140 U90 ( .A1(z0[90]), .A2(z1[90]), .A3(z2[90]), .Z(o1[90]) );
XOR3UD1BWP30P140 U91 ( .A1(z0[91]), .A2(z1[91]), .A3(z2[91]), .Z(o1[91]) );
XOR3UD1BWP30P140 U92 ( .A1(z0[92]), .A2(z1[92]), .A3(z2[92]), .Z(o1[92]) );
XOR3UD1BWP30P140 U93 ( .A1(z0[93]), .A2(z1[93]), .A3(z2[93]), .Z(o1[93]) );
XOR3UD1BWP30P140 U94 ( .A1(z0[94]), .A2(z1[94]), .A3(z2[94]), .Z(o1[94]) );
XOR3UD1BWP30P140 U95 ( .A1(z0[95]), .A2(z1[95]), .A3(z2[95]), .Z(o1[95]) );
XOR3UD1BWP30P140 U96 ( .A1(z0[96]), .A2(z1[96]), .A3(z2[96]), .Z(o1[96]) );
XOR3UD1BWP30P140 U97 ( .A1(z0[97]), .A2(z1[97]), .A3(z2[97]), .Z(o1[97]) );
XOR3UD1BWP30P140 U98 ( .A1(z0[98]), .A2(z1[98]), .A3(z2[98]), .Z(o1[98]) );
XOR3UD1BWP30P140 U99 ( .A1(z0[99]), .A2(z1[99]), .A3(z2[99]), .Z(o1[99]) );
XOR3UD1BWP30P140 U100 ( .A1(z0[100]), .A2(z1[100]), .A3(z2[100]), .Z(o1[100]) );
XOR3UD1BWP30P140 U101 ( .A1(z0[101]), .A2(z1[101]), .A3(z2[101]), .Z(o1[101]) );
XOR3UD1BWP30P140 U102 ( .A1(z0[102]), .A2(z1[102]), .A3(z2[102]), .Z(o1[102]) );
XOR3UD1BWP30P140 U103 ( .A1(z0[103]), .A2(z1[103]), .A3(z2[103]), .Z(o1[103]) );
XOR3UD1BWP30P140 U104 ( .A1(z0[104]), .A2(z1[104]), .A3(z2[104]), .Z(o1[104]) );
XOR3UD1BWP30P140 U105 ( .A1(z0[105]), .A2(z1[105]), .A3(z2[105]), .Z(o1[105]) );
XOR3UD1BWP30P140 U106 ( .A1(z0[106]), .A2(z1[106]), .A3(z2[106]), .Z(o1[106]) );
XOR3UD1BWP30P140 U107 ( .A1(z0[107]), .A2(z1[107]), .A3(z2[107]), .Z(o1[107]) );
XOR3UD1BWP30P140 U108 ( .A1(z0[108]), .A2(z1[108]), .A3(z2[108]), .Z(o1[108]) );
XOR3UD1BWP30P140 U109 ( .A1(z0[109]), .A2(z1[109]), .A3(z2[109]), .Z(o1[109]) );
XOR3UD1BWP30P140 U110 ( .A1(z0[110]), .A2(z1[110]), .A3(z2[110]), .Z(o1[110]) );
XOR3UD1BWP30P140 U111 ( .A1(z0[111]), .A2(z1[111]), .A3(z2[111]), .Z(o1[111]) );
XOR3UD1BWP30P140 U112 ( .A1(z0[112]), .A2(z1[112]), .A3(z2[112]), .Z(o1[112]) );
XOR3UD1BWP30P140 U113 ( .A1(z0[113]), .A2(z1[113]), .A3(z2[113]), .Z(o1[113]) );
XOR3UD1BWP30P140 U114 ( .A1(z0[114]), .A2(z1[114]), .A3(z2[114]), .Z(o1[114]) );
XOR3UD1BWP30P140 U115 ( .A1(z0[115]), .A2(z1[115]), .A3(z2[115]), .Z(o1[115]) );
XOR3UD1BWP30P140 U116 ( .A1(z0[116]), .A2(z1[116]), .A3(z2[116]), .Z(o1[116]) );
XOR3UD1BWP30P140 U117 ( .A1(z0[117]), .A2(z1[117]), .A3(z2[117]), .Z(o1[117]) );
XOR3UD1BWP30P140 U118 ( .A1(z0[118]), .A2(z1[118]), .A3(z2[118]), .Z(o1[118]) );
XOR3UD1BWP30P140 U119 ( .A1(z0[119]), .A2(z1[119]), .A3(z2[119]), .Z(o1[119]) );
XOR3UD1BWP30P140 U120 ( .A1(z0[120]), .A2(z1[120]), .A3(z2[120]), .Z(o1[120]) );
XOR3UD1BWP30P140 U121 ( .A1(z0[121]), .A2(z1[121]), .A3(z2[121]), .Z(o1[121]) );
XOR3UD1BWP30P140 U122 ( .A1(z0[122]), .A2(z1[122]), .A3(z2[122]), .Z(o1[122]) );
XOR3UD1BWP30P140 U123 ( .A1(z0[123]), .A2(z1[123]), .A3(z2[123]), .Z(o1[123]) );
XOR3UD1BWP30P140 U124 ( .A1(z0[124]), .A2(z1[124]), .A3(z2[124]), .Z(o1[124]) );
XOR3UD1BWP30P140 U125 ( .A1(z0[125]), .A2(z1[125]), .A3(z2[125]), .Z(o1[125]) );
XOR3UD1BWP30P140 U126 ( .A1(z0[126]), .A2(z1[126]), .A3(z2[126]), .Z(o1[126]) );
assign y[0] = z0[0];
XOR2UD1BWP30P140 U127 ( .A1(z0[1]), .A2(z2[0]), .Z(y[2]) );
XOR2UD1BWP30P140 U128 ( .A1(z0[2]), .A2(z2[1]), .Z(y[4]) );
XOR2UD1BWP30P140 U129 ( .A1(z0[3]), .A2(z2[2]), .Z(y[6]) );
XOR2UD1BWP30P140 U130 ( .A1(z0[4]), .A2(z2[3]), .Z(y[8]) );
XOR2UD1BWP30P140 U131 ( .A1(z0[5]), .A2(z2[4]), .Z(y[10]) );
XOR2UD1BWP30P140 U132 ( .A1(z0[6]), .A2(z2[5]), .Z(y[12]) );
XOR2UD1BWP30P140 U133 ( .A1(z0[7]), .A2(z2[6]), .Z(y[14]) );
XOR2UD1BWP30P140 U134 ( .A1(z0[8]), .A2(z2[7]), .Z(y[16]) );
XOR2UD1BWP30P140 U135 ( .A1(z0[9]), .A2(z2[8]), .Z(y[18]) );
XOR2UD1BWP30P140 U136 ( .A1(z0[10]), .A2(z2[9]), .Z(y[20]) );
XOR2UD1BWP30P140 U137 ( .A1(z0[11]), .A2(z2[10]), .Z(y[22]) );
XOR2UD1BWP30P140 U138 ( .A1(z0[12]), .A2(z2[11]), .Z(y[24]) );
XOR2UD1BWP30P140 U139 ( .A1(z0[13]), .A2(z2[12]), .Z(y[26]) );
XOR2UD1BWP30P140 U140 ( .A1(z0[14]), .A2(z2[13]), .Z(y[28]) );
XOR2UD1BWP30P140 U141 ( .A1(z0[15]), .A2(z2[14]), .Z(y[30]) );
XOR2UD1BWP30P140 U142 ( .A1(z0[16]), .A2(z2[15]), .Z(y[32]) );
XOR2UD1BWP30P140 U143 ( .A1(z0[17]), .A2(z2[16]), .Z(y[34]) );
XOR2UD1BWP30P140 U144 ( .A1(z0[18]), .A2(z2[17]), .Z(y[36]) );
XOR2UD1BWP30P140 U145 ( .A1(z0[19]), .A2(z2[18]), .Z(y[38]) );
XOR2UD1BWP30P140 U146 ( .A1(z0[20]), .A2(z2[19]), .Z(y[40]) );
XOR2UD1BWP30P140 U147 ( .A1(z0[21]), .A2(z2[20]), .Z(y[42]) );
XOR2UD1BWP30P140 U148 ( .A1(z0[22]), .A2(z2[21]), .Z(y[44]) );
XOR2UD1BWP30P140 U149 ( .A1(z0[23]), .A2(z2[22]), .Z(y[46]) );
XOR2UD1BWP30P140 U150 ( .A1(z0[24]), .A2(z2[23]), .Z(y[48]) );
XOR2UD1BWP30P140 U151 ( .A1(z0[25]), .A2(z2[24]), .Z(y[50]) );
XOR2UD1BWP30P140 U152 ( .A1(z0[26]), .A2(z2[25]), .Z(y[52]) );
XOR2UD1BWP30P140 U153 ( .A1(z0[27]), .A2(z2[26]), .Z(y[54]) );
XOR2UD1BWP30P140 U154 ( .A1(z0[28]), .A2(z2[27]), .Z(y[56]) );
XOR2UD1BWP30P140 U155 ( .A1(z0[29]), .A2(z2[28]), .Z(y[58]) );
XOR2UD1BWP30P140 U156 ( .A1(z0[30]), .A2(z2[29]), .Z(y[60]) );
XOR2UD1BWP30P140 U157 ( .A1(z0[31]), .A2(z2[30]), .Z(y[62]) );
XOR2UD1BWP30P140 U158 ( .A1(z0[32]), .A2(z2[31]), .Z(y[64]) );
XOR2UD1BWP30P140 U159 ( .A1(z0[33]), .A2(z2[32]), .Z(y[66]) );
XOR2UD1BWP30P140 U160 ( .A1(z0[34]), .A2(z2[33]), .Z(y[68]) );
XOR2UD1BWP30P140 U161 ( .A1(z0[35]), .A2(z2[34]), .Z(y[70]) );
XOR2UD1BWP30P140 U162 ( .A1(z0[36]), .A2(z2[35]), .Z(y[72]) );
XOR2UD1BWP30P140 U163 ( .A1(z0[37]), .A2(z2[36]), .Z(y[74]) );
XOR2UD1BWP30P140 U164 ( .A1(z0[38]), .A2(z2[37]), .Z(y[76]) );
XOR2UD1BWP30P140 U165 ( .A1(z0[39]), .A2(z2[38]), .Z(y[78]) );
XOR2UD1BWP30P140 U166 ( .A1(z0[40]), .A2(z2[39]), .Z(y[80]) );
XOR2UD1BWP30P140 U167 ( .A1(z0[41]), .A2(z2[40]), .Z(y[82]) );
XOR2UD1BWP30P140 U168 ( .A1(z0[42]), .A2(z2[41]), .Z(y[84]) );
XOR2UD1BWP30P140 U169 ( .A1(z0[43]), .A2(z2[42]), .Z(y[86]) );
XOR2UD1BWP30P140 U170 ( .A1(z0[44]), .A2(z2[43]), .Z(y[88]) );
XOR2UD1BWP30P140 U171 ( .A1(z0[45]), .A2(z2[44]), .Z(y[90]) );
XOR2UD1BWP30P140 U172 ( .A1(z0[46]), .A2(z2[45]), .Z(y[92]) );
XOR2UD1BWP30P140 U173 ( .A1(z0[47]), .A2(z2[46]), .Z(y[94]) );
XOR2UD1BWP30P140 U174 ( .A1(z0[48]), .A2(z2[47]), .Z(y[96]) );
XOR2UD1BWP30P140 U175 ( .A1(z0[49]), .A2(z2[48]), .Z(y[98]) );
XOR2UD1BWP30P140 U176 ( .A1(z0[50]), .A2(z2[49]), .Z(y[100]) );
XOR2UD1BWP30P140 U177 ( .A1(z0[51]), .A2(z2[50]), .Z(y[102]) );
XOR2UD1BWP30P140 U178 ( .A1(z0[52]), .A2(z2[51]), .Z(y[104]) );
XOR2UD1BWP30P140 U179 ( .A1(z0[53]), .A2(z2[52]), .Z(y[106]) );
XOR2UD1BWP30P140 U180 ( .A1(z0[54]), .A2(z2[53]), .Z(y[108]) );
XOR2UD1BWP30P140 U181 ( .A1(z0[55]), .A2(z2[54]), .Z(y[110]) );
XOR2UD1BWP30P140 U182 ( .A1(z0[56]), .A2(z2[55]), .Z(y[112]) );
XOR2UD1BWP30P140 U183 ( .A1(z0[57]), .A2(z2[56]), .Z(y[114]) );
XOR2UD1BWP30P140 U184 ( .A1(z0[58]), .A2(z2[57]), .Z(y[116]) );
XOR2UD1BWP30P140 U185 ( .A1(z0[59]), .A2(z2[58]), .Z(y[118]) );
XOR2UD1BWP30P140 U186 ( .A1(z0[60]), .A2(z2[59]), .Z(y[120]) );
XOR2UD1BWP30P140 U187 ( .A1(z0[61]), .A2(z2[60]), .Z(y[122]) );
XOR2UD1BWP30P140 U188 ( .A1(z0[62]), .A2(z2[61]), .Z(y[124]) );
XOR2UD1BWP30P140 U189 ( .A1(z0[63]), .A2(z2[62]), .Z(y[126]) );
FXOR2UD1BWP30P140 U190 ( .en(C_g1[18]), .A1(z0[64]), .A2(z2[63]), .Z(y[128]) );
XOR2UD1BWP30P140 U191 ( .A1(z0[65]), .A2(z2[64]), .Z(y[130]) );
XOR2UD1BWP30P140 U192 ( .A1(z0[66]), .A2(z2[65]), .Z(y[132]) );
XOR2UD1BWP30P140 U193 ( .A1(z0[67]), .A2(z2[66]), .Z(y[134]) );
XOR2UD1BWP30P140 U194 ( .A1(z0[68]), .A2(z2[67]), .Z(y[136]) );
XOR2UD1BWP30P140 U195 ( .A1(z0[69]), .A2(z2[68]), .Z(y[138]) );
XOR2UD1BWP30P140 U196 ( .A1(z0[70]), .A2(z2[69]), .Z(y[140]) );
XOR2UD1BWP30P140 U197 ( .A1(z0[71]), .A2(z2[70]), .Z(y[142]) );
XOR2UD1BWP30P140 U198 ( .A1(z0[72]), .A2(z2[71]), .Z(y[144]) );
XOR2UD1BWP30P140 U199 ( .A1(z0[73]), .A2(z2[72]), .Z(y[146]) );
XOR2UD1BWP30P140 U200 ( .A1(z0[74]), .A2(z2[73]), .Z(y[148]) );
XOR2UD1BWP30P140 U201 ( .A1(z0[75]), .A2(z2[74]), .Z(y[150]) );
XOR2UD1BWP30P140 U202 ( .A1(z0[76]), .A2(z2[75]), .Z(y[152]) );
XOR2UD1BWP30P140 U203 ( .A1(z0[77]), .A2(z2[76]), .Z(y[154]) );
XOR2UD1BWP30P140 U204 ( .A1(z0[78]), .A2(z2[77]), .Z(y[156]) );
XOR2UD1BWP30P140 U205 ( .A1(z0[79]), .A2(z2[78]), .Z(y[158]) );
XOR2UD1BWP30P140 U206 ( .A1(z0[80]), .A2(z2[79]), .Z(y[160]) );
XOR2UD1BWP30P140 U207 ( .A1(z0[81]), .A2(z2[80]), .Z(y[162]) );
XOR2UD1BWP30P140 U208 ( .A1(z0[82]), .A2(z2[81]), .Z(y[164]) );
XOR2UD1BWP30P140 U209 ( .A1(z0[83]), .A2(z2[82]), .Z(y[166]) );
XOR2UD1BWP30P140 U210 ( .A1(z0[84]), .A2(z2[83]), .Z(y[168]) );
XOR2UD1BWP30P140 U211 ( .A1(z0[85]), .A2(z2[84]), .Z(y[170]) );
XOR2UD1BWP30P140 U212 ( .A1(z0[86]), .A2(z2[85]), .Z(y[172]) );
XOR2UD1BWP30P140 U213 ( .A1(z0[87]), .A2(z2[86]), .Z(y[174]) );
XOR2UD1BWP30P140 U214 ( .A1(z0[88]), .A2(z2[87]), .Z(y[176]) );
XOR2UD1BWP30P140 U215 ( .A1(z0[89]), .A2(z2[88]), .Z(y[178]) );
XOR2UD1BWP30P140 U216 ( .A1(z0[90]), .A2(z2[89]), .Z(y[180]) );
XOR2UD1BWP30P140 U217 ( .A1(z0[91]), .A2(z2[90]), .Z(y[182]) );
XOR2UD1BWP30P140 U218 ( .A1(z0[92]), .A2(z2[91]), .Z(y[184]) );
XOR2UD1BWP30P140 U219 ( .A1(z0[93]), .A2(z2[92]), .Z(y[186]) );
XOR2UD1BWP30P140 U220 ( .A1(z0[94]), .A2(z2[93]), .Z(y[188]) );
XOR2UD1BWP30P140 U221 ( .A1(z0[95]), .A2(z2[94]), .Z(y[190]) );
XOR2UD1BWP30P140 U222 ( .A1(z0[96]), .A2(z2[95]), .Z(y[192]) );
XOR2UD1BWP30P140 U223 ( .A1(z0[97]), .A2(z2[96]), .Z(y[194]) );
XOR2UD1BWP30P140 U224 ( .A1(z0[98]), .A2(z2[97]), .Z(y[196]) );
XOR2UD1BWP30P140 U225 ( .A1(z0[99]), .A2(z2[98]), .Z(y[198]) );
XOR2UD1BWP30P140 U226 ( .A1(z0[100]), .A2(z2[99]), .Z(y[200]) );
XOR2UD1BWP30P140 U227 ( .A1(z0[101]), .A2(z2[100]), .Z(y[202]) );
XOR2UD1BWP30P140 U228 ( .A1(z0[102]), .A2(z2[101]), .Z(y[204]) );
XOR2UD1BWP30P140 U229 ( .A1(z0[103]), .A2(z2[102]), .Z(y[206]) );
XOR2UD1BWP30P140 U230 ( .A1(z0[104]), .A2(z2[103]), .Z(y[208]) );
XOR2UD1BWP30P140 U231 ( .A1(z0[105]), .A2(z2[104]), .Z(y[210]) );
XOR2UD1BWP30P140 U232 ( .A1(z0[106]), .A2(z2[105]), .Z(y[212]) );
XOR2UD1BWP30P140 U233 ( .A1(z0[107]), .A2(z2[106]), .Z(y[214]) );
XOR2UD1BWP30P140 U234 ( .A1(z0[108]), .A2(z2[107]), .Z(y[216]) );
XOR2UD1BWP30P140 U235 ( .A1(z0[109]), .A2(z2[108]), .Z(y[218]) );
XOR2UD1BWP30P140 U236 ( .A1(z0[110]), .A2(z2[109]), .Z(y[220]) );
XOR2UD1BWP30P140 U237 ( .A1(z0[111]), .A2(z2[110]), .Z(y[222]) );
XOR2UD1BWP30P140 U238 ( .A1(z0[112]), .A2(z2[111]), .Z(y[224]) );
XOR2UD1BWP30P140 U239 ( .A1(z0[113]), .A2(z2[112]), .Z(y[226]) );
XOR2UD1BWP30P140 U240 ( .A1(z0[114]), .A2(z2[113]), .Z(y[228]) );
XOR2UD1BWP30P140 U241 ( .A1(z0[115]), .A2(z2[114]), .Z(y[230]) );
XOR2UD1BWP30P140 U242 ( .A1(z0[116]), .A2(z2[115]), .Z(y[232]) );
XOR2UD1BWP30P140 U243 ( .A1(z0[117]), .A2(z2[116]), .Z(y[234]) );
XOR2UD1BWP30P140 U244 ( .A1(z0[118]), .A2(z2[117]), .Z(y[236]) );
XOR2UD1BWP30P140 U245 ( .A1(z0[119]), .A2(z2[118]), .Z(y[238]) );
XOR2UD1BWP30P140 U246 ( .A1(z0[120]), .A2(z2[119]), .Z(y[240]) );
XOR2UD1BWP30P140 U247 ( .A1(z0[121]), .A2(z2[120]), .Z(y[242]) );
XOR2UD1BWP30P140 U248 ( .A1(z0[122]), .A2(z2[121]), .Z(y[244]) );
XOR2UD1BWP30P140 U249 ( .A1(z0[123]), .A2(z2[122]), .Z(y[246]) );
XOR2UD1BWP30P140 U250 ( .A1(z0[124]), .A2(z2[123]), .Z(y[248]) );
XOR2UD1BWP30P140 U251 ( .A1(z0[125]), .A2(z2[124]), .Z(y[250]) );
XOR2UD1BWP30P140 U252 ( .A1(z0[126]), .A2(z2[125]), .Z(y[252]) );
assign y[254] = z2[126];
assign y[1] = o1[0];
assign y[3] = o1[1];
assign y[5] = o1[2];
assign y[7] = o1[3];
assign y[9] = o1[4];
assign y[11] = o1[5];
assign y[13] = o1[6];
assign y[15] = o1[7];
assign y[17] = o1[8];
assign y[19] = o1[9];
assign y[21] = o1[10];
assign y[23] = o1[11];
assign y[25] = o1[12];
assign y[27] = o1[13];
assign y[29] = o1[14];
assign y[31] = o1[15];
assign y[33] = o1[16];
assign y[35] = o1[17];
assign y[37] = o1[18];
assign y[39] = o1[19];
assign y[41] = o1[20];
assign y[43] = o1[21];
assign y[45] = o1[22];
assign y[47] = o1[23];
assign y[49] = o1[24];
assign y[51] = o1[25];
assign y[53] = o1[26];
assign y[55] = o1[27];
assign y[57] = o1[28];
assign y[59] = o1[29];
assign y[61] = o1[30];
assign y[63] = o1[31];
assign y[65] = o1[32];
assign y[67] = o1[33];
assign y[69] = o1[34];
assign y[71] = o1[35];
assign y[73] = o1[36];
assign y[75] = o1[37];
assign y[77] = o1[38];
assign y[79] = o1[39];
assign y[81] = o1[40];
assign y[83] = o1[41];
assign y[85] = o1[42];
assign y[87] = o1[43];
assign y[89] = o1[44];
assign y[91] = o1[45];
assign y[93] = o1[46];
assign y[95] = o1[47];
assign y[97] = o1[48];
assign y[99] = o1[49];
assign y[101] = o1[50];
assign y[103] = o1[51];
assign y[105] = o1[52];
assign y[107] = o1[53];
assign y[109] = o1[54];
assign y[111] = o1[55];
assign y[113] = o1[56];
assign y[115] = o1[57];
assign y[117] = o1[58];
assign y[119] = o1[59];
assign y[121] = o1[60];
assign y[123] = o1[61];
assign y[125] = o1[62];
assign y[127] = o1[63];
assign y[129] = o1[64];
assign y[131] = o1[65];
assign y[133] = o1[66];
assign y[135] = o1[67];
assign y[137] = o1[68];
assign y[139] = o1[69];
assign y[141] = o1[70];
assign y[143] = o1[71];
assign y[145] = o1[72];
assign y[147] = o1[73];
assign y[149] = o1[74];
assign y[151] = o1[75];
assign y[153] = o1[76];
assign y[155] = o1[77];
assign y[157] = o1[78];
assign y[159] = o1[79];
assign y[161] = o1[80];
assign y[163] = o1[81];
assign y[165] = o1[82];
assign y[167] = o1[83];
assign y[169] = o1[84];
assign y[171] = o1[85];
assign y[173] = o1[86];
assign y[175] = o1[87];
assign y[177] = o1[88];
assign y[179] = o1[89];
assign y[181] = o1[90];
assign y[183] = o1[91];
assign y[185] = o1[92];
assign y[187] = o1[93];
assign y[189] = o1[94];
assign y[191] = o1[95];
assign y[193] = o1[96];
assign y[195] = o1[97];
assign y[197] = o1[98];
assign y[199] = o1[99];
assign y[201] = o1[100];
assign y[203] = o1[101];
assign y[205] = o1[102];
assign y[207] = o1[103];
assign y[209] = o1[104];
assign y[211] = o1[105];
assign y[213] = o1[106];
assign y[215] = o1[107];
assign y[217] = o1[108];
assign y[219] = o1[109];
assign y[221] = o1[110];
assign y[223] = o1[111];
assign y[225] = o1[112];
assign y[227] = o1[113];
assign y[229] = o1[114];
assign y[231] = o1[115];
assign y[233] = o1[116];
assign y[235] = o1[117];
assign y[237] = o1[118];
assign y[239] = o1[119];
assign y[241] = o1[120];
assign y[243] = o1[121];
assign y[245] = o1[122];
assign y[247] = o1[123];
assign y[249] = o1[124];
assign y[251] = o1[125];
assign y[253] = o1[126];
endmodule


module gf_mul_128_top ( clk, rst_n, en, clked, a, b, c );
  input [127:0] a;
  input [127:0] b;
  output [127:0] c;
  input clk, rst_n, en, clked;
  wire   n1, n2, n3, n4, n5, n6, n7;
  wire   [127:0] c_w;

  wire [21:0] C_g1;

  delay_chain dchain_x ( .clked(clked), .C_g1(C_g1) );


  gf_mul_128 mul_x ( .a(a), .b(b), .c(c_w), .C_g1(C_g1), .rst_n(rst_n) );
  EDFCNQD1BWP30P140 \c_o_reg[127]  ( .D(c_w[127]), .E(n7), .CP(clk), .CDN(
        rst_n), .Q(c[127]) );
  EDFCNQD1BWP30P140 \c_o_reg[126]  ( .D(c_w[126]), .E(n7), .CP(clk), .CDN(
        rst_n), .Q(c[126]) );
  EDFCNQD1BWP30P140 \c_o_reg[125]  ( .D(c_w[125]), .E(n7), .CP(clk), .CDN(
        rst_n), .Q(c[125]) );
  EDFCNQD1BWP30P140 \c_o_reg[124]  ( .D(c_w[124]), .E(n7), .CP(clk), .CDN(
        rst_n), .Q(c[124]) );
  EDFCNQD1BWP30P140 \c_o_reg[123]  ( .D(c_w[123]), .E(n7), .CP(clk), .CDN(
        rst_n), .Q(c[123]) );
  EDFCNQD1BWP30P140 \c_o_reg[122]  ( .D(c_w[122]), .E(n7), .CP(clk), .CDN(
        rst_n), .Q(c[122]) );
  EDFCNQD1BWP30P140 \c_o_reg[121]  ( .D(c_w[121]), .E(n7), .CP(clk), .CDN(
        rst_n), .Q(c[121]) );
  EDFCNQD1BWP30P140 \c_o_reg[120]  ( .D(c_w[120]), .E(n7), .CP(clk), .CDN(
        rst_n), .Q(c[120]) );
  EDFCNQD1BWP30P140 \c_o_reg[119]  ( .D(c_w[119]), .E(n7), .CP(clk), .CDN(
        rst_n), .Q(c[119]) );
  EDFCNQD1BWP30P140 \c_o_reg[118]  ( .D(c_w[118]), .E(n7), .CP(clk), .CDN(
        rst_n), .Q(c[118]) );
  EDFCNQD1BWP30P140 \c_o_reg[117]  ( .D(c_w[117]), .E(n7), .CP(clk), .CDN(
        rst_n), .Q(c[117]) );
  EDFCNQD1BWP30P140 \c_o_reg[116]  ( .D(c_w[116]), .E(n6), .CP(clk), .CDN(
        rst_n), .Q(c[116]) );
  EDFCNQD1BWP30P140 \c_o_reg[115]  ( .D(c_w[115]), .E(n6), .CP(clk), .CDN(
        rst_n), .Q(c[115]) );
  EDFCNQD1BWP30P140 \c_o_reg[114]  ( .D(c_w[114]), .E(n6), .CP(clk), .CDN(
        rst_n), .Q(c[114]) );
  EDFCNQD1BWP30P140 \c_o_reg[113]  ( .D(c_w[113]), .E(n6), .CP(clk), .CDN(
        rst_n), .Q(c[113]) );
  EDFCNQD1BWP30P140 \c_o_reg[112]  ( .D(c_w[112]), .E(n6), .CP(clk), .CDN(
        rst_n), .Q(c[112]) );
  EDFCNQD1BWP30P140 \c_o_reg[111]  ( .D(c_w[111]), .E(n6), .CP(clk), .CDN(
        rst_n), .Q(c[111]) );
  EDFCNQD1BWP30P140 \c_o_reg[110]  ( .D(c_w[110]), .E(n6), .CP(clk), .CDN(
        rst_n), .Q(c[110]) );
  EDFCNQD1BWP30P140 \c_o_reg[109]  ( .D(c_w[109]), .E(n6), .CP(clk), .CDN(
        rst_n), .Q(c[109]) );
  EDFCNQD1BWP30P140 \c_o_reg[108]  ( .D(c_w[108]), .E(n6), .CP(clk), .CDN(
        rst_n), .Q(c[108]) );
  EDFCNQD1BWP30P140 \c_o_reg[107]  ( .D(c_w[107]), .E(n6), .CP(clk), .CDN(
        rst_n), .Q(c[107]) );
  EDFCNQD1BWP30P140 \c_o_reg[106]  ( .D(c_w[106]), .E(n6), .CP(clk), .CDN(
        rst_n), .Q(c[106]) );
  EDFCNQD1BWP30P140 \c_o_reg[105]  ( .D(c_w[105]), .E(n6), .CP(clk), .CDN(
        rst_n), .Q(c[105]) );
  EDFCNQD1BWP30P140 \c_o_reg[104]  ( .D(c_w[104]), .E(n6), .CP(clk), .CDN(
        rst_n), .Q(c[104]) );
  EDFCNQD1BWP30P140 \c_o_reg[103]  ( .D(c_w[103]), .E(n5), .CP(clk), .CDN(
        rst_n), .Q(c[103]) );
  EDFCNQD1BWP30P140 \c_o_reg[102]  ( .D(c_w[102]), .E(n5), .CP(clk), .CDN(
        rst_n), .Q(c[102]) );
  EDFCNQD1BWP30P140 \c_o_reg[101]  ( .D(c_w[101]), .E(n5), .CP(clk), .CDN(
        rst_n), .Q(c[101]) );
  EDFCNQD1BWP30P140 \c_o_reg[100]  ( .D(c_w[100]), .E(n5), .CP(clk), .CDN(
        rst_n), .Q(c[100]) );
  EDFCNQD1BWP30P140 \c_o_reg[99]  ( .D(c_w[99]), .E(n5), .CP(clk), .CDN(rst_n),
        .Q(c[99]) );
  EDFCNQD1BWP30P140 \c_o_reg[98]  ( .D(c_w[98]), .E(n5), .CP(clk), .CDN(rst_n),
        .Q(c[98]) );
  EDFCNQD1BWP30P140 \c_o_reg[97]  ( .D(c_w[97]), .E(n5), .CP(clk), .CDN(rst_n),
        .Q(c[97]) );
  EDFCNQD1BWP30P140 \c_o_reg[96]  ( .D(c_w[96]), .E(n5), .CP(clk), .CDN(rst_n),
        .Q(c[96]) );
  EDFCNQD1BWP30P140 \c_o_reg[95]  ( .D(c_w[95]), .E(n5), .CP(clk), .CDN(rst_n),
        .Q(c[95]) );
  EDFCNQD1BWP30P140 \c_o_reg[94]  ( .D(c_w[94]), .E(n5), .CP(clk), .CDN(rst_n),
        .Q(c[94]) );
  EDFCNQD1BWP30P140 \c_o_reg[93]  ( .D(c_w[93]), .E(n5), .CP(clk), .CDN(rst_n),
        .Q(c[93]) );
  EDFCNQD1BWP30P140 \c_o_reg[92]  ( .D(c_w[92]), .E(n5), .CP(clk), .CDN(rst_n),
        .Q(c[92]) );
  EDFCNQD1BWP30P140 \c_o_reg[91]  ( .D(c_w[91]), .E(n5), .CP(clk), .CDN(rst_n),
        .Q(c[91]) );
  EDFCNQD1BWP30P140 \c_o_reg[90]  ( .D(c_w[90]), .E(n4), .CP(clk), .CDN(rst_n),
        .Q(c[90]) );
  EDFCNQD1BWP30P140 \c_o_reg[89]  ( .D(c_w[89]), .E(n4), .CP(clk), .CDN(rst_n),
        .Q(c[89]) );
  EDFCNQD1BWP30P140 \c_o_reg[88]  ( .D(c_w[88]), .E(n4), .CP(clk), .CDN(rst_n),
        .Q(c[88]) );
  EDFCNQD1BWP30P140 \c_o_reg[87]  ( .D(c_w[87]), .E(n4), .CP(clk), .CDN(rst_n),
        .Q(c[87]) );
  EDFCNQD1BWP30P140 \c_o_reg[86]  ( .D(c_w[86]), .E(n4), .CP(clk), .CDN(rst_n),
        .Q(c[86]) );
  EDFCNQD1BWP30P140 \c_o_reg[85]  ( .D(c_w[85]), .E(n4), .CP(clk), .CDN(rst_n),
        .Q(c[85]) );
  EDFCNQD1BWP30P140 \c_o_reg[84]  ( .D(c_w[84]), .E(n4), .CP(clk), .CDN(rst_n),
        .Q(c[84]) );
  EDFCNQD1BWP30P140 \c_o_reg[83]  ( .D(c_w[83]), .E(n4), .CP(clk), .CDN(rst_n),
        .Q(c[83]) );
  EDFCNQD1BWP30P140 \c_o_reg[82]  ( .D(c_w[82]), .E(n4), .CP(clk), .CDN(rst_n),
        .Q(c[82]) );
  EDFCNQD1BWP30P140 \c_o_reg[81]  ( .D(c_w[81]), .E(n4), .CP(clk), .CDN(rst_n),
        .Q(c[81]) );
  EDFCNQD1BWP30P140 \c_o_reg[80]  ( .D(c_w[80]), .E(n4), .CP(clk), .CDN(rst_n),
        .Q(c[80]) );
  EDFCNQD1BWP30P140 \c_o_reg[79]  ( .D(c_w[79]), .E(n4), .CP(clk), .CDN(rst_n),
        .Q(c[79]) );
  EDFCNQD1BWP30P140 \c_o_reg[78]  ( .D(c_w[78]), .E(n4), .CP(clk), .CDN(rst_n),
        .Q(c[78]) );
  EDFCNQD1BWP30P140 \c_o_reg[77]  ( .D(c_w[77]), .E(n2), .CP(clk), .CDN(rst_n),
        .Q(c[77]) );
  EDFCNQD1BWP30P140 \c_o_reg[76]  ( .D(c_w[76]), .E(n6), .CP(clk), .CDN(rst_n),
        .Q(c[76]) );
  EDFCNQD1BWP30P140 \c_o_reg[75]  ( .D(c_w[75]), .E(n4), .CP(clk), .CDN(rst_n),
        .Q(c[75]) );
  EDFCNQD1BWP30P140 \c_o_reg[74]  ( .D(c_w[74]), .E(n5), .CP(clk), .CDN(rst_n),
        .Q(c[74]) );
  EDFCNQD1BWP30P140 \c_o_reg[73]  ( .D(c_w[73]), .E(n3), .CP(clk), .CDN(rst_n),
        .Q(c[73]) );
  EDFCNQD1BWP30P140 \c_o_reg[72]  ( .D(c_w[72]), .E(n6), .CP(clk), .CDN(rst_n),
        .Q(c[72]) );
  EDFCNQD1BWP30P140 \c_o_reg[71]  ( .D(c_w[71]), .E(n4), .CP(clk), .CDN(rst_n),
        .Q(c[71]) );
  EDFCNQD1BWP30P140 \c_o_reg[70]  ( .D(c_w[70]), .E(n5), .CP(clk), .CDN(rst_n),
        .Q(c[70]) );
  EDFCNQD1BWP30P140 \c_o_reg[69]  ( .D(c_w[69]), .E(n2), .CP(clk), .CDN(rst_n),
        .Q(c[69]) );
  EDFCNQD1BWP30P140 \c_o_reg[68]  ( .D(c_w[68]), .E(n6), .CP(clk), .CDN(rst_n),
        .Q(c[68]) );
  EDFCNQD1BWP30P140 \c_o_reg[67]  ( .D(c_w[67]), .E(n4), .CP(clk), .CDN(rst_n),
        .Q(c[67]) );
  EDFCNQD1BWP30P140 \c_o_reg[66]  ( .D(c_w[66]), .E(n5), .CP(clk), .CDN(rst_n),
        .Q(c[66]) );
  EDFCNQD1BWP30P140 \c_o_reg[65]  ( .D(c_w[65]), .E(n3), .CP(clk), .CDN(rst_n),
        .Q(c[65]) );
  EDFCNQD1BWP30P140 \c_o_reg[64]  ( .D(c_w[64]), .E(n3), .CP(clk), .CDN(rst_n),
        .Q(c[64]) );
  EDFCNQD1BWP30P140 \c_o_reg[63]  ( .D(c_w[63]), .E(n3), .CP(clk), .CDN(rst_n),
        .Q(c[63]) );
  EDFCNQD1BWP30P140 \c_o_reg[62]  ( .D(c_w[62]), .E(n3), .CP(clk), .CDN(rst_n),
        .Q(c[62]) );
  EDFCNQD1BWP30P140 \c_o_reg[61]  ( .D(c_w[61]), .E(n3), .CP(clk), .CDN(rst_n),
        .Q(c[61]) );
  EDFCNQD1BWP30P140 \c_o_reg[60]  ( .D(c_w[60]), .E(n3), .CP(clk), .CDN(rst_n),
        .Q(c[60]) );
  EDFCNQD1BWP30P140 \c_o_reg[59]  ( .D(c_w[59]), .E(n3), .CP(clk), .CDN(rst_n),
        .Q(c[59]) );
  EDFCNQD1BWP30P140 \c_o_reg[58]  ( .D(c_w[58]), .E(n3), .CP(clk), .CDN(rst_n),
        .Q(c[58]) );
  EDFCNQD1BWP30P140 \c_o_reg[57]  ( .D(c_w[57]), .E(n3), .CP(clk), .CDN(rst_n),
        .Q(c[57]) );
  EDFCNQD1BWP30P140 \c_o_reg[56]  ( .D(c_w[56]), .E(n3), .CP(clk), .CDN(rst_n),
        .Q(c[56]) );
  EDFCNQD1BWP30P140 \c_o_reg[55]  ( .D(c_w[55]), .E(n3), .CP(clk), .CDN(rst_n),
        .Q(c[55]) );
  EDFCNQD1BWP30P140 \c_o_reg[54]  ( .D(c_w[54]), .E(n3), .CP(clk), .CDN(rst_n),
        .Q(c[54]) );
  EDFCNQD1BWP30P140 \c_o_reg[53]  ( .D(c_w[53]), .E(n3), .CP(clk), .CDN(rst_n),
        .Q(c[53]) );
  EDFCNQD1BWP30P140 \c_o_reg[52]  ( .D(c_w[52]), .E(n3), .CP(clk), .CDN(rst_n),
        .Q(c[52]) );
  EDFCNQD1BWP30P140 \c_o_reg[51]  ( .D(c_w[51]), .E(n2), .CP(clk), .CDN(rst_n),
        .Q(c[51]) );
  EDFCNQD1BWP30P140 \c_o_reg[50]  ( .D(c_w[50]), .E(n2), .CP(clk), .CDN(rst_n),
        .Q(c[50]) );
  EDFCNQD1BWP30P140 \c_o_reg[49]  ( .D(c_w[49]), .E(n2), .CP(clk), .CDN(rst_n),
        .Q(c[49]) );
  EDFCNQD1BWP30P140 \c_o_reg[48]  ( .D(c_w[48]), .E(n2), .CP(clk), .CDN(rst_n),
        .Q(c[48]) );
  EDFCNQD1BWP30P140 \c_o_reg[47]  ( .D(c_w[47]), .E(n2), .CP(clk), .CDN(rst_n),
        .Q(c[47]) );
  EDFCNQD1BWP30P140 \c_o_reg[46]  ( .D(c_w[46]), .E(n2), .CP(clk), .CDN(rst_n),
        .Q(c[46]) );
  EDFCNQD1BWP30P140 \c_o_reg[45]  ( .D(c_w[45]), .E(n2), .CP(clk), .CDN(rst_n),
        .Q(c[45]) );
  EDFCNQD1BWP30P140 \c_o_reg[44]  ( .D(c_w[44]), .E(n2), .CP(clk), .CDN(rst_n),
        .Q(c[44]) );
  EDFCNQD1BWP30P140 \c_o_reg[43]  ( .D(c_w[43]), .E(n2), .CP(clk), .CDN(rst_n),
        .Q(c[43]) );
  EDFCNQD1BWP30P140 \c_o_reg[42]  ( .D(c_w[42]), .E(n2), .CP(clk), .CDN(rst_n),
        .Q(c[42]) );
  EDFCNQD1BWP30P140 \c_o_reg[41]  ( .D(c_w[41]), .E(n2), .CP(clk), .CDN(rst_n),
        .Q(c[41]) );
  EDFCNQD1BWP30P140 \c_o_reg[40]  ( .D(c_w[40]), .E(n2), .CP(clk), .CDN(rst_n),
        .Q(c[40]) );
  EDFCNQD1BWP30P140 \c_o_reg[39]  ( .D(c_w[39]), .E(n2), .CP(clk), .CDN(rst_n),
        .Q(c[39]) );
  EDFCNQD1BWP30P140 \c_o_reg[38]  ( .D(c_w[38]), .E(n2), .CP(clk), .CDN(rst_n),
        .Q(c[38]) );
  EDFCNQD1BWP30P140 \c_o_reg[37]  ( .D(c_w[37]), .E(n3), .CP(clk), .CDN(rst_n),
        .Q(c[37]) );
  EDFCNQD1BWP30P140 \c_o_reg[36]  ( .D(c_w[36]), .E(n4), .CP(clk), .CDN(rst_n),
        .Q(c[36]) );
  EDFCNQD1BWP30P140 \c_o_reg[35]  ( .D(c_w[35]), .E(n5), .CP(clk), .CDN(rst_n),
        .Q(c[35]) );
  EDFCNQD1BWP30P140 \c_o_reg[34]  ( .D(c_w[34]), .E(n6), .CP(clk), .CDN(rst_n),
        .Q(c[34]) );
  EDFCNQD1BWP30P140 \c_o_reg[33]  ( .D(c_w[33]), .E(n2), .CP(clk), .CDN(rst_n),
        .Q(c[33]) );
  EDFCNQD1BWP30P140 \c_o_reg[32]  ( .D(c_w[32]), .E(n3), .CP(clk), .CDN(rst_n),
        .Q(c[32]) );
  EDFCNQD1BWP30P140 \c_o_reg[31]  ( .D(c_w[31]), .E(n4), .CP(clk), .CDN(rst_n),
        .Q(c[31]) );
  EDFCNQD1BWP30P140 \c_o_reg[30]  ( .D(c_w[30]), .E(n5), .CP(clk), .CDN(rst_n),
        .Q(c[30]) );
  EDFCNQD1BWP30P140 \c_o_reg[29]  ( .D(c_w[29]), .E(n6), .CP(clk), .CDN(rst_n),
        .Q(c[29]) );
  EDFCNQD1BWP30P140 \c_o_reg[28]  ( .D(c_w[28]), .E(n2), .CP(clk), .CDN(rst_n),
        .Q(c[28]) );
  EDFCNQD1BWP30P140 \c_o_reg[27]  ( .D(c_w[27]), .E(n3), .CP(clk), .CDN(rst_n),
        .Q(c[27]) );
  EDFCNQD1BWP30P140 \c_o_reg[26]  ( .D(c_w[26]), .E(n7), .CP(clk), .CDN(rst_n),
        .Q(c[26]) );
  EDFCNQD1BWP30P140 \c_o_reg[25]  ( .D(c_w[25]), .E(n1), .CP(clk), .CDN(rst_n),
        .Q(c[25]) );
  EDFCNQD1BWP30P140 \c_o_reg[24]  ( .D(c_w[24]), .E(n1), .CP(clk), .CDN(rst_n),
        .Q(c[24]) );
  EDFCNQD1BWP30P140 \c_o_reg[23]  ( .D(c_w[23]), .E(n1), .CP(clk), .CDN(rst_n),
        .Q(c[23]) );
  EDFCNQD1BWP30P140 \c_o_reg[22]  ( .D(c_w[22]), .E(n1), .CP(clk), .CDN(rst_n),
        .Q(c[22]) );
  EDFCNQD1BWP30P140 \c_o_reg[21]  ( .D(c_w[21]), .E(n1), .CP(clk), .CDN(rst_n),
        .Q(c[21]) );
  EDFCNQD1BWP30P140 \c_o_reg[20]  ( .D(c_w[20]), .E(n1), .CP(clk), .CDN(rst_n),
        .Q(c[20]) );
  EDFCNQD1BWP30P140 \c_o_reg[19]  ( .D(c_w[19]), .E(n1), .CP(clk), .CDN(rst_n),
        .Q(c[19]) );
  EDFCNQD1BWP30P140 \c_o_reg[18]  ( .D(c_w[18]), .E(n1), .CP(clk), .CDN(rst_n),
        .Q(c[18]) );
  EDFCNQD1BWP30P140 \c_o_reg[17]  ( .D(c_w[17]), .E(n1), .CP(clk), .CDN(rst_n),
        .Q(c[17]) );
  EDFCNQD1BWP30P140 \c_o_reg[16]  ( .D(c_w[16]), .E(n1), .CP(clk), .CDN(rst_n),
        .Q(c[16]) );
  EDFCNQD1BWP30P140 \c_o_reg[15]  ( .D(c_w[15]), .E(n1), .CP(clk), .CDN(rst_n),
        .Q(c[15]) );
  EDFCNQD1BWP30P140 \c_o_reg[14]  ( .D(c_w[14]), .E(n1), .CP(clk), .CDN(rst_n),
        .Q(c[14]) );
  EDFCNQD1BWP30P140 \c_o_reg[13]  ( .D(c_w[13]), .E(n1), .CP(clk), .CDN(rst_n),
        .Q(c[13]) );
  EDFCNQD1BWP30P140 \c_o_reg[12]  ( .D(c_w[12]), .E(n7), .CP(clk), .CDN(rst_n),
        .Q(c[12]) );
  EDFCNQD1BWP30P140 \c_o_reg[11]  ( .D(c_w[11]), .E(n1), .CP(clk), .CDN(rst_n),
        .Q(c[11]) );
  EDFCNQD1BWP30P140 \c_o_reg[10]  ( .D(c_w[10]), .E(n7), .CP(clk), .CDN(rst_n),
        .Q(c[10]) );
  EDFCNQD1BWP30P140 \c_o_reg[9]  ( .D(c_w[9]), .E(n1), .CP(clk), .CDN(rst_n),
        .Q(c[9]) );
  EDFCNQD1BWP30P140 \c_o_reg[8]  ( .D(c_w[8]), .E(n7), .CP(clk), .CDN(rst_n),
        .Q(c[8]) );
  EDFCNQD1BWP30P140 \c_o_reg[7]  ( .D(c_w[7]), .E(n1), .CP(clk), .CDN(rst_n),
        .Q(c[7]) );
  EDFCNQD1BWP30P140 \c_o_reg[6]  ( .D(c_w[6]), .E(n7), .CP(clk), .CDN(rst_n),
        .Q(c[6]) );
  EDFCNQD1BWP30P140 \c_o_reg[5]  ( .D(c_w[5]), .E(n1), .CP(clk), .CDN(rst_n),
        .Q(c[5]) );
  EDFCNQD1BWP30P140 \c_o_reg[4]  ( .D(c_w[4]), .E(n7), .CP(clk), .CDN(rst_n),
        .Q(c[4]) );
  EDFCNQD1BWP30P140 \c_o_reg[3]  ( .D(c_w[3]), .E(n1), .CP(clk), .CDN(rst_n),
        .Q(c[3]) );
  EDFCNQD1BWP30P140 \c_o_reg[2]  ( .D(c_w[2]), .E(n7), .CP(clk), .CDN(rst_n),
        .Q(c[2]) );
  EDFCNQD1BWP30P140 \c_o_reg[1]  ( .D(c_w[1]), .E(n1), .CP(clk), .CDN(rst_n),
        .Q(c[1]) );
  EDFCNQD1BWP30P140 \c_o_reg[0]  ( .D(c_w[0]), .E(n7), .CP(clk), .CDN(rst_n),
        .Q(c[0]) );
  CKBD1BWP30P140 U3 ( .I(en), .Z(n1) );
  CKBD1BWP30P140 U4 ( .I(en), .Z(n2) );
  CKBD1BWP30P140 U5 ( .I(en), .Z(n3) );
  CKBD1BWP30P140 U6 ( .I(en), .Z(n4) );
  CKBD1BWP30P140 U7 ( .I(en), .Z(n5) );
  CKBD1BWP30P140 U8 ( .I(en), .Z(n6) );
  CKBD1BWP30P140 U9 ( .I(en), .Z(n7) );
endmodule

