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
int TH[4] = {1500, 1500, 1500 ,1500};
int cmd = 0;
char IMU[28];
//char G[28];


/*---------------------Status Word-----------------------*/
int Th_PWR = 0;

/*---------------------Status Command-----------------------*/
char Ready[] = "Ready";
char Th_Set[] = "Th_Set";
int resetPin = 12;

void setup()
{
  pinMode(resetPin, OUTPUT);
  digitalWrite(resetPin, HIGH);
  Raspberry_Init();
  Buzzer_Init();
  Power_Init();
  SparkFun_IMU_Init();
  Thruster_Init();
  //Sonar_Init();
}

void loop() {

  char *a;
  Thruster_Speed(TH);
  Raspberry_RX(Data_Raspberry);

  cmd = int(strtod(Data_Raspberry,&a));
  strcpy(Data_Raspberry, "");// clear command

  switch(cmd) {
        case 1: //IMU
         IMU_Data(IMU, 1);
         Raspberry_TX(IMU);
         break;

        case 2: //PwrOn
         if(Th_PWR == 0) { Th_PWR = Thruster_PWR(Thruster_ON); Thruster_Init(); Buzzer_3x500ms(); }
         Raspberry_TX(Ready);

         //Thruster_Stop();

        break;

        case 3: //PwrOff

            Th_PWR = Thruster_PWR(Thruster_OFF);

        break;

        case 4: //Idle
          Thruster_Stop();

        break;

        case 5:  //right
          TH[0] = Thruster1; TH[1] = IDLE; TH[2] = IDLE; TH[3] = IDLE;
          Thruster_Speed(TH);

        break;
        case 6: // left

           TH[0] = IDLE; TH[1] = Thruster2; TH[2] = IDLE; TH[3] = IDLE;
           Thruster_Speed(TH);
           // IMU_Data(IMU, 2);
           // Serial.println(IMU);
           // Thruster_Speed(TH);

        break;
        case 7: //rise
          TH[0] = IDLE; TH[1] = IDLE; TH[2] = Thruster3; TH[3] = Thruster4;
          Thruster_Speed(TH);

        break;
        case 8:  //dive
          TH[0] = IDLE; TH[1] = IDLE; TH[2] = Reverse1; TH[3] = Reverse2;
          Thruster_Speed(TH);

        break;
        case 9: //Fwd
          TH[0] = Thruster1; TH[1] = Thruster2; TH[2] = IDLE; TH[3] = IDLE;
          Thruster_Speed(TH);
        break;

        case 0:  // Back
          TH[0] = Reverse1; TH[1] = Reverse2; TH[2] = IDLE; TH[3] = IDLE;
          Thruster_Speed(TH);
        break;
        // Thruster_Setting(Data_Raspberry, TH);

        case 11: //Fwd

        TH[0] = Thruster1; TH[1] = IDLE; TH[2] = IDLE; TH[3] = IDLE;
        Thruster_Speed(TH);
        break;

        case 12: //Back

        TH[0] = IDLE; TH[1] = IDLE; TH[2] = IDLE; TH[3] = IDLE;
        Thruster_Speed(TH);
        break;

        case 13: //Reset
           //Raspberry_TX("Reset");
           digitalWrite (resetPin, LOW);
           break;
        default:
           Serial.println("Wrong Command");
           Thruster_Speed(TH);
           Thruster_Stop();
        }
        //strcpy(Data_Raspberry, "");// clear command
        //Thruster_Stop();
     }





