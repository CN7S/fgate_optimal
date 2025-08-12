
// KA 16 type , 2-term
module OKA_16bit
(
   input [15:0] a,
   input [15:0] b,
   output [30:0] y
);
// wire 
wire [7:0] aa;
wire [7:0] bb;
wire [7:0] al;
wire [7:0] ah;
wire [7:0] bl;
wire [7:0] bh;
wire [7:0] z0;
wire [14:0] z1;
wire [7:0] z2;
wire [6:0] o;

wire [14:0] yy;


assign al[0] = a[0];
assign al[1] = a[1];
assign al[2] = a[2];
assign al[3] = a[3];
assign al[4] = a[4];
assign al[5] = a[5];
assign al[6] = a[6];
assign al[7] = a[7];
assign ah[0] = a[8];
assign ah[1] = a[9];
assign ah[2] = a[10];
assign ah[3] = a[11];
assign ah[4] = a[12];
assign ah[5] = a[13];
assign ah[6] = a[14];
assign ah[7] = a[15];
assign bl[0] = b[0];
assign bl[1] = b[1];
assign bl[2] = b[2];
assign bl[3] = b[3];
assign bl[4] = b[4];
assign bl[5] = b[5];
assign bl[6] = b[6];
assign bl[7] = b[7];
assign bh[0] = b[8];
assign bh[1] = b[9];
assign bh[2] = b[10];
assign bh[3] = b[11];
assign bh[4] = b[12];
assign bh[5] = b[13];
assign bh[6] = b[14];
assign bh[7] = b[15];
s_16bit s16_u
(
   .a(a),
   .b(b),
   .aa(aa),
   .bb(bb)
);

OKA_8bit_0 mul8_0
(
.a(al),
.b(bl),
.y(z0)
);
OKA_8bit_1 mul8_1
(
.a(aa),
.b(bb),
.y(z1)
);
OKA_8bit_2 mul8_2
(
.a(ah),
.b(bh),
.y(z2)
);

OS_XOR2 os_xor2_u
(
   .a0(al),
   .b0(bl),
   .a1(ah),
   .b1(bh),
   .y(o)
);
 
os_16bit os16_u
(
   .z0(z0),
   .z1(z1),
   .z2(z2),
   .o(o),
   .y(yy)
);

assign y[0] = z0[0];
assign y[1] = z0[1];
assign y[2] = z0[2];
assign y[3] = z0[3];
assign y[4] = z0[4];
assign y[5] = z0[5];
assign y[6] = z0[6];
assign y[7] = z0[7];

assign y[8] = yy[0];
assign y[9] = yy[1];
assign y[10] = yy[2];
assign y[11] = yy[3];
assign y[12] = yy[4];
assign y[13] = yy[5];
assign y[14] = yy[6];
assign y[15] = yy[7];
assign y[16] = yy[8];
assign y[17] = yy[9];
assign y[18] = yy[10];
assign y[19] = yy[11];
assign y[20] = yy[12];
assign y[21] = yy[13];
assign y[22] = yy[14];

assign y[23] = z2[0];
assign y[24] = z2[1];
assign y[25] = z2[2];
assign y[26] = z2[3];
assign y[27] = z2[4];
assign y[28] = z2[5];
assign y[29] = z2[6];
assign y[30] = z2[7];
endmodule
// slice 
module s_16bit
(
   input [15:0] a,
   input [15:0] b,
   output [7:0] aa,
   output [7:0] bb
);
XOR2UD1BWP30P140 U0 ( .A1(a[0]), .A2(a[8]), .Z(aa[0]) );
XOR2UD1BWP30P140 U1 ( .A1(a[1]), .A2(a[9]), .Z(aa[1]) );
XOR2UD1BWP30P140 U2 ( .A1(a[2]), .A2(a[10]), .Z(aa[2]) );
XOR2UD1BWP30P140 U3 ( .A1(a[3]), .A2(a[11]), .Z(aa[3]) );
XOR2UD1BWP30P140 U4 ( .A1(a[4]), .A2(a[12]), .Z(aa[4]) );
XOR2UD1BWP30P140 U5 ( .A1(a[5]), .A2(a[13]), .Z(aa[5]) );
XOR2UD1BWP30P140 U6 ( .A1(a[6]), .A2(a[14]), .Z(aa[6]) );
XOR2UD1BWP30P140 U7 ( .A1(a[7]), .A2(a[15]), .Z(aa[7]) );
XOR2UD1BWP30P140 U8 ( .A1(b[0]), .A2(b[8]), .Z(bb[0]) );
XOR2UD1BWP30P140 U9 ( .A1(b[1]), .A2(b[9]), .Z(bb[1]) );
XOR2UD1BWP30P140 U10 ( .A1(b[2]), .A2(b[10]), .Z(bb[2]) );
XOR2UD1BWP30P140 U11 ( .A1(b[3]), .A2(b[11]), .Z(bb[3]) );
XOR2UD1BWP30P140 U12 ( .A1(b[4]), .A2(b[12]), .Z(bb[4]) );
XOR2UD1BWP30P140 U13 ( .A1(b[5]), .A2(b[13]), .Z(bb[5]) );
XOR2UD1BWP30P140 U14 ( .A1(b[6]), .A2(b[14]), .Z(bb[6]) );
XOR2UD1BWP30P140 U15 ( .A1(b[7]), .A2(b[15]), .Z(bb[7]) );
endmodule


