#include "Buzzer.h"
#include "Depth.h"
#include "Power.h"
#include "Sonar.h"
#include "SparkFunIMU.h"
#include "Thruster.h"
#include "Raspberry.h"
#include <Servo.h>
#include <string.h>

/*---------------------Status Word-----------------------*/
char Data_Raspberry[Raspberry_Data_Width];
char Data_Sonar[Sonar_Data_Width];
char x[8], y[8], z[8];
int TH[4] = {1500, 1500, 1500 ,1500};// Last one TH[4] is time, 0-99s

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
  if(strcmp(Data_Raspberry, "PowerOn")==0)
  {
    strcpy(Data_Raspberry, "");
    if(Th_PWR == 0) { Th_PWR = Thruster_PWR(Thruster_ON); Thruster_Init(); Buzzer_3x500ms(); }
    Thruster_Stop();
    Raspberry_TX(Ready);
    Raspberry_RX(Data_Raspberry);
    if(strcmp(Data_Raspberry, "Accelx")==0)  { IMU_Data(Accel, x, y, z); Raspberry_TX(x); }
    else if(strcmp(Data_Raspberry, "Accely")==0) { IMU_Data(Accel, x, y, z); Raspberry_TX(y); }
        else if(strcmp(Data_Raspberry, "Accelz")==0) { IMU_Data(Accel, x, y, z); Raspberry_TX(z); }
            else if(strcmp(Data_Raspberry, "Gyrox")==0) { IMU_Data(Gyro, x, y, z); Raspberry_TX(x); }
                else if(strcmp(Data_Raspberry, "Gyroy")==0) { IMU_Data(Gyro, x, y, z); Raspberry_TX(y); }
                    else if(strcmp(Data_Raspberry, "Gyroz")==0) { IMU_Data(Gyro, x, y, z); Raspberry_TX(x); }            
  }
  else if(strcmp(Data_Raspberry,"Motion")==0)
      {
        strcpy(Data_Raspberry, "");
        if(Th_PWR == 0) { Th_PWR = Thruster_PWR(Thruster_ON); Thruster_Init(); Buzzer_3x500ms(); }
        Raspberry_TX(Ready);
        Raspberry_RX(Data_Raspberry);
        if(strcmp(Data_Raspberry,"Accelx")==0)  { IMU_Data(Accel, x, y, z); Raspberry_TX(x); }
        else if(strcmp(Data_Raspberry, "Accely")==0) { IMU_Data(Accel, x, y, z); Raspberry_TX(y); }
            else if(strcmp(Data_Raspberry, "Accelz")==0) { IMU_Data(Accel, x, y, z); Raspberry_TX(z); }
                else if(strcmp(Data_Raspberry, "Gyrox")==0) { IMU_Data(Gyro, x, y, z); Raspberry_TX(x); }
                    else if(strcmp(Data_Raspberry, "Gyroy")==0) { IMU_Data(Gyro, x, y, z); Raspberry_TX(y); }
                        else if(strcmp(Data_Raspberry, "Gyroz")==0) { IMU_Data(Gyro, x, y, z); Raspberry_TX(x); }
     // delay(100);
        Raspberry_TX(Th_Set);
        Raspberry_RX(Data_Raspberry);
        Thruster_Setting(Data_Raspberry, TH);
        Thruster_Speed(TH);
      }
      else if(strcmp(Data_Raspberry,"PowerOFF")==0)
          {
            Th_PWR = Thruster_PWR(Thruster_OFF);
          }
          else Raspberry_TX("Wrong Command!");                
    
}

