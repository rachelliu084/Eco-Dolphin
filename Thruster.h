#ifndef _THRUSTER_H_
#define _THRUSTER_H_

#include <Arduino.h>
#include <Servo.h>

#define MOTOR1_PIN 4
#define MOTOR2_PIN 6
#define MOTOR3_PIN 8
#define MOTOR4_PIN 10

#define MID_SIGNAL 1500

void Thruster_Speed(int *TH);
void Thruster_Stop();

#endif