module os_16bit
(
   input [7:0] z0,
   input [14:0] z1,
   input [7:0] z2,
   input [6:0] o,
   output [14:0] y
);
XOR3UD1BWP30P140 U7 ( .A1(z1[0]), .A2(z0[0]), .A3(o[0]), .Z(y[0]) );
XOR3UD1BWP30P140 U8 ( .A1(z1[1]), .A2(z0[1]), .A3(o[1]), .Z(y[1]) );
XOR3UD1BWP30P140 U9 ( .A1(z1[2]), .A2(z0[2]), .A3(o[2]), .Z(y[2]) );
XOR3UD1BWP30P140 U10 ( .A1(z1[3]), .A2(z0[3]), .A3(o[3]), .Z(y[3]) );
XOR3UD1BWP30P140 U11 ( .A1(z1[4]), .A2(z0[4]), .A3(o[4]), .Z(y[4]) );
XOR3UD1BWP30P140 U12 ( .A1(z1[5]), .A2(z0[5]), .A3(o[5]), .Z(y[5]) );
XOR3UD1BWP30P140 U13 ( .A1(z1[6]), .A2(z0[6]), .A3(o[6]), .Z(y[6]) );
XOR3UD1BWP30P140 U14 ( .A1(z2[0]), .A2(z1[7]), .A3(z0[7]), .Z(y[7]) );
XOR3UD1BWP30P140 U15 ( .A1(z1[8]), .A2(z2[1]), .A3(o[0]), .Z(y[8]) );
XOR3UD1BWP30P140 U16 ( .A1(z1[9]), .A2(z2[2]), .A3(o[1]), .Z(y[9]) );
XOR3UD1BWP30P140 U17 ( .A1(z1[10]), .A2(z2[3]), .A3(o[2]), .Z(y[10]) );
XOR3UD1BWP30P140 U18 ( .A1(z1[11]), .A2(z2[4]), .A3(o[3]), .Z(y[11]) );
XOR3UD1BWP30P140 U19 ( .A1(z1[12]), .A2(z2[5]), .A3(o[4]), .Z(y[12]) );
XOR3UD1BWP30P140 U20 ( .A1(z1[13]), .A2(z2[6]), .A3(o[5]), .Z(y[13]) );
XOR3UD1BWP30P140 U21 ( .A1(z1[14]), .A2(z2[7]), .A3(o[6]), .Z(y[14]) );
endmodule

// SBM 8 bit

