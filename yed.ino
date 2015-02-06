#include "Relay.h"
#include <string.h>
#include <Servo.h>
#include "Sonar.h"
#include "Thruster.h"
//#include "Depth.h"

#define ON 1
#define OFF 0

int Flag_Sonar = 0;
int Flag_Serial_0 = 0;
int Init_Sonar = 0;
int Init_Thruster = 0;
int t = 0;//  var for temp test
int Thruster = 0;
int Speed = 1500;
int RunTime = 1;

//Test[0]-ESC1,Test[1]-ESC3,Test[2]-ESC4,Test[3]-ESC2
//Forward Test[0],Test[3]
//Dive Test[1],Test[2]
//              Th1  Th3  Th4  Th2
int THSL[5] = {1530,1500,1500,1560,15000};// assume 1 feet per second
int THLL[5] = {1500,1500,1500,1560,7000};
int THRL[5] = {1530,1500,1500,1500,7000};

int THSM[5] = {1540,1500,1500,1570,7500};// assume 2 feet per second
int THLM[5] = {1500,1500,1500,1570,6000};// assume 
int THRM[5] = {1540,1500,1500,1500,6000};

int THSH[5] = {1550,1500,1500,1580,5000};// assume 3 feet per second
int THLH[5] = {1500,1500,1500,1580,5000};
int THRH[5] = {1550,1500,1500,1500,5000};

//int TestForward[5] = {1540, 1540, 1550, 1570, 30000};
//int TestBackward[5] = {1400, 1400, 1400, 1470, 30000};



char Data_Sonar[6];
char Data_PC[6];

int Read_Serial_0(char *DaTest)
{
  int index = 0;
  char inChar;
//  Serial.println("Wait");
  while(!Serial.available()); // wait until receive daTest
//  Serial.println("Buff Gets DaTest");
  while(Serial.available())               // Don't read unless there you know there is daTest
  {
    if(index < Data_Width)          // One less than the size of the array
    {
      delay(100);
      inChar = Serial.read();      // Read a character
      DaTest[index] = inChar;       // Store it
      index++;                             // Increment where to write next
      DaTest[index] = '\0';         // Null terminate the string
    }
  }
  return 1;  
}

void Thruster_Test()
{
  int Test[5] = {1500,1500,1500,1500,2000};//Test[0]-ESC1,Test[1]-ESC3,Test[2]-ESC4,Test[3]-ESC2
  Serial.print("Select Thruster:  ");
  Flag_Serial_0 = Read_Serial_0(Data_PC);
  Thruster = Data_PC[0]-48;
  Serial.println(Thruster);
  Serial.print("Select Speed:  ");
  Flag_Serial_0 = Read_Serial_0(Data_PC);
  Speed = (Data_PC[0]-48)*1000+(Data_PC[1]-48)*100+(Data_PC[2]-48)*10+(Data_PC[3]-48);
  Serial.println(Speed);
  Serial.print("Select Run Time(0-99s):  ");
  Flag_Serial_0 = Read_Serial_0(Data_PC);
  RunTime = (Data_PC[0]-48)*10+(Data_PC[1]-48);
  Serial.println(RunTime);  
  switch (Thruster)
  {
    case 0:  Thruster_Stop();
    case 1:  {  Test[0] = Speed;  Test[4] = (RunTime*1000);  Thruster_Speed(Test);  Thruster_Stop();  break;}
    case 2:  {  Test[3] = Speed;  Test[4] = (RunTime*1000);  Thruster_Speed(Test);  Thruster_Stop();  break;}
    case 3:  {  Test[1] = Speed;  Test[4] = (RunTime*1000);  Thruster_Speed(Test);  Thruster_Stop();  break;}
    case 4:  {  Test[2] = Speed;  Test[4] = (RunTime*1000);  Thruster_Speed(Test);  Thruster_Stop();  break;}
  }
  Thruster = 0;
  RunTime = 1;
  for(int i=0; i < 4; i++)  Test[i] = 1500;  

}

