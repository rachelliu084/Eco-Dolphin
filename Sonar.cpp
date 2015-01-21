#include "Sonar.h"
#include <string.h>


int flag_Serial = 0;
int Init_Fail = 0;
char Data_Sonar[Data_Width];

char CM[4] = "###";
char Sx[3] = "S4";
char Rx[3] = "R4";
char Txx[4] = "T50";
int i = 0;

int Read_Serial_3(char *Data)
{
  int index = 0;
  char inChar;
  while(Serial3.available())               // Don't read unless there you know there is data
  {
    if(index < (Data_Width-1))                             // One less than the size of the array
    {
      delay(100);
      inChar = Serial3.read();               // Read a character
      Data[index] = inChar;       // Store it
      index++;                             // Increment where to write next
      Data[index] = '\0';         // Null terminate the string
    }
  }
  return 1;  
}

int Sonar_Init()
{
  /*--------------- Enter Control Mode----------------------*/
  Serial3.write("###");
  delay(100);
  flag_Serial = Read_Serial_3(Data_Sonar);
  while(flag_Serial && (~Init_Fail))
  {
    if(strcmp(Data_Sonar,"<CM>") == 0 || strcmp(Data_Sonar,"###") == 0)
    {
//      Serial.print("Enter Control Mode");
//      Serial.println();
//      Serial.println();
      flag_Serial = 0;
      Init_Fail = 0;      
    }
    else  if(i < MaxTry)        // set the resending time set max-tries
          {
            delay(2000);
            Serial3.write("###");
            Init_Fail = 0;
//            Serial.println("Warning: Trying To Enter Control Mode Again!");              
            i++; 
          }
          else  
         {
           i = 0;
           Init_Fail = 1;
//           Serial.println("Error: Entering Control Mode Failed!");
//           while(1);
         }
  }
  i = 0;
  flag_Serial = 0;
  delay(500);
  /*---------------Set Sx---------------------*/ 
  Serial3.write("S4");
  delay(100);
  flag_Serial = Read_Serial_3(Data_Sonar);
  while(flag_Serial && (~Init_Fail))
  {
    if(strcmp(Data_Sonar,"S4") == 0)
    {
//      Serial.println("Set Acoustic Transmit Data Speed And Telemetry Speed");        
//      Serial.println("S4");
//      Serial.println(); 
      flag_Serial = 0; 
      Init_Fail = 0;      
    }
    else  if(i < MaxTry)        // set the resending time set max-tries
          {
            delay(2000);
            Serial3.write("S4");
            Init_Fail = 0;
//          Serial.println("Warning: Trying To Set Sx Again!");             
            i++; 
          }
          else  
         {
           i = 0;
           Init_Fail = 1;
//           Serial.println("Error: Setting Sx Failed!");
//           while(1);
         }
  }
  i = 0;
  flag_Serial = 0;
  delay(500);  
  /*---------------Set Txx---------------------*/
  Serial3.write("R4");
  delay(100);
  flag_Serial = Read_Serial_3(Data_Sonar);
  while(flag_Serial && (~Init_Fail))
  {
    if(strcmp(Data_Sonar,"R4") == 0)
    {
//      Serial.println("Set Acoustic Receive Data Speed");        
//      Serial.println("R4");
//      Serial.println(); 
      flag_Serial = 0; 
      Init_Fail = 0;      
    }
    else  if(i < MaxTry)        // set the resending time set max-tries
          {
            delay(2000);
            Serial3.write("R4");
            Init_Fail = 0;
//          Serial.println("Warning: Trying To Set Rx Again!");             
            i++; 
          }
          else  
         {
           i = 0;
           Init_Fail = 1;
//           Serial.println("Error: Setting Sx Failed!");
//           while(1);
         }
  }
  i = 0;
  flag_Serial = 0;
  delay(500);
  /*---------------Set Txx---------------------*/
  Serial3.write("T50");
  delay(100);
  flag_Serial = Read_Serial_3(Data_Sonar);
  while(flag_Serial && (~Init_Fail))
  {
    if(strcmp(Data_Sonar,"T50") == 0)
    {
//      Serial.println("Set Receiver Detection Threshold");        
//      Serial.println("T50");
//      Serial.println(); 
      flag_Serial = 0; 
      Init_Fail = 0;      
    }
    else  if(i < MaxTry)        // set the resending time set max-tries
          {
            delay(2000);
            Serial3.write("T50");
            Init_Fail = 0;
//          Serial.println("Warning: Trying To Set Txx Again!");             
            i++; 
          }
          else  
         {
           i = 0;
           Init_Fail = 1;
//           Serial.println("Error: Setting Txx Failed!");
//           while(1);
         }
  }
  i = 0;
  flag_Serial = 0;
  delay(500);
  /*---------------Enter Data Mode---------------------*/
  Serial3.write("D");
  delay(100);
  flag_Serial = Read_Serial_3(Data_Sonar);
  while(flag_Serial && (~Init_Fail))
  {
    if(strcmp(Data_Sonar,"T50") == 0)
    {
//      Serial.println("Set Receiver Detection Threshold");        
//      Serial.println("T50");
//      Serial.println(); 
      flag_Serial = 0; 
      Init_Fail = 0;      
    }
    else  if(i < MaxTry)        // set the resending time set max-tries
          {
            delay(2000);
            Serial3.write("T50");
            Init_Fail = 0;
//          Serial.println("Warning: Trying To Set Txx Again!");             
            i++; 
          }
          else  
         {
           i = 0;
           Init_Fail = 1;
//           Serial.println("Error: Setting Txx Failed!");
//           while(1);
         }
  }
  i = 0;
  flag_Serial = 0;
  return (~Init_Fail);
  
}


void Sonar_Tx(char *TxData)
{
  Serial3.write(TxData);
}

int Sonar_Rx(char *RxData)
{
  return Read_Serial_3(RxData);
}
