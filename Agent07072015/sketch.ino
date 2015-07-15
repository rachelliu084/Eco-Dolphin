//This file will be installed in the Eco-Dolphin
//software system as the agent interface with the RPi 2

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
  Th_PWR = Thruster_PWR(Thruster_OFF);
  //Sonar_Init();
}

void loop() {

  char *a;
  //Thruster_Speed(TH);
  Raspberry_RX(Data_Raspberry);
  char inByte = Serial.read();
  cmd = int(strtod(Data_Raspberry,&a));
  strcpy(Data_Raspberry, "");// clear command
if serial.available == "" { //If Something is in the buffer
  serialEvent();
}
  switch(cmd) {
        case 1: //IMU
         IMU_Data(IMU, 1);
         Raspberry_TX(IMU);
         break;

        case 2: //PwrOn
         if(Th_PWR == 0) { Th_PWR = Thruster_PWR(Thruster_ON); Thruster_Init(); Buzzer_3x500ms(); }
         Raspberry_TX(Ready);
         break;

        case 3: //PwrOff
         Th_PWR = Thruster_PWR(Thruster_OFF);
         break;

        case 4: //Idle
         Thruster_Stop();
         break;

        case 5:  //Right
         TH[0] = Thruster1; TH[1] = IDLE; TH[2] = IDLE; TH[3] = IDLE;
         Thruster_Speed(TH);
         break;
         
        case 6: // Left
         TH[0] = IDLE; TH[1] = Thruster2; TH[2] = IDLE; TH[3] = IDLE;
         Thruster_Speed(TH);
         break;
         
        case 7: //Rise
         TH[0] = IDLE; TH[1] = IDLE; TH[2] = Thruster3; TH[3] = Thruster4;
         Thruster_Speed(TH);
         break;
         
        case 8:  //Dive
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

        default:
           Serial.println("Wrong Command");
           Thruster_Stop();
        }
        
  void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read(); 
    // add it to the inputString:
    inByte += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
      Raspbery_TX("Interrupt")
      //Serial.print(Interrupt_data)
    } 
     }
       switch (inByte) {
             case 'a':  //  Right
              digitalWrite(2, HIGH);
              break;
            case 'b':    // left
              digitalWrite(3, HIGH);
              break;
            case 'c':    // rise
              digitalWrite(4, HIGH);
              break;
            case 'd':    // Forward
              digitalWrite(5, HIGH);
              break;
            case 'e':    // Back
              digitalWrite(6, HIGH);
              break;
            case 'f': // Dive
              digitalWrite(7,HIGH);
              break;
        }
     
     
     
     
  }




