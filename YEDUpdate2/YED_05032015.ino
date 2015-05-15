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
  //Sonar_Init();
  Thruster_Init();
}

void loop() {
  strcpy(Data_Raspberry, "");// clear string
  Raspberry_RX(Data_Raspberry);
  while((strcmp(Data_Raspberry, "IMUSet") !=0)) { //beginning of while loop
    
  if(strcmp(Data_Raspberry, "PowerOn")==0) {
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

           }
         //   Raspberry_RX(Data_Raspberry);// wait until get the next command              

//        Serial.print(TH[0]);

      
   else if(strcmp(Data_Raspberry,"PowerOFF")==0)
          {
            Th_PWR = Thruster_PWR(Thruster_OFF);
          }
   else {Raspberry_TX("Wrong Command!");}
  Raspberry_RX(Data_Raspberry);
  } // end of while loop
  //Set the thrusters according to RPI specifications
  Raspberry_TX(Th_Set);
  Raspberry_RX(Data_Raspberry);
        if(strcmp(Data_Raspberry,"Turn right")==0) { TH[0] = Thruster1; TH[1] = IDLE; TH[2] = IDLE; TH[3] = IDLE; }
        else if(strcmp(Data_Raspberry, "Turn left")==0) { TH[0] = IDLE; TH[1] = Thruster2; TH[2] = IDLE; TH[3] = IDLE; }
            else if(strcmp(Data_Raspberry, "Surface")==0) { TH[0] = IDLE; TH[1] = IDLE; TH[2] = Thruster3; TH[3] = IDLE;}
                else if(strcmp(Data_Raspberry, "Descend")==0) { TH[0] = IDLE; TH[1] = IDLE; TH[2] = IDLE; TH[3] = Thruster4; }
                    else if(strcmp(Data_Raspberry, "Go straight")==0) {  TH[0] = Thruster1; TH[1] = Thruster2; TH[2] = IDLE; TH[3] = IDLE; }
                        else if(strcmp(Data_Raspberry, "Go back")==0) { TH[0] = Reverse1; TH[1] = Reverse2; TH[2] = IDLE; TH[3] = IDLE;  }
                          else if(strcmp(Data_Raspberry, "Dead zone")==0) { TH[0] = IDLE; TH[1] = IDLE; TH[2] = IDLE; TH[3] = IDLE; }
                            else {Raspberry_TX("Wrong Command");}   
   Thruster_Speed(TH);
  
}

