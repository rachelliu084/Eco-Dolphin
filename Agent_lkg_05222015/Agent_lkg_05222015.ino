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
int cmd=0

/*---------------------Status Word-----------------------*/
int Th_PWR = 0;

/*---------------------Status Command-----------------------*/
char Ready[] = "Ready";
char Th_Set[] = "Th_Set";
int resetPin = 12;

void setup()
{
  digitalWrite(resetPin, HIGH);
  pinMode(resetPin, OUTPUT);
  Raspberry_Init();
  Buzzer_Init();
  Power_Init();
  SparkFun_IMU_Init();
  Sonar_Init();
//  Thruster_Init();
}

void loop() {
  
  
  strcpy(Data_Raspberry, "");// clear command
  Raspberry_RX(Data_Raspberry);
  
  
  switch(cmd);{
    
  case 1:
      IMU_Data(Accel, x, y, z); Raspberry_TX(x+y+z); 
      IMU_Data(Gyro, x, y, z); Raspberry_TX(x+y+z);
    
   break;

  case 2:
        if(Th_PWR == 0) { Th_PWR = Thruster_PWR(Thruster_ON); Thruster_Init(); Buzzer_3x500ms(); }
        Raspberry_TX(Ready);
          IMU_Data(Accel, x, y, z); Raspberry_TX(x+y+z); 
          IMU_Data(Gyro, x, y, z); Raspberry_TX(x+y+z); 
        }
                         
            Thruster_Speed(TH);

        Raspberry_TX(TH); //sending the feedback chosen from the thrusters to the raspberry

      break;
      
      case 3:
          {
            Th_PWR = Thruster_PWR(Thruster_OFF);
          }
        Raspberry_TX(Th_Set);

        
        break;
        
         case 4: { TH[0] = Thruster1; TH[1] = IDLE; TH[2] = IDLE; TH[3] = IDLE; }
         
         break;
         
        case 5: { TH[0] = IDLE; TH[1] = Thruster2; TH[2] = IDLE; TH[3] = IDLE; }
        
        break;
        
            case 6: { TH[0] = IDLE; TH[1] = IDLE; TH[2] = Thruster3; TH[3] = IDLE;}
            
            break;
            
                case 7: { TH[0] = IDLE; TH[1] = IDLE; TH[2] = IDLE; TH[3] = Thruster4; }
                
                break;
                
                    case 8: {  TH[0] = Thruster1; TH[1] = Thruster2; TH[2] = IDLE; TH[3] = IDLE; }
                    
                    break;
                    
                        case 9: { TH[0] = Reverse1; TH[1] = Reverse2; TH[2] = IDLE; TH[3] = IDLE;  }
                        
                        break;
                        
                          case 10: { TH[0] = IDLE; TH[1] = IDLE; TH[2] = IDLE; TH[3] = IDLE; }
                          
                          break;
                          
        // Thruster_Setting(Data_Raspberry, TH);
        
        
        case 11:
        Raspberry_TX(Reset);
        digitalWrite (resetPin LOW);
        
        break;
        }


                   
     


