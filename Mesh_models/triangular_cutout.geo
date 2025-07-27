// Gmsh project created on Tue Nov 26 22:46:18 2024
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
Point(5) = {4, 4, 0, 1.0};
//+
Point(6) = {6, 4, 0, 1.0};
//+
Point(7) = {5, 6, 0, 1.0};
//+
Line(1) = {1, 2};
//+
Line(2) = {2, 3};
//+
Line(3) = {3, 4};
//+
Line(4) = {4, 1};
//+
Line(5) = {5, 7};
//+
Line(6) = {7, 6};
//+
Line(7) = {6, 5};
//+
Curve Loop(1) = {4, 1, 2, 3};
//+
Curve Loop(2) = {5, 6, 7};
//+
Plane Surface(1) = {1, 2};
//+
Physical Curve("Left", 8) = {4};
//+
Physical Curve("Top", 9) = {1};
//+
Physical Curve("Right", 10) = {2};
//+
Physical Curve("Bottom", 11) = {3};
//+
Physical Point("Bottom", 12) = {4, 3};
//+
Physical Point("Left", 13) = {4, 1};
//+
Physical Point("Top", 14) = {1, 2};
//+
Physical Point("Right", 15) = {2, 3};
//+
Transfinite Surface {1};
//+
Recombine Surface {1};
//+
Field[1] = Cylinder;
//+
Compound Curve {5};
//+
Compound Curve {6, 7};
//+
Compound Curve {5};