void Speed_Test()
{
  int Test[5] = {1500,1500,1500,1500,2000};
  int Mode = 0; 
  Serial.print("Select Mode(1. Forward  2. Dive  3. Run Together):  ");
  Flag_Serial_0 = Read_Serial_0(Data_PC);
  Mode = Data_PC[0]-48;
  switch(Mode)
  {
    case 1:
    {
      Serial.print("Select Speed For Thruster 1:  ");
      Flag_Serial_0 = Read_Serial_0(Data_PC);
      Test[0] = (Data_PC[0]-48)*1000+(Data_PC[1]-48)*100+(Data_PC[2]-48)*10+(Data_PC[3]-48);
      Serial.println(Test[0]);
      Serial.print("Select Speed For Thruster 2:  ");
      Flag_Serial_0 = Read_Serial_0(Data_PC);
      Test[3] = (Data_PC[0]-48)*1000+(Data_PC[1]-48)*100+(Data_PC[2]-48)*10+(Data_PC[3]-48);
      Serial.println(Test[3]);
      Serial.print("Select Run Time(0-99s):  ");
      Flag_Serial_0 = Read_Serial_0(Data_PC);
      Test[4] = ((Data_PC[0]-48)*10+(Data_PC[1]-48))*1000;
      Serial.println(Test[4]);
      Thruster_Speed(Test); 
      Thruster_Stop();  
      break;
    }
    case 2:
    {
      Serial.print("Select Speed For Thruster 3:  ");
      Flag_Serial_0 = Read_Serial_0(Data_PC);
      Test[1] = (Data_PC[0]-48)*1000+(Data_PC[1]-48)*100+(Data_PC[2]-48)*10+(Data_PC[3]-48);
      Serial.println(Test[1]);
      Serial.print("Select Speed For Thruster 4:  ");
      Flag_Serial_0 = Read_Serial_0(Data_PC);
      Test[2] = (Data_PC[0]-48)*1000+(Data_PC[1]-48)*100+(Data_PC[2]-48)*10+(Data_PC[3]-48);
      Serial.println(Test[2]);
      Serial.print("Select Run Time(0-99s):  ");
      Flag_Serial_0 = Read_Serial_0(Data_PC);
      Test[4] = ((Data_PC[0]-48)*10+(Data_PC[1]-48))*1000;
      Serial.println(Test[4]);
      Thruster_Speed(Test); 
      Thruster_Stop();  
      break;    
    }
    case 3:
    {
      Serial.print("Select Speed For Thruster 1:  ");
      Flag_Serial_0 = Read_Serial_0(Data_PC);
      Test[0] = (Data_PC[0]-48)*1000+(Data_PC[1]-48)*100+(Data_PC[2]-48)*10+(Data_PC[3]-48);
      Serial.println(Test[0]);
      Serial.print("Select Speed For Thruster 2:  ");
      Flag_Serial_0 = Read_Serial_0(Data_PC);
      Test[3] = (Data_PC[0]-48)*1000+(Data_PC[1]-48)*100+(Data_PC[2]-48)*10+(Data_PC[3]-48);
      Serial.println(Test[3]);  
      Serial.print("Select Speed For Thruster 3:  ");
      Flag_Serial_0 = Read_Serial_0(Data_PC);
      Test[1] = (Data_PC[0]-48)*1000+(Data_PC[1]-48)*100+(Data_PC[2]-48)*10+(Data_PC[3]-48);
      Serial.println(Test[1]);
      Serial.print("Select Speed For Thruster 4:  ");
      Flag_Serial_0 = Read_Serial_0(Data_PC);
      Test[2] = (Data_PC[0]-48)*1000+(Data_PC[1]-48)*100+(Data_PC[2]-48)*10+(Data_PC[3]-48);
      Serial.println(Test[2]);
      Serial.print("Select Run Time(0-99s):  ");
      Flag_Serial_0 = Read_Serial_0(Data_PC);
      Test[4] = ((Data_PC[0]-48)*10+(Data_PC[1]-48))*1000;
      Serial.println(Test[4]);
      Thruster_Speed(Test); 
      Thruster_Stop();  
      break;  
    }
  }
  for(int s=0; s < 4; s++)  Test[s] = 1500;
  
}

