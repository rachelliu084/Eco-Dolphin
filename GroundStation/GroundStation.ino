#include "NRF24L01.h"
#include<SPI.h>
#include <string.h>

#define Data_Width 3

extern byte TX_Addr[TX_Addr_Num];
extern byte RX_Addr[RX_Addr_Num];

unsigned char L1[TX_Data_Num] = "L1";
unsigned char L2[TX_Data_Num] = "L2";
extern unsigned char RX_Data[RX_Data_Num];

extern byte Status;

char PC[Data_Width];
unsigned char PC_unchar[Data_Width];

int Read_Serial_0(char *Data)
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
      Data[index] = inChar;       // Store it
      index++;                             // Increment where to write next
      Data[index] = '\0';         // Null terminate the string
    }
  }
  return 1;  
}

void char2unchar(char *Char, unsigned char *Unchar)
{
  int index = 0;
  while(index < Data_Width)          // One less than the size of the array
    {
      Unchar[index] = byte(Char[index]);       // Store it
      index++;                             // Increment where to write next
      Unchar[index] = '\0';         // Null terminate the string
    }
}

void unchar2char(unsigned char *Unchar, char *Char)
{
  int index = 0;
  while(index < Data_Width)          // One less than the size of the array
    {
      Char[index] = char(Unchar[index]);       // Store it
      index++;                             // Increment where to write next
      Char[index] = '\0';         // Null terminate the string
    }
}


void setup()
{
  Serial.begin(9600);
  SPI_Init();
  nRF24L01_Init(); 
}

void loop()
{
  Read_Serial_0(PC);
  Serial.println(PC);
  char2unchar(PC,PC_unchar);
  nRF24L01_TX(TX_Addr, RX_Addr, L1, TX_Data_Num);
  Serial.println("Sending...");
  Status = SPI_RW_Reg(R_REGISTER + STATUS, 0x00);
/*  Serial.print("Status = ");
  Serial.print(Status,HEX);
  Serial.print("\t");
  Serial.println(Status,BIN);*/
  if(Status & TX_DS)
  {
    Serial.println("Done");
//    if(digitalRead(IRQ==0)) Serial.println("IRQ_Sent");
  }
  if(Status & MAX_RT)
  {
    Serial.println("MAX_RT");
//    if(digitalRead(IRQ==0)) Serial.println("IRQ_MAX_RT");
  }  
}
