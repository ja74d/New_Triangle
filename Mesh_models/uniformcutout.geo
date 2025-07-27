// Gmsh project created on Tue Nov 12 22:02:46 2024
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
Point(6) = {4, 6, 0, 1.0};
//+
Point(7) = {6, 6, 0, 1.0};
//+
Point(8) = {6, 4, 0, 1.0};
//+
Line(1) = {1, 2};
//+
Line(2) = {2, 3};
//+
Line(3) = {3, 4};
//+
Line(4) = {4, 1};
//+
Line(5) = {6, 7};
//+
Line(6) = {7, 8};
//+
Line(7) = {8, 5};
//+
Line(8) = {5, 6};
//+
Line(9) = {1, 6};
//+
Line(10) = {7, 2};
//+
Line(11) = {8, 3};
//+
Line(12) = {5, 4};
//+
Curve Loop(1) = {4, 9, -8, 12};
//+
Plane Surface(1) = {1};
//+
Curve Loop(2) = {1, -10, -5, -9};
//+
Plane Surface(2) = {2};
//+
Curve Loop(3) = {2, -11, -6, 10};
//+
Plane Surface(3) = {3};
//+
Curve Loop(4) = {3, -12, -7, 11};
//+
Plane Surface(4) = {4};
//+
Physical Curve("Left", 13) = {4};
//+
Physical Curve("Top", 14) = {1};
//+
Physical Curve("Right", 15) = {2};
//+
Physical Curve("Bottom", 16) = {3};
//+
Physical Point("Bottom", 17) = {4, 3};
//+
Physical Point("Left", 18) = {4, 1};
//+
Physical Point("Top", 19) = {1, 2};
//+
Physical Point("Right", 20) = {2, 3};
//+
Transfinite Surface {1};
//+
Transfinite Surface {2};
//+
Transfinite Surface {3};
//+
Transfinite Surface {4};
//+
Recombine Surface {1};
//+
Recombine Surface {2};
//+
Recombine Surface {3};
//+
Recombine Surface {4};
//+
Transfinite Curve {4, 1, 2, 3, 8, 5, 6, 7} = 11 Using Progression 1;
//+
Transfinite Curve {9, 10, 11, 12} = 11 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3, 8, 5, 6, 7} = 21 Using Progression 1;
//+
Transfinite Curve {9, 10, 11, 12} = 21 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3, 8, 5, 6, 7} = 41 Using Progression 1;
//+
Transfinite Curve {9, 10, 11, 12} = 21 Using Progression 1;
//+
Transfinite Curve {9, 10, 12, 11} = 41 Using Progression 1;