module OS_XOR2 ( a0, b0, a1, b1, y );
  input [7:0] a0;
  input [7:0] b0;
  input [7:0] a1;
  input [7:0] b1;
  output [6:0] y;
  wire   n71, n72, n73, n74, n75, n76, n77, n78, n79, n80, n81, n82, n83, n84,
         n85, n86, n87, n88, n89, n90, n91, n92, n93, n94, n95, n96, n97, n98,
         n99, n100, n101, n102, n103, n104, n105, n106, n107, n108, n109, n110,
         n111, n112, n113, n114, n115, n116, n117, n118, n119, n120, n121,
         n122, n123, n124, n125, n126, n127, n128, n129, n130, n131, n132,
         n133, n134, n135, n136, n137, n138, n139, n140;

  XOR2UD1BWP30P140 U1 ( .A1(n90), .A2(n89), .Z(y[1]) );
  XOR4D1BWP30P140 U2 ( .A1(n84), .A2(n83), .A3(n82), .A4(n81), .Z(n90) );
  XOR4D1BWP30P140 U3 ( .A1(n88), .A2(n87), .A3(n86), .A4(n85), .Z(n89) );
  CKND2D1BWP30P140 U4 ( .A1(a0[4]), .A2(b0[5]), .ZN(n84) );
  XOR2UD1BWP30P140 U5 ( .A1(n80), .A2(n79), .Z(y[0]) );
  XOR4D1BWP30P140 U6 ( .A1(n74), .A2(n73), .A3(n72), .A4(n71), .Z(n80) );
  XOR4D1BWP30P140 U7 ( .A1(n78), .A2(n77), .A3(n76), .A4(n75), .Z(n79) );
  CKND2D1BWP30P140 U8 ( .A1(a0[3]), .A2(b0[5]), .ZN(n74) );
  XOR2UD1BWP30P140 U9 ( .A1(n120), .A2(n119), .Z(y[4]) );
  XOR4D1BWP30P140 U10 ( .A1(n114), .A2(n113), .A3(n112), .A4(n111), .Z(n120)
         );
  XOR4D1BWP30P140 U11 ( .A1(n118), .A2(n117), .A3(n116), .A4(n115), .Z(n119)
         );
  CKND2D1BWP30P140 U12 ( .A1(b0[5]), .A2(a0[7]), .ZN(n114) );
  XOR2UD1BWP30P140 U13 ( .A1(n110), .A2(n109), .Z(y[3]) );
  XOR4D1BWP30P140 U14 ( .A1(n104), .A2(n103), .A3(n102), .A4(n101), .Z(n110)
         );
  XOR4D1BWP30P140 U15 ( .A1(n108), .A2(n107), .A3(n106), .A4(n105), .Z(n109)
         );
  CKND2D1BWP30P140 U16 ( .A1(b0[5]), .A2(a0[6]), .ZN(n104) );
  XOR2UD1BWP30P140 U17 ( .A1(n100), .A2(n99), .Z(y[2]) );
  XOR4D1BWP30P140 U18 ( .A1(n94), .A2(n93), .A3(n92), .A4(n91), .Z(n100) );
  XOR4D1BWP30P140 U19 ( .A1(n98), .A2(n97), .A3(n96), .A4(n95), .Z(n99) );
  CKND2D1BWP30P140 U20 ( .A1(b0[5]), .A2(a0[5]), .ZN(n94) );
  XOR2UD1BWP30P140 U21 ( .A1(n140), .A2(n139), .Z(y[6]) );
  XOR4D1BWP30P140 U22 ( .A1(n134), .A2(n133), .A3(n132), .A4(n131), .Z(n140)
         );
  XOR4D1BWP30P140 U23 ( .A1(n138), .A2(n137), .A3(n136), .A4(n135), .Z(n139)
         );
  CKND2D1BWP30P140 U24 ( .A1(b1[5]), .A2(a1[1]), .ZN(n134) );
  XOR2UD1BWP30P140 U25 ( .A1(n130), .A2(n129), .Z(y[5]) );
  XOR4D1BWP30P140 U26 ( .A1(n124), .A2(n123), .A3(n122), .A4(n121), .Z(n130)
         );
  XOR4D1BWP30P140 U27 ( .A1(n128), .A2(n127), .A3(n126), .A4(n125), .Z(n129)
         );
  CKND2D1BWP30P140 U28 ( .A1(b1[5]), .A2(a1[0]), .ZN(n124) );
  CKND2D1BWP30P140 U29 ( .A1(b1[1]), .A2(a1[1]), .ZN(n98) );
  CKND2D1BWP30P140 U30 ( .A1(b1[1]), .A2(a1[0]), .ZN(n88) );
  CKND2D1BWP30P140 U31 ( .A1(a0[6]), .A2(b0[7]), .ZN(n121) );
  CKND2D1BWP30P140 U32 ( .A1(a0[5]), .A2(b0[7]), .ZN(n111) );
  CKND2D1BWP30P140 U33 ( .A1(b1[2]), .A2(a1[1]), .ZN(n105) );
  CKND2D1BWP30P140 U34 ( .A1(a0[4]), .A2(b0[7]), .ZN(n101) );
  CKND2D1BWP30P140 U35 ( .A1(a0[3]), .A2(b0[7]), .ZN(n91) );
  CKND2D1BWP30P140 U36 ( .A1(a0[2]), .A2(b0[7]), .ZN(n81) );
  CKND2D1BWP30P140 U37 ( .A1(b0[2]), .A2(a0[6]), .ZN(n75) );
  CKND2D1BWP30P140 U38 ( .A1(a0[1]), .A2(b0[7]), .ZN(n71) );
  CKND2D1BWP30P140 U39 ( .A1(b1[2]), .A2(a1[0]), .ZN(n95) );
  CKND2D1BWP30P140 U40 ( .A1(b1[1]), .A2(a1[3]), .ZN(n118) );
  CKND2D1BWP30P140 U41 ( .A1(b0[7]), .A2(a0[7]), .ZN(n131) );
  CKND2D1BWP30P140 U42 ( .A1(b0[2]), .A2(a0[7]), .ZN(n85) );
  CKND2D1BWP30P140 U43 ( .A1(b1[1]), .A2(a1[4]), .ZN(n128) );
  CKND2D1BWP30P140 U44 ( .A1(b1[1]), .A2(a1[2]), .ZN(n108) );
  CKND2D1BWP30P140 U45 ( .A1(b1[2]), .A2(a1[3]), .ZN(n125) );
  CKND2D1BWP30P140 U46 ( .A1(b1[2]), .A2(a1[4]), .ZN(n135) );
  CKND2D1BWP30P140 U47 ( .A1(b1[2]), .A2(a1[2]), .ZN(n115) );
  CKND2D1BWP30P140 U48 ( .A1(b1[4]), .A2(a1[1]), .ZN(n123) );
  CKND2D1BWP30P140 U49 ( .A1(b0[4]), .A2(a0[6]), .ZN(n93) );
  CKND2D1BWP30P140 U50 ( .A1(b1[0]), .A2(a1[1]), .ZN(n87) );
  CKND2D1BWP30P140 U51 ( .A1(b0[4]), .A2(a0[5]), .ZN(n83) );
  CKND2D1BWP30P140 U52 ( .A1(b1[4]), .A2(a1[0]), .ZN(n113) );
  CKND2D1BWP30P140 U53 ( .A1(b1[0]), .A2(a1[0]), .ZN(n77) );
  CKND2D1BWP30P140 U54 ( .A1(b1[3]), .A2(a1[1]), .ZN(n116) );
  CKND2D1BWP30P140 U55 ( .A1(a0[6]), .A2(b0[6]), .ZN(n112) );
  CKND2D1BWP30P140 U56 ( .A1(a0[5]), .A2(b0[6]), .ZN(n102) );
  CKND2D1BWP30P140 U57 ( .A1(a0[4]), .A2(b0[6]), .ZN(n92) );
  CKND2D1BWP30P140 U58 ( .A1(b0[3]), .A2(a0[6]), .ZN(n86) );
  CKND2D1BWP30P140 U59 ( .A1(a0[3]), .A2(b0[6]), .ZN(n82) );
  CKND2D1BWP30P140 U60 ( .A1(b0[3]), .A2(a0[5]), .ZN(n76) );
  CKND2D1BWP30P140 U61 ( .A1(a0[2]), .A2(b0[6]), .ZN(n72) );
  CKND2D1BWP30P140 U62 ( .A1(b0[4]), .A2(a0[7]), .ZN(n103) );
  CKND2D1BWP30P140 U63 ( .A1(b1[6]), .A2(a1[0]), .ZN(n132) );
  CKND2D1BWP30P140 U64 ( .A1(b1[3]), .A2(a1[0]), .ZN(n106) );
  CKND2D1BWP30P140 U65 ( .A1(b0[6]), .A2(a0[7]), .ZN(n122) );
  CKND2D1BWP30P140 U66 ( .A1(b0[3]), .A2(a0[7]), .ZN(n96) );
  CKND2D1BWP30P140 U67 ( .A1(b1[1]), .A2(a1[5]), .ZN(n138) );
  CKND2D1BWP30P140 U68 ( .A1(b1[0]), .A2(a1[3]), .ZN(n107) );
  CKND2D1BWP30P140 U69 ( .A1(b1[4]), .A2(a1[2]), .ZN(n133) );
  CKND2D1BWP30P140 U70 ( .A1(b1[0]), .A2(a1[4]), .ZN(n117) );
  CKND2D1BWP30P140 U71 ( .A1(b1[0]), .A2(a1[2]), .ZN(n97) );
  CKND2D1BWP30P140 U72 ( .A1(b1[3]), .A2(a1[3]), .ZN(n136) );
  CKND2D1BWP30P140 U73 ( .A1(b1[3]), .A2(a1[2]), .ZN(n126) );
  CKND2D1BWP30P140 U74 ( .A1(b1[0]), .A2(a1[5]), .ZN(n127) );
  CKND2D1BWP30P140 U75 ( .A1(b0[4]), .A2(a0[4]), .ZN(n73) );
  CKND2D1BWP30P140 U76 ( .A1(b0[1]), .A2(a0[7]), .ZN(n78) );
  CKND2D1BWP30P140 U77 ( .A1(b1[0]), .A2(a1[6]), .ZN(n137) );
