#include "SparkFunIMU.h"
#include <string.h>
#include <Arduino.h>

char ACCEL[] = "#osctA";//Command Output triple-axis acceleration
char MAGN[] = "#osctM";//Command Output triple-axis magnet
char GYRO[] = "#osctG";//Command Output triple-axis gyro

void SparkFun_IMU_Init()
{
  Serial3.begin(SparkFun_IMU_Baud_Rate);
}


int Read_Serial_3(char *Data)
{
  int index = 0;
  char inChar;
//  Serial.println("Wait");
  while(!Serial3.available()); // wait until receive Data
//  Serial.println("Buff Gets Data");
  //delay(5);
  while(Serial3.available())               // Don't read unless there you know there is Data
  {
    if(index < IMU_Data_Width)          // One less than the size of the array
    {
      inChar = Serial3.read();      // Read a character
      Data[index] = inChar;       // Store it
      index++;                             // Increment where to write next
      Data[index] = '\0';         // Null terminate the string
    }
  }
//  Serial.println("End");
  return 1;  
}

void Data_Converter(char *Data, char *x, char *y, char *z)
{
  int n = 5;// the real data in the string begin from the 5th byte
  int index = 0;
  while(Data[n]!=',')
  {
    x[index]=Data[n++];
    x[++index]='\0';
  }
  n++;
  index = 0;
  while(Data[n]!=',')
  {
    y[index]=Data[n++];
    y[++index]='\0';
  }
  n++;
  index = 0;
  while(Data[n]!='\n')//the string arduino receiveds from IMU contains /n before \0
  {
    z[index]=Data[n++];
    z[++index]='\0';
  }
}


void IMU_Data(char *Data, int sw)// x,y,z are the strings of xyz-axis
{
  char Data_IMU[28];
  strcpy(Data, "");

  switch(sw)// Type: 1,Accel  2,Magnet  3,Gyro
  {
    case 1:
    {
      Serial3.print(ACCEL);// send command to IMU
      Read_Serial_3(Data_IMU);// wait and read data from IMU
//      Data_Converter(Data_IMU, x, y, z);// separate the string into three strings on xyz-axis
//      break;
        strcpy(Data, Data_IMU);
        break;
    }
/*    case 2:
    {
      Serial3.print(MAGN);// send command to IMU
      Read_Serial_3(Data_IMU);// wait and read data from IMU
      Data_Converter(Data_IMU, x, y, z);// separate the string into three strings on xyz-axis
      break;			
    }*/
    case 2:
    {
      Serial3.print(GYRO);// send command to IMU
      Read_Serial_3(Data_IMU);// wait and read data from IMU
 //     Data_Converter(Data_IMU, x, y, z);// separate the string into three strings on xyz-axis
      strcpy(Data, Data_IMU);
      break;			
    }
  }  
}
