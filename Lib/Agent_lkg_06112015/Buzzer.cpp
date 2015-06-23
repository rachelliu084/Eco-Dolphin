#include "Buzzer.h"

void Buzzer_Init()
{
  pinMode(BUZZER, OUTPUT);
}

void Buzzer(int x)//switch of buzzer 1=ON, 0=OFF
{
  if(x == 1) digitalWrite(BUZZER, HIGH);
  else digitalWrite(BUZZER, LOW);
}

void Buzzer_3x500ms()
{
  for(int i = 0; i < 3; i++)
  {
    Buzzer(Buzzer_ON);
    delay(100);
    Buzzer(Buzzer_OFF);
    delay(500);
  }
}
