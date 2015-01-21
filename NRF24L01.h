#include<SPI.h>
#include "NRF24L01.h"

byte TX_Addr[TX_Addr_Num] = {0xAB,0xAB,0xAB,0xAB,0xAB};
byte RX_Addr[RX_Addr_Num] = {0xAB,0xAB,0xAB,0xAB,0xAB};

byte Pipe0[5] = {0xAB,0xAB,0xAB,0xAB,0xAB};
byte Pipe1[5] = {0xC2,0xC2,0xC2,0xC2,0xC2};
byte Pipe2[5] = {0xC2,0xC2,0xC2,0xC2,0xC3};
byte Pipe3[5] = {0xC2,0xC2,0xC2,0xC2,0xC4};
byte Pipe4[5] = {0xC2,0xC2,0xC2,0xC2,0xC5};
byte Pipe5[5] = {0xC2,0xC2,0xC2,0xC2,0xC6};

unsigned char TX_Data[TX_Data_Num] = "1234";
unsigned char RX_Data[RX_Data_Num] = "0";

byte Status;



void SPI_Init()//Initilize SPI
{
  pinMode(CSN, OUTPUT);
  pinMode(MOSI, OUTPUT);
  pinMode(MISO, INPUT);
  pinMode(SCK, OUTPUT);
  SPCR = (1<<SPE)|(1<<MSTR);// Enable SPI Master Mode
}

byte SPI_RW(byte TxData)
{
  SPDR = TxData;//start transmisson
  while(!(SPSR & (1<<SPIF)));// wait transmisson finished
  return SPDR;
}

byte SPI_RW_Reg(byte reg, byte value)
{
  byte sta;
  digitalWrite(CSN, LOW);
  SPI_RW(reg);
  sta = SPI_RW(value);
  digitalWrite(CSN, HIGH);
  return sta;
}

/*
byte SPI_R_Reg(byte reg)
{
  byte sta;
  digitalWrite(CSN, LOW);
  SPI_RW(reg);
  sta = SPI_RW(0x00);
  digitalWrite(CSN, HIGH);
  return sta;
}
*/

byte SPI_R_Buf(byte reg, byte *value, int Width)
{
  byte sta;
  digitalWrite(CSN, LOW);
  sta = SPI_RW(reg);
  for(int n = 0; n < Width; n++)
  {
    value[n] = SPI_RW(0x00);
  }
  digitalWrite(CSN, HIGH);
  return sta;
}

byte SPI_W_Buf(byte reg, byte *value, int Width)
{
  byte sta;
  digitalWrite(CSN, LOW);
  sta = SPI_RW(reg);
  for(int n = 0; n < Width; n++)
  {
    SPI_RW(*value++);
  }
  digitalWrite(CSN, HIGH);
  return sta;
}


void nRF24L01_Init()
{
//  SPI_Init();
  pinMode(LED_Tx, OUTPUT);
  pinMode(LED_Rx, OUTPUT);
  digitalWrite(CE,LOW);
  digitalWrite(CSN,HIGH);
  digitalWrite(SCK,LOW);
}

byte nRF24L01_TX(unsigned char *TxAd, unsigned char *RxAd, unsigned char *TxData, int Width)
{
  digitalWrite(LED_Tx,LOW);
  digitalWrite(LED_Rx,HIGH);
  digitalWrite(CE,LOW);
  SPI_RW(FLUSH_TX);//empty Tx Buff
  SPI_W_Buf(W_REGISTER + TX_ADDR, TxAd, TX_Addr_Num); //Set transmitter address
  SPI_W_Buf(W_REGISTER + RX_ADDR_P0, RxAd, RX_Addr_Num);//Set receiver address
  SPI_RW_Reg(W_REGISTER + EN_AA, 0x01); //Enable auto ACK
  SPI_RW_Reg(W_REGISTER + EN_RXADDR, 0x01); //Enable Pipe 0 to receive
  SPI_RW_Reg(W_REGISTER + SETUP_RETR, 0x03); //Setup Auto ACK time and 3 times
  SPI_RW_Reg(W_REGISTER + RF_CH, 0x40);  //Set RF channel frenquency
  SPI_RW_Reg(W_REGISTER + RF_SETUP, 0x0F);  //Set RF power and rate
  SPI_RW_Reg(W_REGISTER + RX_PW_P0, RX_Data_Num);  //Num of bytes in RX payload in data pipe 0
  SPI_W_Buf(W_TX_PAYLOAD, TxData, Width);  //Load TxData
  SPI_RW_Reg(W_REGISTER + CONFIG, 0x0E);  // Set working mode
  digitalWrite(CE,HIGH);
  delay(1);
}

byte nRF24L01_RX()//(unsigned char *RxData, int Width)
{
  digitalWrite(LED_Tx,HIGH);
  digitalWrite(LED_Rx,LOW);
  digitalWrite(CE,LOW);
  SPI_RW(FLUSH_RX);
  SPI_W_Buf(W_REGISTER + RX_ADDR_P0, RX_Addr, RX_Addr_Num);
  SPI_RW_Reg(W_REGISTER + EN_AA, 0x01); //Enable auto ACK
  SPI_RW_Reg(W_REGISTER + EN_RXADDR, 0x01); //Enable Pipe 0 to receive
  SPI_RW_Reg(W_REGISTER + RF_CH, 0x40);  //Set RF channel frenquency
  SPI_RW_Reg(W_REGISTER + RF_SETUP, 0x0F);  //Set RF power and rate
  SPI_RW_Reg(W_REGISTER + RX_PW_P0, RX_Data_Num);  //Num of bytes in RX payload in data pipe 0
  SPI_RW_Reg(W_REGISTER + CONFIG, 0x0F);
  digitalWrite(CE,HIGH);
  delay(1);  
}


