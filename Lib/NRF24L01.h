#ifndef _NRF24L01_H_
#define _NRF24L01_H_

#include <Arduino.h>

#define R_REGISTER    0x00 // Define read command to register
#define W_REGISTER    0x20 // Define write command to register
#define R_RX_PAYLOAD  0x61 // Define RX payload register address
#define W_TX_PAYLOAD  0xA0 // Define TX payload register address
#define FLUSH_TX      0xE1 // Define flush TX register command
#define FLUSH_RX      0xE2 // Define flush RX register command
#define REUSE_TX_PL   0xE3 // Define reuse TX payload register command
#define NOP           0xFF // Define No Operation, might be used to read status

#define CONFIG 0x00 // 'Config' register address
#define EN_AA 0x01 // 'Enable Auto Acknowledgment' register address
#define EN_RXADDR 0x02 // 'Enabled RX addresses' register address
#define SETUP_AW 0x03 // 'Setup address width' register address
#define SETUP_RETR 0x04 // 'Setup Auto. Retrans' register address
#define RF_CH 0x05 // 'RF channel' register address
#define RF_SETUP 0x06 // 'RF setup' register address
#define STATUS 0x07 // 'Status' register address
#define OBSERVE_TX 0x08 // 'Observe TX' register address
#define CD 0x09 // 'Carrier Detect' register address
#define RX_ADDR_P0 0x0A // 'RX address pipe0' register address
#define RX_ADDR_P1 0x0B // 'RX address pipe1' register address
#define RX_ADDR_P2 0x0C // 'RX address pipe2' register address
#define RX_ADDR_P3 0x0D // 'RX address pipe3' register address
#define RX_ADDR_P4 0x0E // 'RX address pipe4' register address
#define RX_ADDR_P5 0x0F // 'RX address pipe5' register address
#define TX_ADDR 0x10 // 'TX address' register address
#define RX_PW_P0 0x11 // 'RX payload width, pipe0' register address
#define RX_PW_P1 0x12 // 'RX payload width, pipe1' register address
#define RX_PW_P2 0x13 // 'RX payload width, pipe2' register address
#define RX_PW_P3 0x14 // 'RX payload width, pipe3' register address
#define RX_PW_P4 0x15 // 'RX payload width, pipe4' register address
#define RX_PW_P5 0x16 // 'RX payload width, pipe5' register address
#define FIFO_STATUS 0x17 // 'FIFO Status Register' register address

#define RX_DR    0x40
#define TX_DS    0x20
#define MAX_RT   0x10


#define CSN 53 //SS  Mega 53 Uno 10
#define IRQ 3//interrupt
#define CE 2//config
#define LED_Tx 47//interrupt
#define LED_Rx 49//config


#define TX_Data_Num 32
#define RX_Data_Num 32

#define TX_Addr_Num 5
#define RX_Addr_Num 5

void SPI_Init();
byte SPI_RW(byte TxData);
byte SPI_RW_Reg(byte reg, byte value);
byte SPI_R_Buf(byte reg, byte *value, int Width);
byte SPI_W_Buf(byte reg, byte *value, int Width);
void nRF24L01_Init();
byte nRF24L01_TX(unsigned char *TxAddr, unsigned char *RxAddr, unsigned char *TxData, int Width);
byte nRF24L01_RX();


#endif
