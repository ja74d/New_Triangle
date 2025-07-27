// Gmsh project created on Wed Nov 13 11:14:02 2024
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
Point(5) = {4, 4, 0, 1.0};
//+
Point(6) = {4, 6, 0, 1.0};
//+
Point(7) = {6, 6, 0, 1.0};
//+
Point(8) = {6, 4, 0, 1.0};
//+
Point(9) = {2.5, 2.5, 0, 1.0};
//+
Point(10) = {2.5, 7.5, 0, 1.0};
//+
Point(11) = {7.5, 7.5, 0, 1.0};
//+
Point(12) = {7.5, 2.5, 0, 1.0};
//+
Line(1) = {3, 2};
//+
Line(2) = {2, 1};
//+
Line(3) = {1, 4};
//+
Line(4) = {4, 3};
//+
Line(5) = {6, 7};
//+
Line(6) = {7, 8};
//+
Line(7) = {8, 5};
//+
Line(8) = {5, 6};
//+
Line(9) = {10, 11};
//+
Line(10) = {11, 12};
//+
Line(11) = {12, 9};
//+
Line(12) = {9, 10};
//+
Curve Loop(1) = {4, 1, 2, 3};
//+
Curve Loop(2) = {12, 9, 10, 11};
//+
Plane Surface(1) = {1, 2};
//+
Curve Loop(3) = {12, 9, 10, 11};
//+
Curve Loop(4) = {8, 5, 6, 7};
//+
Plane Surface(2) = {3, 4};
//+
Physical Curve("Left", 13) = {4};
//+
Physical Curve("Top", 14) = {1};
//+
Physical Curve("Right", 15) = {2};
//+
Physical Curve("Bottom", 16) = {3};
//+
Physical Point("Bottom", 17) = {4, 1};
//+
Physical Point("Left", 18) = {4, 3};
//+
Physical Point("Top", 19) = {3, 2};
//+
Physical Point("Right", 20) = {2, 1};
//+
Physical Point("Top", 19) += {3, 2};
//+
Physical Point("Right", 20) += {2, 1};
//+
Transfinite Surface {1};
//+
Transfinite Surface {2};
//+
Recombine Surface {1};
//+
Recombine Surface {2};
//+
Transfinite Curve {4, 1, 2, 3} = 21 Using Progression 1;
//+
Transfinite Curve {12, 9, 10, 11} = 11 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 11 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 21 Using Progression 1;
//+
Transfinite Curve {12, 9, 10, 11} = 11 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 21 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3, 4} = 41 Using Progression 1;
//+
Transfinite Curve {12, 9, 10, 11} = 21 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 21 Using Progression 1;
