#include "Thruster.h"
#include <Servo.h>

Servo motor1;
Servo motor2;
Servo motor3;
Servo motor4;


void Thruster_Speed(int *TH)
{
  motor1.writeMicroseconds(TH[0]);
  motor2.writeMicroseconds(TH[1]);
  motor3.writeMicroseconds(TH[2]);
  motor4.writeMicroseconds(TH[3]);
  delay(TH[4]);
}

void Thruster_Stop()
{
  motor1.writeMicroseconds(MID_SIGNAL);
  motor2.writeMicroseconds(MID_SIGNAL);
  motor3.writeMicroseconds(MID_SIGNAL);
  motor4.writeMicroseconds(MID_SIGNAL);   

}
