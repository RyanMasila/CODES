/*
Copyright (c) 2004, Lode Vandevenne
All rights reserved.
*/

#include <cmath>
#include <string>
#include <vector>
#include <iostream>

#include "quickcg.h"
using namespace QuickCG;
using namespace std;

//place the example code below here:

int main(int argc, char *argv[])
{
  screen(400, 300, 0, "2D primitives");
  int x1, y1, x2, y2; //The initial line, too big for the screen
  int x3, y3, x4, y4; //Will become the clipped line
  x1 = -50; //This is outside the string
  y1 = -20; //This will be outside the string
  x2 = 1000; //This is outside the string
  y2 = 1200; //This is outside the string
  clipLine(x1, y1, x2, y2, x3, y3, x4, y4);//the new line represents the part of the old line that is visible on the screen
  drawLine(x3, y3, x4, y4, RGB_Red); //The new line is drawn as a red line
  drawCircle(100, 100, 30, RGB_Green); //a green unfilled circle
  drawDisk(200, 100, 20, RGB_Yellow); //a yellow filled circle
  drawRect(150, 150, 200, 200, RGB_Cyan); //a cyan square
  redraw(); //make it visible
  sleep(); //pause
}
