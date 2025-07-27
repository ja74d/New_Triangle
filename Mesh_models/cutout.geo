// Gmsh project created on Sun Nov 10 08:44:12 2024
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
Physical Point("Left", 13) = {4, 1};
//+
Physical Point("Top", 14) = {1, 2};
//+
Physical Point("Right", 15) = {2, 3};
//+
Physical Point("Bottom", 16) = {3, 4};
//+
Transfinite Surface {1};
//+
Recombine Surface {1};
//+
Transfinite Curve {4, 1, 2, 3} = 11 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 3 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 21 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 5 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 26 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 6 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 41 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 9 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 26 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 6 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 21 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 5 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 41 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 9 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 81 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 17 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 6 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 1 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 11 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 3 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 5 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 21 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 41 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 9 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 81 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 17 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 41 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 21 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 11 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 21 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 5 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 41 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 9 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 81 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 17 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 21 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 21 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 41 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 61 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 26 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 46 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 41 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 41 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3, 8, 5, 6, 7} = 21 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 26 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 41 Using Progression 1;
//+
Transfinite Curve {5, 8, 7, 6} = 41 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3, 6, 5, 8, 7} = 41 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3, 8, 5, 6, 7} = 26 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 41 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 26 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 41 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 21 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 21 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 11 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 21 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 11 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 21 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 21 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 41 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 81 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 41 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 51 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 26 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 21 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 11 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 41 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 21 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 11 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 6 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 51 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 26 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 11 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 6 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 64 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 32 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 16 Using Progression 1;
//+
Transfinite Curve {8, 5, 6, 7} = 9 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 17 Using Progression 1;
//+
Recombine Surface {1};
