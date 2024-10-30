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
  screen(512, 256, 0, "HSL versus HSV");
  ColorRGB color;

  for(int x = 0; x < 256; x++)
  for(int y = 0; y < h; y++)
  {
    color = HSLtoRGB(ColorHSL(x, 255, y)); //convert the colr "hue=x, saturation=255, lightness=y" to RGB
    pset(x, y, color); //plot a pixel from the HSL model
    color = HSVtoRGB(ColorHSV(x, 255, y)); //convert the color "hue=x, saturation=255, value=y" to RGB
    pset(x + 256, y, color); //plot a pixel from the HSV model
  }
  redraw();
  sleep();
}
