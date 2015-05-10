#ifndef _POWER_H_
#define _POWER_H_

#include <Arduino.h>


#define RELAY 12//pin 12

#define Thruster_ON	1
#define Thruster_OFF	0

int Thruster_PWR(int x);

void Power_Init();//Initilize the control pin

#endif
