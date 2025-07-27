// Gmsh project created on Tue Feb 11 18:49:31 2025
SetFactory("OpenCASCADE");
//+
Point(1) = {0, 12.5, 0, 1.0};
//+
Point(2) = {12.5, 12.5, 0, 1.0};
//+
Point(3) = {12.5, 0, 0, 1.0};
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
Transfinite Curve {4, 1, 2, 3} = 21 Using Progression 1;