void setup()
{
  Serial.begin(4800);
  Serial1.begin(4800);
  pinMode(RELAY,OUTPUT);
  Relay(ON);
  Init_Thruster = Thruster_Init();
  if(Init_Thruster)  Serial.println("Done");
  else Serial.println("Initialize Thrusters Failed");
  Serial.println();
  delay(500);
//  Serial.println("a1");
  Thruster_Stop();
//  Serial.println("a2");
  Init_Sonar = Sonar_Init();
  if(Init_Sonar)  Serial.println("Done");
  else Serial.println("Initialize Sonar Failed");
  delay(500); 
}

void loop()
{
  //Speed_Test();
  Flag_Sonar = Sonar_Rx(Data_Sonar);
  if(strcmp(Data_Sonar,"L1") == 0)
  {
    if(Flag_Sonar)
    {
      Sonar_Tx("L1");
      Flag_Sonar = 0;
      delay(6000);
    }
    for(int i=0; i < 4; i++)
    {
      Thruster_Speed(THSL);
      Thruster_Speed(THLL);
    }
    Thruster_Stop();
    Sonar_Tx("DN");
  }
  if(strcmp(Data_Sonar,"L2") == 0)
  {
    if(Flag_Sonar)
    {
      Sonar_Tx("L2");
      Flag_Sonar = 0;
      delay(6000);
    }
//    Thruster_Speed(THLL);//change heading first
    for(int i=0; i < 4; i++)
    {
      Thruster_Speed(THSL);
      Thruster_Speed(THRL);
    }
    Thruster_Stop();
    Sonar_Tx("DN");
  }
  if(strcmp(Data_Sonar,"M1") == 0)
  {
    if(Flag_Sonar)
    {
      Sonar_Tx("M1");
      Flag_Sonar = 0;
      delay(6000);
    }
    for(int i=0; i < 4; i++)
    {
      Thruster_Speed(THSM);
      Thruster_Speed(THLM);
    }
    Thruster_Stop();
    Sonar_Tx("DN");
  }
  if(strcmp(Data_Sonar,"M2") == 0)
  {
    if(Flag_Sonar)
    {
      Sonar_Tx("M2");
      Flag_Sonar = 0;
      delay(6000);
    }
//    Thruster_Speed(THLM);//change heading first
    for(int i=0; i < 4; i++)
    {
      Thruster_Speed(THSM);
      Thruster_Speed(THRM);
    }
    Thruster_Stop();
    Sonar_Tx("DN");
  }  
  if(strcmp(Data_Sonar,"H1") == 0)
  {
    if(Flag_Sonar)
    {
      Sonar_Tx("H1");
      Flag_Sonar = 0;
      delay(6000);
    }
    for(int i=0; i < 4; i++)
    {
      Thruster_Speed(THSH);
      Thruster_Speed(THLH);
    }
    Thruster_Stop();
    Sonar_Tx("DN");
  }
  if(strcmp(Data_Sonar,"H2") == 0)
  {
    if(Flag_Sonar)
    {
      Sonar_Tx("H2");
      Flag_Sonar = 0;
      delay(6000);
    }
//    Thruster_Speed(THLH);//change heading first
    for(int i=0; i < 4; i++)
    {
      Thruster_Speed(THSH);
      Thruster_Speed(THRH);
    }
    Thruster_Stop();
    Sonar_Tx("DN");
  }
  strcpy(Data_Sonar,"");
    
  
  
}
