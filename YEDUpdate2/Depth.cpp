#include "Depth.h"

float Read_PT(int PT)
{
  // make 16 readings and average them (reduces some noise) you can tune the number 16 of course
  float val;
  int count = 16, raw = 0, sensorValue = 0;
  for(int i = 0; i< count; i++)
  {
    if(PT) 
    {
      sensorValue = analogRead(Pressure);
      raw += sensorValue;
    }
    else 
    {
      sensorValue = analogRead(Temp);
      raw += sensorValue;
    }
  }
  raw = raw / count; // return 0..1023 representing 0..5V
  float voltage = 5.0 * raw / 1023; //CONVERT TO VOLTAGE voltage = 0..5V;  we do the math in millivolts!!
//  Serial.print(voltage);
//  Serial.println();
  if(PT)  val = mapFloat(voltage, 0.88, 4.4, 0, 50);  // Pressure
  else  val = mapFloat(voltage, 0.88, 4.4, 32, 135);  // Temperature
  return val;
}


float mapFloat(float x, float in_min, float in_max, float out_min, float out_max)
{
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

float psi2feet(float psi)
{
  int feet;
  feet = (psi-14.6959)*6894.75729/(1027*9.8*0.3048);
  return feet;  

}

float feet2psi(float depth) //feet
{
  int psi;
  psi = 1027*9.8*depth*0.3048/6894.75729+14.5;
  return psi;
}