endmodule



module OKA_8bit_0 ( a, b, y );
  input [7:0] a;
  input [7:0] b;
  output [7:0] y;
  wire   n45, n46, n47, n48, n49, n50, n51, n52, n53, n54, n55, n56, n57, n58,
         n59, n60, n61, n62, n63, n64, n65, n66, n67, n68, n69, n70, n71, n72,
         n73, n74, n75, n76, n77, n78, n79, n80, n81, n82, n83, n84, n85, n86,
         n87, n88;

  XOR2UD1BWP30P140 U1 ( .A1(n84), .A2(n83), .Z(y[7]) );
  XOR4D1BWP30P140 U2 ( .A1(n78), .A2(n77), .A3(n76), .A4(n75), .Z(n84) );
  XOR4D1BWP30P140 U3 ( .A1(n82), .A2(n81), .A3(n80), .A4(n79), .Z(n83) );
  CKND2D1BWP30P140 U4 ( .A1(b[5]), .A2(a[2]), .ZN(n78) );
  XOR4D1BWP30P140 U5 ( .A1(n66), .A2(n65), .A3(n64), .A4(n63), .Z(y[5]) );
  CKND2D1BWP30P140 U6 ( .A1(b[0]), .A2(a[5]), .ZN(n63) );
  NR2D1BWP30P140 U7 ( .A1(n87), .A2(n86), .ZN(n66) );
  NR2D1BWP30P140 U8 ( .A1(n88), .A2(n85), .ZN(n65) );
  XOR4D1BWP30P140 U9 ( .A1(n70), .A2(n69), .A3(n68), .A4(n67), .Z(n74) );
  CKND2D1BWP30P140 U10 ( .A1(b[4]), .A2(a[2]), .ZN(n70) );
  CKND2D1BWP30P140 U11 ( .A1(a[0]), .A2(b[6]), .ZN(n67) );
  CKND2D1BWP30P140 U12 ( .A1(b[3]), .A2(a[3]), .ZN(n69) );
  XOR3UD1BWP30P140 U13 ( .A1(n59), .A2(n58), .A3(n57), .Z(y[4]) );
  CKND2D1BWP30P140 U14 ( .A1(b[0]), .A2(a[4]), .ZN(n58) );
  NR2D1BWP30P140 U15 ( .A1(n87), .A2(n85), .ZN(n59) );
  XOR3UD1BWP30P140 U16 ( .A1(n56), .A2(n55), .A3(n54), .Z(n57) );
  XOR3UD1BWP30P140 U17 ( .A1(n49), .A2(n48), .A3(n47), .Z(y[2]) );
  AN2D1BWP30P140 U18 ( .A1(a[2]), .A2(b[0]), .Z(n47) );
  AN2D1BWP30P140 U19 ( .A1(a[0]), .A2(b[2]), .Z(n48) );
  INR2D1BWP30P140 U20 ( .A1(a[1]), .B1(n85), .ZN(n49) );
  INVD1BWP30P140 U21 ( .I(b[2]), .ZN(n86) );
  AN2D1BWP30P140 U22 ( .A1(a[0]), .A2(b[0]), .Z(y[0]) );
  XOR3UD1BWP30P140 U23 ( .A1(n62), .A2(n61), .A3(n60), .Z(n64) );
  CKND2D1BWP30P140 U24 ( .A1(b[3]), .A2(a[2]), .ZN(n60) );
  CKND2D1BWP30P140 U25 ( .A1(b[4]), .A2(a[1]), .ZN(n61) );
  CKND2D1BWP30P140 U26 ( .A1(b[5]), .A2(a[0]), .ZN(n62) );
  CKND2D1BWP30P140 U27 ( .A1(b[3]), .A2(a[1]), .ZN(n55) );
  CKND2D1BWP30P140 U28 ( .A1(b[7]), .A2(a[0]), .ZN(n75) );
  INVD1BWP30P140 U29 ( .I(a[4]), .ZN(n88) );
  INVD1BWP30P140 U30 ( .I(a[3]), .ZN(n87) );
  CKND2D1BWP30P140 U31 ( .A1(b[2]), .A2(a[5]), .ZN(n79) );
  CKND2D1BWP30P140 U32 ( .A1(b[4]), .A2(a[0]), .ZN(n56) );
  CKND2D1BWP30P140 U33 ( .A1(b[4]), .A2(a[3]), .ZN(n77) );
  CKND2D1BWP30P140 U34 ( .A1(b[6]), .A2(a[1]), .ZN(n76) );
  CKND2D1BWP30P140 U35 ( .A1(b[5]), .A2(a[1]), .ZN(n68) );
  CKND2D1BWP30P140 U36 ( .A1(b[3]), .A2(a[4]), .ZN(n80) );
  CKND2D1BWP30P140 U37 ( .A1(b[0]), .A2(a[7]), .ZN(n81) );
  CKND2D1BWP30P140 U38 ( .A1(b[2]), .A2(a[2]), .ZN(n54) );
  CKND2D1BWP30P140 U39 ( .A1(b[2]), .A2(a[1]), .ZN(n51) );
  XOR2UD1BWP30P140 U40 ( .A1(n46), .A2(n45), .Z(y[1]) );
  CKND2D1BWP30P140 U41 ( .A1(b[0]), .A2(a[1]), .ZN(n46) );
  CKND2D1BWP30P140 U42 ( .A1(b[1]), .A2(a[0]), .ZN(n45) );
  INVD1BWP30P140 U43 ( .I(b[1]), .ZN(n85) );
  XOR4D1BWP30P140 U44 ( .A1(n53), .A2(n52), .A3(n51), .A4(n50), .Z(y[3]) );
  CKND2D1BWP30P140 U45 ( .A1(b[3]), .A2(a[0]), .ZN(n50) );
  CKND2D1BWP30P140 U46 ( .A1(b[1]), .A2(a[2]), .ZN(n53) );
  CKND2D1BWP30P140 U47 ( .A1(b[0]), .A2(a[3]), .ZN(n52) );
  XOR4D1BWP30P140 U48 ( .A1(n74), .A2(n73), .A3(n72), .A4(n71), .Z(y[6]) );
  CKND2D1BWP30P140 U49 ( .A1(b[0]), .A2(a[6]), .ZN(n71) );
  CKND2D1BWP30P140 U50 ( .A1(b[1]), .A2(a[5]), .ZN(n72) );
  NR2D1BWP30P140 U51 ( .A1(n88), .A2(n86), .ZN(n73) );
  CKND2D1BWP30P140 U52 ( .A1(b[1]), .A2(a[6]), .ZN(n82) );
