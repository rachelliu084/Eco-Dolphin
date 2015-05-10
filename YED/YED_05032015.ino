#include "Buzzer.h"
#include "Depth.h"
#include "Power.h"
#include "Sonar.h"
#include "SparkFunIMU.h"
#include "Thruster.h"
#include "Raspberry.h"
#include <Servo.h>
#include <String.h>

/*---------------------Status Word-----------------------*/
char Data_Raspberry[Raspberry_Data_Width];
char Data_Sonar[Sonar_Data_Width];
char x[8], y[8], z[8];
int TH[5] = {1500, 1500, 1500 ,1500 , 0};

/*---------------------Status Word-----------------------*/
int Th_PWR = 0;

/*---------------------Status Command-----------------------*/
char Ready[] = "Ready";
char Th_Set[] = "Th_Set";


void setup()
{
  Raspberry_Init();
  Buzzer_Init();
  Power_Init();
  SparkFun_IMU_Init();
  Sonar_Init();
//  Thruster_Init();
}

void loop()
{
  strcpy(Data_Raspberry, "");// clear command
  Raspberry_RX(Data_Raspberry);// wait until get the next command
  if(Data_Raspberry == "PowerOn")
  {
    strcpy(Data_Raspberry, "");
    if(Th_PWR == 0) { Th_PWR = Thruster_PWR(Thruster_ON); Thruster_Init(); Buzzer_3x500ms(); }
    Thruster_Stop();
    Raspberry_TX(Ready);
    Raspberry_RX(Data_Raspberry);
    if(Data_Raspberry == "Accel-x")  { IMU_Data(Accel, x, y, z); Raspberry_TX(x); }
    else if(Data_Raspberry == "Accel-y") { IMU_Data(Accel, x, y, z); Raspberry_TX(y); }
        else if(Data_Raspberry == "Accel-z") { IMU_Data(Accel, x, y, z); Raspberry_TX(z); }
            else if(Data_Raspberry == "Gyro-x") { IMU_Data(Gyro, x, y, z); Raspberry_TX(x); }
                else if(Data_Raspberry == "Gyro-y") { IMU_Data(Gyro, x, y, z); Raspberry_TX(y); }
                    else if(Data_Raspberry == "Gyro-z") { IMU_Data(Gyro, x, y, z); Raspberry_TX(x); }            
  }
  else if(Data_Raspberry == "Motion")
      {
        strcpy(Data_Raspberry, "");
        if(Th_PWR == 0) { Th_PWR = Thruster_PWR(Thruster_ON); Thruster_Init(); Buzzer_3x500ms(); }
        Raspberry_TX(Ready);
        Raspberry_RX(Data_Raspberry);
        if(Data_Raspberry == "Accel-x")  { IMU_Data(Accel, x, y, z); Raspberry_TX(x); }
        else if(Data_Raspberry == "Accel-y") { IMU_Data(Accel, x, y, z); Raspberry_TX(y); }
            else if(Data_Raspberry == "Accel-z") { IMU_Data(Accel, x, y, z); Raspberry_TX(z); }
                else if(Data_Raspberry == "Gyro-x") { IMU_Data(Gyro, x, y, z); Raspberry_TX(x); }
                    else if(Data_Raspberry == "Gyro-y") { IMU_Data(Gyro, x, y, z); Raspberry_TX(y); }
                        else if(Data_Raspberry == "Gyro-z") { IMU_Data(Gyro, x, y, z); Raspberry_TX(x); }
     // delay(100);
        Raspberry_TX(Th_Set);
        Raspberry_RX(Data_Raspberry);
        Thruster_Setting(Data_Raspberry, TH);
        Thruster_Speed(TH);
      }
      else if(Data_Raspberry == "PowerOFF")
          {
            Th_PWR = Thruster_PWR(Thruster_OFF);
          }
          else Raspberry_TX("Wrong Command!");                
    
}

