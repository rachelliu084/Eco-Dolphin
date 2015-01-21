#ifndef _POWER_H_
#define _POWER_H_

#include <Arduino.h>

#define EN_6 25
#define EN_12 27
#define EN_3V3 29
#define RELAY 12

#define ALL_ON 0x0F
#define ON_25V 0x08
#define ON_12V 0x04
#define ON_6V 0x02
#define ON_3V3 0x01
#define ALL_OFF 0x00

void POWER_ON(int power);

#endif
