// Gmsh project created on Sat Mar  1 10:12:31 2025
SetFactory("OpenCASCADE");
//+
Point(1) = {0, 0, 0, 1.0};
//+
Point(2) = {4, 0, 0, 1.0};
//+
Point(3) = {5, 0, 0, 1.0};
//+
Point(4) = {5, 1, 0, 1.0};
//+
Point(5) = {5, 5, 0, 1.0};
//+
Point(6) = {0, 5, 0, 1.0};
//+
Line(1) = {6, 5};
//+
Line(2) = {5, 4};
//+
Line(3) = {6, 1};
//+
Line(4) = {1, 2};
//+
Circle(5) = {2, 3, 4};
//+
Recursive Delete {
  Point{3}; 
}
//+
Curve Loop(1) = {3, 4, 5, -2, -1};
//+
Plane Surface(1) = {1};
//+
Physical Curve("Left", 6) = {3};
//+
Physical Curve("Top", 7) = {1};
//+
Physical Curve("Right", 8) = {2};
//+
Physical Curve("Bottom", 9) = {4};
//+
Physical Point("Bottom", 10) = {2, 1};
//+
Physical Point("Left", 11) = {1, 6};
//+
Physical Point("Top", 12) = {6, 5};
//+
Physical Point("Right", 13) = {5, 4};
//+
Transfinite Surface {1};
//+
Transfinite Curve {4, 3, 1, 2} = 21 Using Progression 1;
//+
Transfinite Curve {5} = 11 Using Progression 1;
//+
Transfinite Curve {5} = 16 Using Progression 1;
//+
Transfinite Curve {5} = 11 Using Progression 1;
//+
Transfinite Surface {1};
