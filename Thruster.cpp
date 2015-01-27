#include "Thruster.h"

void Thruster_Init()
{
  //Serial.println("0");
  motor1.attach(MOTOR1_PIN);
  motor2.attach(MOTOR2_PIN);
  motor3.attach(MOTOR3_PIN);
  motor4.attach(MOTOR4_PIN);
  
  motor1.writeMicroseconds(MID_SIGNAL);
  motor2.writeMicroseconds(MID_SIGNAL);
  motor3.writeMicroseconds(MID_SIGNAL);
  motor4.writeMicroseconds(MID_SIGNAL);
  delay(10000);
}

void Thruster_Speed(int *TH)
{
  motor1.writeMicroseconds(TH[0]);
//  Serial.println("1");
  motor2.writeMicroseconds(TH[1]);
//  Serial.println("2");
  motor3.writeMicroseconds(TH[2]);
//  Serial.println("3");
  motor4.writeMicroseconds(TH[3]);
//  Serial.println("4");
  delay(TH[4]);
  
  
}

void Thruster_Stop()
{
  motor1.writeMicroseconds(MID_SIGNAL);
  motor2.writeMicroseconds(MID_SIGNAL);
  motor3.writeMicroseconds(MID_SIGNAL);
  motor4.writeMicroseconds(MID_SIGNAL);   

}
