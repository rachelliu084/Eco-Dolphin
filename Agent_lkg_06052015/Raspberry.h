#ifndef _RASPBERRY_H_
#define _RASPBERRY_H_

#include <Arduino.h>
#include <string.h>

#define Raspberry_Data_Width 18  //include '\0' which is the null termination character
#define Raspberry_Baud_Rate 57600

int Read_Serial_0(char *Data);

void Raspberry_Init();

void Raspberry_TX(char *Data);

void Raspberry_RX(char *Data);

void Thruster_Setting(char *Th, int *TH);

#endif
