#ifndef _BUZZER_H_
#define _BUZZER_H_

#include <Arduino.h>


#define BUZZER  8// pin 8

#define Buzzer_ON  1
#define Buzzer_OFF  0

void Buzzer(int x);

void Buzzer_Init();

void Buzzer_3x500ms();

#endif
