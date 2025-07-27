// Gmsh project created on Sun Nov 10 14:51:48 2024
SetFactory("OpenCASCADE");
//+
Point(1) = {0, 3, 0, 1.0};
//+
Point(2) = {3, 3, 0, 1.0};
//+
Point(3) = {3, 0, 0, 1.0};
//+
Point(4) = {0, 0, 0, 1.0};
//+
Point(5) = {1, 1, 0, 1.0};
//+
Point(6) = {2, 1, 0, 1.0};
//+
Point(7) = {2, 2, 0, 1.0};
//+
Point(8) = {1, 2, 0, 1.0};
//+
Line(1) = {1, 2};
//+
Line(2) = {2, 3};
//+
Line(3) = {3, 4};
//+
Line(4) = {4, 1};
//+
Line(5) = {8, 7};
//+
Line(6) = {7, 6};
//+
Line(7) = {6, 5};
//+
Line(8) = {5, 8};
//+
Curve Loop(1) = {4, 1, 2, 3};
//+
Curve Loop(2) = {8, 5, 6, 7};
//+
Plane Surface(1) = {1, 2};
//+
Physical Curve("Left", 9) = {4};
//+
Physical Curve("Top", 10) = {1};
//+
Physical Curve("Right", 11) = {2};
//+
Physical Curve("Bottom", 12) = {3};
//+
Physical Point("Bottom", 13) = {4, 3};
//+
Physical Point("Left", 14) = {4, 1};
//+
Physical Point("Top", 15) = {1, 2};
//+
Physical Point("Right", 16) = {2, 3};
//+
Transfinite Surface {1};
//+
Recombine Surface {1};
//+
Transfinite Curve {4, 1, 2, 3} = 4 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 2 Using Progression 1;
