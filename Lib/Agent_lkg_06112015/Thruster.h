#ifndef _THRUSTER_H_
#define _THRUSTER_H_

#include <Arduino.h>
#include <Servo.h>

#define MOTOR1_PIN 4   //1
#define MOTOR2_PIN 6   // 2
#define MOTOR3_PIN 8   // 3
#define MOTOR4_PIN 10  // 4

#define IDLE 1500
#define Thruster1  1550 //red
#define Thruster2  1610 //blue
#define Thruster3  1600 //lime green
#define Thruster4  1390 // orange
#define Reverse1 1390
#define Reverse2 1390

void Thruster_Speed(int *TH);

void Thruster_Stop();

int Thruster_Init();

#endif
