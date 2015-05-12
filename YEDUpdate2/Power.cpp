#include "Power.h"

void Power_Init()//Initilize the control pin
{
  pinMode(RELAY,OUTPUT);
}


int Thruster_PWR(int x)//switch of 25V 1=ON, 0=OFF
{
  if(x == 1) 
  { 
    digitalWrite(RELAY, HIGH); 
    return 1;
  }
  else 
  {
    digitalWrite(RELAY, LOW);
    return 0;
  }
}
