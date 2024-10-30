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

int main(int /*argc*/, char */*argv*/[])
{
  screen(256, 256, 1, "A Face!");
  drawDisk(128, 128, 100, ColorRGB(255, 128, 200));
  drawDisk(88, 100, 10, ColorRGB(0, 0, 255));
  drawDisk(168, 100, 10, ColorRGB(0, 0, 255));
  drawLine(88, 150, 168, 150, ColorRGB(255, 0, 0));

  redraw();
  sleep();
}
