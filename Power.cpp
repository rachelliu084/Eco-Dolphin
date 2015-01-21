#include "Power.h"


void POWER_ON(int power)
{
  int t = 1;
  if(t)
  {
    pinMode(EN_6,OUTPUT);
    pinMode(EN_12,OUTPUT);
    pinMode(EN_3V3,OUTPUT);
    pinMode(RELAY,OUTPUT);
    t = 0;
  }
  if((power & ALL_ON) == ALL_ON) //
  {
    digitalWrite(EN_6, LOW);
    digitalWrite(EN_12, LOW);
    digitalWrite(EN_3V3, LOW);
    digitalWrite(RELAY, HIGH);
  }
  if((power & ON_25V) == ON_25V)  digitalWrite(RELAY, HIGH);    
  if((power & ON_12V) == ON_12V)  digitalWrite(EN_12, LOW);
  if((power & ON_6V) == ON_6V)    digitalWrite(EN_6, LOW);
  if((power & ON_3V3) == ON_3V3)  digitalWrite(EN_3V3, LOW);
  if((power & ALL_OFF) == ALL_OFF)
  {
    digitalWrite(EN_6, HIGH);
    digitalWrite(EN_12, HIGH);
    digitalWrite(EN_3V3, HIGH);
    digitalWrite(RELAY, LOW); 
  }
}
