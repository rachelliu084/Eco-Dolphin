#ifndef _THRUSTER_H_
#define _THRUSTER_H_

#include <Arduino.h>
#include <Servo.h>

#define MOTOR1_PIN 4
#define MOTOR2_PIN 6
#define MOTOR3_PIN 8
#define MOTOR4_PIN 10

#define IDLE 1500
#define Thruster1  1550
#define Thruster2  1610
#define Thruster3  1600
#define Thruster4  1390
#define Reverse1 1390
#define Reverse2 1390

void Thruster_Speed(int *TH);

void Thruster_Stop();

int Thruster_Init();

#endif
