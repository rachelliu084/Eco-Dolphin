#include "Raspberry.h"

void Raspberry_Init()
{
  Serial.begin(Raspberry_Baud_Rate);
}

int Read_Serial_0(char *Data)
{
  int index = 0;
  char inChar;
//  Serial.println("Wait");
  while(!Serial.available()); // wait until receive data
//  Serial.println("Buff Gets Data");
  delay(5);
  while(Serial.available())               // Don't read unless there you know there is data
  {
    if(index < Raspberry_Data_Width)          // One less than the size of the array
    {
      inChar = Serial.read();      // Read a character
//      Serial.println("Read");
      Data[index] = inChar;       // Store it
      index++;                             // Increment where to write next
      Data[index] = '\0';         // Null terminate the string
    }
  }
  return 1;  
}

void Raspberry_TX(char *Data)
{
  Serial.print(Data);
}

void Raspberry_RX(char *Data)
{
  Read_Serial_0(Data);
}

void Thruster_Setting(char *Th, int *TH)
{
  char Th1[5], Th2[5], Th3[5], Th4[5], Th5[2];
  for(int i = 0; i < 19; i++)
  {
    if(i < 4) { Th1[i] = Th[i]; Th1[i+1] = '\0'; }
    else if( i < 8) { Th2[i-4] = Th[i]; Th2[i-3] = '\0'; }
        else if( i < 12) { Th3[i-8] = Th[i]; Th3[i-7] = '\0'; }
            else if( i < 16) { Th4[i-12] = Th[i]; Th4[i-11] = '\0'; }
                else if( i < 18) { Th5[i-16] = Th[i]; Th5[i-15] = '\0'; }
  }
  TH[0] = int(strtod(Th1,NULL));
  TH[1] = int(strtod(Th2,NULL));
  TH[2] = int(strtod(Th3,NULL));
  TH[3] = int(strtod(Th4,NULL));
  TH[4] = int(strtod(Th5,NULL));  
}
