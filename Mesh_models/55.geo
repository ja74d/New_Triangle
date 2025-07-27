// Gmsh project created on Thu Jan  2 09:45:06 2025
SetFactory("OpenCASCADE");
//+
Point(1) = {0, 5, 0, 1.0};
//+
Point(2) = {5, 5, 0, 1.0};
//+
Point(3) = {5, 0, 0, 1.0};
//+
Point(4) = {0, 0, 0, 1.0};
//+
Line(1) = {1, 2};
//+
Line(2) = {2, 3};
//+
Line(3) = {3, 4};
//+
Line(4) = {4, 1};
//+
Curve Loop(1) = {4, 1, 2, 3};
//+
Plane Surface(1) = {1};
//+
Physical Curve("Right", 5) = {2};
//+
Physical Curve("Bottom", 6) = {3};
//+
Physical Curve("Left", 7) = {4};
//+
Physical Curve("Top", 8) = {1};
//+
Physical Point("Top", 9) = {1, 2};
//+
Physical Point("Right", 10) = {2, 3};
//+
Physical Point("Bottom", 11) = {3, 4};
//+
Physical Point("Left", 12) = {4, 1};
//+
Transfinite Surface {1};
//+
Transfinite Curve {4, 1, 2, 3} = 65 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 3 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 5 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 9 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 17 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 33 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 17 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 17 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 21 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 25 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 21 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 2 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 3 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = ۴ Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 4 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 5 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 6 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 7 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 8 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 9 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 10 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 11 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 12 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 13 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 14 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 15 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 16 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 17 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 18 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 19 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 20 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 21 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 3 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 4 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 5 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 6 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 7 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 8 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 9 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 10 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 11 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 12 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 13 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 14 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 15 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 16 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 17 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 18 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 19 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 20 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 21 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 3 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 5 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 9 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 17 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 17 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 31 Using Progression 1;
//+
Transfinite Curve {4, 1, 2, 3} = 17 Using Progression 1;
