#include "Relay.h"
#include <string.h>
#include <Servo.h>
#include "Sonar.h"
#include "Thruster.h"
//#include "Depth.h"

#define ON 1
#define OFF 0

int Flag_Serial = 0;
int SonarInit = 0;

int THSL[5] = {1530,1530,1500,1500,15000};// assume 1 feet per second
int THLL[5] = {1500,1530,1500,1500,7000};
int THRL[5] = {1530,1500,1500,1500,7000};

int THSM[5] = {1550,1550,1500,1500,7500};// assume 2 feet per second
int THLM[5] = {1500,1550,1500,1500,6000};// assume 
int THRM[5] = {1550,1500,1500,1500,6000};

int THSH[5] = {1570,1570,1500,1500,5000};// assume 3 feet per second
int THLH[5] = {1500,1570,1500,1500,5000};
int THRH[5] = {1570,1500,1500,1500,5000};


char Data_Sonar_String[6];

void setup()
{
//  Serial.begin(4800);
//  Relay(ON);
  Thruster_Init();
//  Serial.println("a1");
  Thruster_Stop();
//    Serial.println("a2");
//  SonarInit = Sonar_Init();
//  Serial.println("a5");
// Thruster_Speed(THU); 
}

void loop()
{
 /* Serial.println("a2");
  Relay(ON);
  digitalWrite(11, HIGH);
  delay(2000);
  Serial.println("a5");
  Relay(OFF);
  digitalWrite(11, LOW);
  delay(2000);*/
//  Sonar_Rx(Data_Sonar_String);
//  if(strcmp(Data_Sonar_String,"L2") == 0)
  {
    for(int i=0; i < 4; i++)
    {
      Thruster_Speed(THSL);
      Thruster_Speed(THLL);
    }
    Thruster_Stop();
  }
  delay(10000);
//  if(strcmp(Data_Sonar_String,"L1") == 0)
  {
    Thruster_Speed(THLL);//change heading first
    for(int i=0; i < 4; i++)
    {
      Thruster_Speed(THSL);
      Thruster_Speed(THRL);
    }
    Thruster_Stop();
  }
  delay(10000);
//  if(strcmp(Data_Sonar_String,"M2") == 0)
  {
    for(int i=0; i < 4; i++)
    {
      Thruster_Speed(THSM);
      Thruster_Speed(THLM);
    }
    Thruster_Stop();
  }
  delay(10000);
//  if(strcmp(Data_Sonar_String,"M1") == 0)
  {
    Thruster_Speed(THLM);//change heading first
    for(int i=0; i < 4; i++)
    {
      Thruster_Speed(THSM);
      Thruster_Speed(THRM);
    }
    Thruster_Stop();
  }  
  delay(10000);
//    if(strcmp(Data_Sonar_String,"H2") == 0)
  {
    for(int i=0; i < 4; i++)
    {
      Thruster_Speed(THSH);
      Thruster_Speed(THLH);
    }
    Thruster_Stop();
  }
  delay(10000);
//  if(strcmp(Data_Sonar_String,"H1") == 0)
  {
    Thruster_Speed(THLH);//change heading first
    for(int i=0; i < 4; i++)
    {
      Thruster_Speed(THSH);
      Thruster_Speed(THRH);
    }
    Thruster_Stop();
  }
  delay(10000);
//  strcpy(Data_Sonar_String,"");
  
}
