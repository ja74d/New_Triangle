// Gmsh project created on Sun Jan  5 08:55:32 2025
SetFactory("OpenCASCADE");
//+
Point(1) = {0, 5, 0, 1.0};
//+
Point(2) = {5, 5, 0, 1.0};
//+
Point(3) = {5, 1, 0, 1.0};
//+
Point(4) = {4, 1, 0, 1.0};
//+
Point(5) = {4, 0, 0, 1.0};
//+
Point(6) = {0, 0, 0, 1.0};
//+
Line(1) = {1, 2};
//+
Line(2) = {2, 3};
//+
Line(3) = {3, 4};
//+
Line(4) = {4, 5};
//+
Line(5) = {5, 6};
//+
Line(6) = {6, 1};
//+
Curve Loop(1) = {6, 1, 2, 3, 4, 5};
//+
Plane Surface(1) = {1};
//+
Physical Curve("Left", 7) = {6};
//+
Physical Curve("Top", 8) = {1};
//+
Physical Curve("Right", 9) = {2};
//+
Physical Curve("Bottom", 10) = {5};
//+
Physical Point("Bottom", 11) = {6, 5};
//+
Physical Point("Left", 12) = {6, 1};
//+
Physical Point("Top", 13) = {1, 2};
//+
Physical Point("Right", 14) = {2, 3};
//+
Transfinite Surface {1};
//+
Transfinite Surface {1};
//+
Transfinite Curve {6, 1, 2, 5} = 9 Using Progression 1;
//+
Transfinite Curve {3, 4} = 5 Using Progression 1;
