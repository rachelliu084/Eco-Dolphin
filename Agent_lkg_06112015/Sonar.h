#ifndef _SONAR_H_
#define _SONAR_H_

#include <Arduino.h>
#include <string.h>

#define MaxTry 3
#define Sonar_Data_Width 9  //include '\0' which is the null termination character
#define Soanr_Baud_Rate 57600

int Read_Serial_1(char *Data);

int Sonar_Init();

void Sonar_Tx(char *TxData);

int Sonar_Rx(char *RxData);

#endif
