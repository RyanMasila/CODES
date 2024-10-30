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
  screen(400, 300, 0, "Movable Circle");
  float x = w / 2, y = h / 2; //the position of the circle; initially set it to the center of the screen
  float time, oldTime; //the time of the current and previous loop
  while(!done())
  {
    //set the old time to the time of the previous loop
    oldTime = time;
    waitFrame(oldTime, 0.05);
    time = getTime(); //get the time since program start
    readKeys(); //get the current keystate

    //if an arrow key is pressed, move the circle in its direction at a speed of 50 pixels/second
    if(keyDown(SDLK_RIGHT)) { x += (time - oldTime) / 20.0; }
    if(keyDown(SDLK_LEFT)) { x -= (time - oldTime) / 20.0; }
    if(keyDown(SDLK_UP)) { y -= (time - oldTime) / 20.0; }
    if(keyDown(SDLK_DOWN)) { y += (time - oldTime) / 20.0; }
    drawDisk(int(x), int(y), 20, RGB_Gray); //draw a grey circle with radius 20 pixels at the position of the ball
    redraw();
    cls(); //clear the screen so the old position of the ball becomes black again
  }
}
