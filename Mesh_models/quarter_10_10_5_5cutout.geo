// Gmsh project created on Sun Jul 27 08:51:33 2025
SetFactory("OpenCASCADE");
//+
Point(1) = {0, 0, 0, 1.0};
//+
Point(2) = {2.5, 0, 0, 1.0};
//+
Point(3) = {2.5, 2.5, 0, 1.0};
//+
Point(4) = {5, 2.5, 0, 1.0};
//+
Point(5) = {5, 5, 0, 1.0};
//+
Point(6) = {0, 5, 0, 1.0};
//+
Line(1) = {6, 5};
//+
Line(2) = {5, 4};
//+
Line(3) = {4, 3};
//+
Line(4) = {3, 2};
//+
Line(5) = {2, 1};
//+
Line(6) = {1, 6};
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
Physical Point("Bottom", 11) = {2, 1};
//+
Physical Point("Left", 12) = {1, 6};
//+
Physical Point("Top", 13) = {6, 5};
//+
Physical Point("Right", 14) = {5, 4};
//+
Transfinite Curve {6, 1, 2, 3, 4, 5} = 21 Using Progression 1;
