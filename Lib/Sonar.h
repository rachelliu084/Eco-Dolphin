#ifndef _SONAR_H_
#define _SONAR_H_

#include <Arduino.h>
#include <string.h>

#define MaxTry 3
#define Data_Width 9

int Read_Serial_3(char *Data);
int Sonar_Init();
void Sonar_Tx(char *TxData);
int Sonar_Rx(char *RxData);

#endif
