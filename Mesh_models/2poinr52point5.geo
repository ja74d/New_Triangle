// Gmsh project created on Tue Jun  3 09:31:06 2025
SetFactory("OpenCASCADE");
//+
Point(1) = {0, 0, 0, 1.0};
//+
Point(2) = {0, 2.5, 0, 1.0};
//+
Point(3) = {2.5, 2.5, 0, 1.0};
//+
Point(4) = {2.5, 0, 0, 1.0};
//+
Line(1) = {2, 3};
//+
Line(2) = {3, 4};
//+
Line(3) = {4, 1};
//+
Line(4) = {1, 2};
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
Physical Point("Bottom", 9) = {4, 1};
//+
Physical Point("Left", 10) = {1, 2};
//+
Physical Point("Top", 11) = {2, 3};
//+
Physical Point("Right", 12) = {3, 4};
//+
Transfinite Surface {1};
//+
Transfinite Curve {4, 1, 2, 3} = 17 Using Progression 1;
