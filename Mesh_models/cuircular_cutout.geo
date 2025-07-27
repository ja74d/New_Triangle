// Gmsh project created on Sun Nov 17 14:32:25 2024
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
Point(5) = {5, 5, 0, 1.0};
//+
Point(6) = {5, 6, 0, 1.0};
//+
Point(7) = {5, 4, 0, 1.0};
//+
Point(8) = {4, 5, 0, 1.0};
//+
Point(9) = {6, 5, 0, 1.0};
//+
Line(1) = {1, 2};
//+
Line(2) = {2, 3};
//+
Line(3) = {3, 4};
//+
Line(4) = {4, 1};
//+
Circle(5) = {8, 5, 6};
//+
Circle(6) = {6, 5, 9};
//+
Circle(7) = {9, 5, 7};
//+
Circle(8) = {7, 5, 8};
//+
Curve Loop(1) = {4, 1, 2, 3};
//+
Curve Loop(2) = {5, 6, 7, 8};
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
Physical Point("Left", 14) += {4, 1};
//+
Physical Point("Top", 13) = {1, 2};
//+
Physical Point("Right", 14) = {2, 3};
//+
Transfinite Surface {1};
//+
Recombine Surface {1};
//+
Transfinite Curve {4, 1, 2, 3} = 17 Using Progression 1;
//+
Transfinite Curve {5, 6, 7, 8} = 5 Using Progression 1;
//+
Transfinite Curve {4, 1, 1, 2, 3, 7, 6, 5, 8} = 3 Using Progression 1;
