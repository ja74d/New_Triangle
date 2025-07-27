// Gmsh project created on Tue Nov 26 23:59:42 2024
SetFactory("OpenCASCADE");
//+
Point(1) = {10, 0, 0, 1.0};
//+
Point(2) = {10, 10, 0, 1.0};
//+
Point(3) = {0, 10, 0, 1.0};
//+
Point(4) = {0, 0, 0, 1.0};
//+
Point(5) = {5, 5, 0, 1.0};
//+
Circle(1) = {5, 5, 0, 0.5, 0, 2*Pi};
//+
Line(2) = {3, 2};
//+
Line(3) = {2, 1};
//+
Line(4) = {1, 4};
//+
Line(5) = {4, 3};
//+
Curve Loop(1) = {5, 2, 3, 4};
//+
Curve Loop(2) = {1};
//+
Plane Surface(1) = {1, 2};
//+
Physical Curve("Left", 6) = {5};
//+
Physical Curve("Top", 7) = {2};
//+
Physical Curve("Right", 8) = {3};
//+
Physical Curve("Bottom", 9) = {4};
//+
Physical Point("Bottom", 10) = {4, 1};
//+
Physical Point("Left", 11) = {4, 3};
//+
Physical Point("Top", 12) = {3, 2};
//+
Physical Point("Right", 13) = {2, 1};
//+
Transfinite Surface {1};
//+
Recombine Surface {1};
//+
Transfinite Curve {5, 2, 3, 4} = 3 Using Progression 1;
//+
Transfinite Curve {1} = 9 Using Progression 1;
