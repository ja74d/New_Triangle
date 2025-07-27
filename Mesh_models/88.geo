// Gmsh project created on Sat Nov  9 21:38:13 2024
SetFactory("OpenCASCADE");
//+
Point(1) = {0, 8, 0, 1.0};
//+
Point(2) = {8, 8, 0, 1.0};
//+
Point(3) = {8, 0, 0, 1.0};
//+
Point(4) = {0, 0, 0, 1.0};
//+
Line(1) = {1, 2};
//+
Line(2) = {2, 3};
//+
Line(3) = {3, 4};
//+
Line(4) = {4, 1};
//+
Physical Curve("Left", 5) = {4};
//+
Physical Curve("Top", 6) = {1};
//+
Physical Curve("Right", 7) = {2};
//+
Physical Curve("Bottom", 8) = {3};
//+
Physical Point("Bottom", 9) = {4, 3};
//+
Physical Point("Left", 10) = {4, 1};
//+
Physical Point("Top", 11) = {1, 2};
//+
Physical Point("Right", 12) = {3, 2};
//+
Curve Loop(1) = {4, 1, 2, 3};
//+
Plane Surface(1) = {1};
//+
Transfinite Surface {1};
//+
Recombine Surface {1};
//+
Transfinite Curve {4, 1, 2, 3} = 65 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 81 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 101 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 33 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 17 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 33 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 17 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 33 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 9 Using Progression 1;
//+
Transfinite Curve {1, 4, 2, 3} = 17 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 65 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 9 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 33 Using Progression 1;