endmodule

module OKA_8bit_1 ( a, b, y );
  input [7:0] a;
  input [7:0] b;
  output [14:0] y;
  wire   n79, n80, n81, n82, n83, n84, n85, n86, n87, n88, n89, n90, n91, n92,
         n93, n94, n95, n96, n97, n98, n99, n100, n101, n102, n103, n104, n105,
         n106, n107, n108, n109, n110, n111, n112, n113, n114, n115, n116,
         n117, n118, n119, n120, n121, n122, n123, n124, n125, n126, n127,
         n128, n129, n130, n131, n132, n133, n134, n135, n136, n137, n138,
         n139, n140, n141, n142, n143, n144, n145, n146, n147, n148, n149,
         n150, n151, n152, n153, n154, n155, n156;

  INVD1BWP30P140 U1 ( .I(a[6]), .ZN(n156) );
  INVD1BWP30P140 U2 ( .I(b[3]), .ZN(n151) );
  INVD1BWP30P140 U3 ( .I(b[2]), .ZN(n150) );
  INVD1BWP30P140 U4 ( .I(b[4]), .ZN(n152) );
  XOR2UD1BWP30P140 U5 ( .A1(n93), .A2(n92), .Z(y[13]) );
  CKND2D1BWP30P140 U6 ( .A1(a[6]), .A2(b[7]), .ZN(n92) );
  CKND2D1BWP30P140 U7 ( .A1(a[7]), .A2(b[6]), .ZN(n93) );
  INVD1BWP30P140 U8 ( .I(a[3]), .ZN(n153) );
  CKND2D1BWP30P140 U9 ( .A1(a[2]), .A2(b[5]), .ZN(n127) );
  INVD1BWP30P140 U10 ( .I(a[4]), .ZN(n154) );
  CKND2D1BWP30P140 U11 ( .A1(b[6]), .A2(a[4]), .ZN(n80) );
  CKND2D1BWP30P140 U12 ( .A1(a[2]), .A2(b[6]), .ZN(n135) );
  CKND2D1BWP30P140 U13 ( .A1(a[1]), .A2(b[6]), .ZN(n125) );
  CKND2D1BWP30P140 U14 ( .A1(a[5]), .A2(b[6]), .ZN(n86) );
  CKND2D1BWP30P140 U15 ( .A1(a[1]), .A2(b[3]), .ZN(n104) );
  CKND2D1BWP30P140 U16 ( .A1(b[2]), .A2(a[2]), .ZN(n103) );
  INVD1BWP30P140 U17 ( .I(a[5]), .ZN(n155) );
  CKND2D1BWP30P140 U18 ( .A1(a[5]), .A2(b[5]), .ZN(n79) );
  CKND2D1BWP30P140 U19 ( .A1(a[0]), .A2(b[7]), .ZN(n124) );
  CKND2D1BWP30P140 U20 ( .A1(a[1]), .A2(b[5]), .ZN(n117) );
  CKND2D1BWP30P140 U21 ( .A1(a[0]), .A2(b[4]), .ZN(n105) );
  CKND2D1BWP30P140 U22 ( .A1(b[7]), .A2(a[3]), .ZN(n81) );
  CKND2D1BWP30P140 U23 ( .A1(b[4]), .A2(a[3]), .ZN(n126) );
  CKND2D1BWP30P140 U24 ( .A1(b[0]), .A2(a[7]), .ZN(n130) );
  CKND2D1BWP30P140 U25 ( .A1(b[3]), .A2(a[4]), .ZN(n129) );
  CKND2D1BWP30P140 U26 ( .A1(a[1]), .A2(b[2]), .ZN(n100) );
  CKND2D1BWP30P140 U27 ( .A1(a[5]), .A2(b[2]), .ZN(n128) );
  XOR4D1BWP30P140 U28 ( .A1(n137), .A2(n136), .A3(n135), .A4(n134), .Z(n141)
         );
  CKND2D1BWP30P140 U29 ( .A1(a[3]), .A2(b[5]), .ZN(n137) );
  CKND2D1BWP30P140 U30 ( .A1(a[1]), .A2(b[7]), .ZN(n134) );
  CKND2D1BWP30P140 U31 ( .A1(b[4]), .A2(a[4]), .ZN(n136) );
  XOR4D1BWP30P140 U32 ( .A1(n119), .A2(n118), .A3(n117), .A4(n116), .Z(n123)
         );
  CKND2D1BWP30P140 U33 ( .A1(b[4]), .A2(a[2]), .ZN(n119) );
  CKND2D1BWP30P140 U34 ( .A1(b[3]), .A2(a[3]), .ZN(n118) );
  CKND2D1BWP30P140 U35 ( .A1(a[0]), .A2(b[6]), .ZN(n116) );
  XOR4D1BWP30P140 U36 ( .A1(n115), .A2(n114), .A3(n113), .A4(n112), .Z(y[5])
         );
  CKND2D1BWP30P140 U37 ( .A1(b[0]), .A2(a[5]), .ZN(n112) );
  NR2D1BWP30P140 U38 ( .A1(n153), .A2(n150), .ZN(n115) );
  NR2D1BWP30P140 U39 ( .A1(n154), .A2(n149), .ZN(n114) );
  XOR4D1BWP30P140 U40 ( .A1(n148), .A2(n147), .A3(n146), .A4(n145), .Z(y[9])
         );
  CKND2D1BWP30P140 U41 ( .A1(b[2]), .A2(a[7]), .ZN(n145) );
  NR2D1BWP30P140 U42 ( .A1(n155), .A2(n152), .ZN(n148) );
  NR2D1BWP30P140 U43 ( .A1(n156), .A2(n151), .ZN(n147) );
  XOR4D1BWP30P140 U44 ( .A1(n88), .A2(n87), .A3(n86), .A4(n85), .Z(y[11]) );
  CKND2D1BWP30P140 U45 ( .A1(a[6]), .A2(b[5]), .ZN(n88) );
  CKND2D1BWP30P140 U46 ( .A1(b[7]), .A2(a[4]), .ZN(n85) );
  CKND2D1BWP30P140 U47 ( .A1(b[4]), .A2(a[7]), .ZN(n87) );
  AN2D1BWP30P140 U48 ( .A1(a[0]), .A2(b[0]), .Z(y[0]) );
  AN2D1BWP30P140 U49 ( .A1(b[7]), .A2(a[7]), .Z(y[14]) );
  XOR3UD1BWP30P140 U50 ( .A1(n108), .A2(n107), .A3(n106), .Z(y[4]) );
  CKND2D1BWP30P140 U51 ( .A1(b[0]), .A2(a[4]), .ZN(n107) );
  NR2D1BWP30P140 U52 ( .A1(n153), .A2(n149), .ZN(n108) );
  XOR3UD1BWP30P140 U53 ( .A1(n105), .A2(n104), .A3(n103), .Z(n106) );
  XOR3UD1BWP30P140 U54 ( .A1(n84), .A2(n83), .A3(n82), .Z(y[10]) );
  CKND2D1BWP30P140 U55 ( .A1(b[3]), .A2(a[7]), .ZN(n83) );
  NR2D1BWP30P140 U56 ( .A1(n152), .A2(n156), .ZN(n84) );
  XOR3UD1BWP30P140 U57 ( .A1(n81), .A2(n80), .A3(n79), .Z(n82) );
  XOR3UD1BWP30P140 U58 ( .A1(n111), .A2(n110), .A3(n109), .Z(n113) );
  CKND2D1BWP30P140 U59 ( .A1(b[3]), .A2(a[2]), .ZN(n109) );
  CKND2D1BWP30P140 U60 ( .A1(a[1]), .A2(b[4]), .ZN(n110) );
  CKND2D1BWP30P140 U61 ( .A1(a[0]), .A2(b[5]), .ZN(n111) );
  XOR3UD1BWP30P140 U62 ( .A1(n144), .A2(n143), .A3(n142), .Z(n146) );
  CKND2D1BWP30P140 U63 ( .A1(b[5]), .A2(a[4]), .ZN(n142) );
  CKND2D1BWP30P140 U64 ( .A1(b[6]), .A2(a[3]), .ZN(n143) );
  CKND2D1BWP30P140 U65 ( .A1(b[7]), .A2(a[2]), .ZN(n144) );
  XOR3UD1BWP30P140 U66 ( .A1(n91), .A2(n90), .A3(n89), .Z(y[12]) );
  AN2D1BWP30P140 U67 ( .A1(b[5]), .A2(a[7]), .Z(n89) );
  AN2D1BWP30P140 U68 ( .A1(b[7]), .A2(a[5]), .Z(n90) );
  INR2D1BWP30P140 U69 ( .A1(b[6]), .B1(n156), .ZN(n91) );
  XOR3UD1BWP30P140 U70 ( .A1(n98), .A2(n97), .A3(n96), .Z(y[2]) );
  AN2D1BWP30P140 U71 ( .A1(a[2]), .A2(b[0]), .Z(n96) );
  AN2D1BWP30P140 U72 ( .A1(a[0]), .A2(b[2]), .Z(n97) );
  INR2D1BWP30P140 U73 ( .A1(a[1]), .B1(n149), .ZN(n98) );
  INVD1BWP30P140 U74 ( .I(b[1]), .ZN(n149) );
  XOR2UD1BWP30P140 U75 ( .A1(n133), .A2(n132), .Z(y[7]) );
  XOR4D1BWP30P140 U76 ( .A1(n131), .A2(n130), .A3(n129), .A4(n128), .Z(n132)
         );
  XOR4D1BWP30P140 U77 ( .A1(n127), .A2(n126), .A3(n125), .A4(n124), .Z(n133)
         );
  CKND2D1BWP30P140 U78 ( .A1(b[1]), .A2(a[6]), .ZN(n131) );
  XOR2UD1BWP30P140 U79 ( .A1(n95), .A2(n94), .Z(y[1]) );
  CKND2D1BWP30P140 U80 ( .A1(b[0]), .A2(a[1]), .ZN(n95) );
  CKND2D1BWP30P140 U81 ( .A1(a[0]), .A2(b[1]), .ZN(n94) );
  XOR4D1BWP30P140 U82 ( .A1(n141), .A2(n140), .A3(n139), .A4(n138), .Z(y[8])
         );
  CKND2D1BWP30P140 U83 ( .A1(b[1]), .A2(a[7]), .ZN(n138) );
  CKND2D1BWP30P140 U84 ( .A1(a[6]), .A2(b[2]), .ZN(n139) );
  NR2D1BWP30P140 U85 ( .A1(n155), .A2(n151), .ZN(n140) );
  XOR4D1BWP30P140 U86 ( .A1(n123), .A2(n122), .A3(n121), .A4(n120), .Z(y[6])
         );
  CKND2D1BWP30P140 U87 ( .A1(b[0]), .A2(a[6]), .ZN(n120) );
  CKND2D1BWP30P140 U88 ( .A1(b[1]), .A2(a[5]), .ZN(n121) );
  NR2D1BWP30P140 U89 ( .A1(n154), .A2(n150), .ZN(n122) );
  XOR4D1BWP30P140 U90 ( .A1(n102), .A2(n101), .A3(n100), .A4(n99), .Z(y[3]) );
  CKND2D1BWP30P140 U91 ( .A1(b[1]), .A2(a[2]), .ZN(n102) );
  CKND2D1BWP30P140 U92 ( .A1(a[0]), .A2(b[3]), .ZN(n99) );
  CKND2D1BWP30P140 U93 ( .A1(b[0]), .A2(a[3]), .ZN(n101) );
