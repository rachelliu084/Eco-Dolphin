#include "Servos.h"
#include <Servo.h>

Servo Servo1;
Servo Servo2;
Servo Servo3;
Servo Servo4;


void Servo_Angle(int *servo)
{
  Servo1.writeMicroseconds(servo[0]);
  Servo2.writeMicroseconds(servo[1]);
  Servo3.writeMicroseconds(servo[2]);
  Servo4.writeMicroseconds(servo[3]);
}
