// Gmsh project created on Tue Feb 25 10:18:01 2025
SetFactory("OpenCASCADE");
//+
Point(1) = {0, 0, 0, 1.0};
//+
Point(2) = {10, 0, 0, 1.0};
//+
Point(3) = {10, 5, 0, 1.0};
//+
Point(4) = {0, 5, 0, 1.0};
//+
Line(1) = {4, 3};
//+
Line(2) = {3, 2};
//+
Line(3) = {2, 1};
//+
Line(4) = {1, 4};
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
Physical Point("Bottom", 9) = {2, 1};
//+
Physical Point("Left", 10) = {1, 4};
//+
Physical Point("Top", 11) = {4, 3};
//+
Physical Point("Right", 12) = {3, 2};
//+
Transfinite Surface {1};
//+
Transfinite Curve {4, 1, 2, 3} = 21 Using Progression 1;