endmodule

module OKA_8bit_2 ( a, b, y );
  input [7:0] a;
  input [7:0] b;
  output [7:0] y;
  wire   n45, n46, n47, n48, n49, n50, n51, n52, n53, n54, n55, n56, n57, n58,
         n59, n60, n61, n62, n63, n64, n65, n66, n67, n68, n69, n70, n71, n72,
         n73, n74, n75, n76, n77, n78, n79, n80, n81, n82, n83, n84, n85, n86,
         n87, n88;

  XOR2UD1BWP30P140 U1 ( .A1(n54), .A2(n53), .Z(y[0]) );
  XOR4D1BWP30P140 U2 ( .A1(n48), .A2(n47), .A3(n46), .A4(n45), .Z(n54) );
  XOR4D1BWP30P140 U3 ( .A1(n52), .A2(n51), .A3(n50), .A4(n49), .Z(n53) );
  CKND2D1BWP30P140 U4 ( .A1(a[2]), .A2(b[5]), .ZN(n48) );
  XOR4D1BWP30P140 U5 ( .A1(n79), .A2(n78), .A3(n77), .A4(n76), .Z(y[4]) );
  CKND2D1BWP30P140 U6 ( .A1(b[5]), .A2(a[6]), .ZN(n79) );
  CKND2D1BWP30P140 U7 ( .A1(a[4]), .A2(b[7]), .ZN(n76) );
  CKND2D1BWP30P140 U8 ( .A1(b[4]), .A2(a[7]), .ZN(n78) );
  XOR4D1BWP30P140 U9 ( .A1(n69), .A2(n68), .A3(n67), .A4(n66), .Z(y[2]) );
  CKND2D1BWP30P140 U10 ( .A1(b[2]), .A2(a[7]), .ZN(n66) );
  NR2D1BWP30P140 U11 ( .A1(n87), .A2(n86), .ZN(n69) );
  NR2D1BWP30P140 U12 ( .A1(n88), .A2(n85), .ZN(n68) );
  XOR4D1BWP30P140 U13 ( .A1(n62), .A2(n61), .A3(n60), .A4(n59), .Z(y[1]) );
  CKND2D1BWP30P140 U14 ( .A1(b[1]), .A2(a[7]), .ZN(n59) );
  CKND2D1BWP30P140 U15 ( .A1(b[2]), .A2(a[6]), .ZN(n60) );
  NR2D1BWP30P140 U16 ( .A1(n87), .A2(n85), .ZN(n61) );
  XOR4D1BWP30P140 U17 ( .A1(n58), .A2(n57), .A3(n56), .A4(n55), .Z(n62) );
  CKND2D1BWP30P140 U18 ( .A1(a[3]), .A2(b[5]), .ZN(n58) );
  CKND2D1BWP30P140 U19 ( .A1(a[1]), .A2(b[7]), .ZN(n55) );
  CKND2D1BWP30P140 U20 ( .A1(b[4]), .A2(a[4]), .ZN(n57) );
  INVD1BWP30P140 U21 ( .I(a[6]), .ZN(n88) );
  AN2D1BWP30P140 U22 ( .A1(a[7]), .A2(b[7]), .Z(y[7]) );
  INVD1BWP30P140 U23 ( .I(b[4]), .ZN(n86) );
  INVD1BWP30P140 U24 ( .I(b[3]), .ZN(n85) );
  XOR3UD1BWP30P140 U25 ( .A1(n75), .A2(n74), .A3(n73), .Z(y[3]) );
  CKND2D1BWP30P140 U26 ( .A1(b[3]), .A2(a[7]), .ZN(n74) );
  NR2D1BWP30P140 U27 ( .A1(n88), .A2(n86), .ZN(n75) );
  XOR3UD1BWP30P140 U28 ( .A1(n72), .A2(n71), .A3(n70), .Z(n73) );
  XOR3UD1BWP30P140 U29 ( .A1(n65), .A2(n64), .A3(n63), .Z(n67) );
  CKND2D1BWP30P140 U30 ( .A1(a[4]), .A2(b[5]), .ZN(n63) );
  CKND2D1BWP30P140 U31 ( .A1(a[3]), .A2(b[6]), .ZN(n64) );
  CKND2D1BWP30P140 U32 ( .A1(a[2]), .A2(b[7]), .ZN(n65) );
  CKND2D1BWP30P140 U33 ( .A1(a[4]), .A2(b[6]), .ZN(n71) );
  CKND2D1BWP30P140 U34 ( .A1(b[1]), .A2(a[6]), .ZN(n52) );
  XOR2UD1BWP30P140 U35 ( .A1(n84), .A2(n83), .Z(y[6]) );
  CKND2D1BWP30P140 U36 ( .A1(b[6]), .A2(a[7]), .ZN(n84) );
  CKND2D1BWP30P140 U37 ( .A1(a[6]), .A2(b[7]), .ZN(n83) );
  CKND2D1BWP30P140 U38 ( .A1(a[0]), .A2(b[7]), .ZN(n45) );
  CKND2D1BWP30P140 U39 ( .A1(b[2]), .A2(a[5]), .ZN(n49) );
  INVD1BWP30P140 U40 ( .I(a[5]), .ZN(n87) );
  XOR3UD1BWP30P140 U41 ( .A1(n82), .A2(n81), .A3(n80), .Z(y[5]) );
  AN2D1BWP30P140 U42 ( .A1(a[7]), .A2(b[5]), .Z(n80) );
  AN2D1BWP30P140 U43 ( .A1(b[7]), .A2(a[5]), .Z(n81) );
  INR2D1BWP30P140 U44 ( .A1(b[6]), .B1(n88), .ZN(n82) );
  CKND2D1BWP30P140 U45 ( .A1(a[3]), .A2(b[7]), .ZN(n72) );
  CKND2D1BWP30P140 U46 ( .A1(a[3]), .A2(b[4]), .ZN(n47) );
  CKND2D1BWP30P140 U47 ( .A1(b[0]), .A2(a[7]), .ZN(n51) );
  CKND2D1BWP30P140 U48 ( .A1(a[1]), .A2(b[6]), .ZN(n46) );
  CKND2D1BWP30P140 U49 ( .A1(a[2]), .A2(b[6]), .ZN(n56) );
  CKND2D1BWP30P140 U50 ( .A1(a[5]), .A2(b[5]), .ZN(n70) );
  CKND2D1BWP30P140 U51 ( .A1(b[3]), .A2(a[4]), .ZN(n50) );
  CKND2D1BWP30P140 U52 ( .A1(a[5]), .A2(b[6]), .ZN(n77) );
endmodule

