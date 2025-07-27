// Gmsh project created on Thu Jan  2 10:01:47 2025
SetFactory("OpenCASCADE");
//+
Point(1) = {0, 10, 0, 1.0};
//+
Point(2) = {10, 10, 0, 1.0};
//+
Point(3) = {10, 0, 0, 1.0};
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
Curve Loop(1) = {4, 1, 2, 3};
//+
Plane Surface(1) = {1};
//+
Physical Curve("Left", 5) = {4};
//+
Physical Curve("Top", 6) = {1};
//+
Physical Curve("Right", 7) = {2};
//+
Physical Curve("Bottom", 8) = {3};
//+
Physical Point("Bottom", 9) = {3, 4};
//+
Physical Point("Left", 10) = {4, 1};
//+
Physical Point("Top", 11) = {1, 2};
//+
Physical Point("Right", 12) = {2, 3};
//+
Transfinite Surface {1};
//+
Transfinite Curve {4, 1, 2, 3} = 33 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 65 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 33 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 17 Using Progression 1;
//+
Transfinite Curve {4, 2, 1, 3} = 9 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 3 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 13 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 17 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 34 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 21 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 23 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 26 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 27 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 29 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 31 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 17 Using Progression 1;
