#ifndef _DEPTH_H_
#define _DEPTH_H_

#include <Arduino.h>

#define Pressure A0  // pin A0
#define Temp A1  // pin A1

float Read_PT(int PT);

float mapFloat(float x, float in_min, float in_max, float out_min, float out_max);

float psi2feet(float psi);

float feet2psi(float depth);



#endif
