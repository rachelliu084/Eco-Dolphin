#ifndef _SPARKFUNIMU_H_
#define _SPARKFUNIMU_H_

#define SparkFun_IMU_Baud_Rate  57600
#define IMU_Data_Width  28
#define Accel  1
#define Magn  2
#define Gyro  3  

void SparkFun_IMU_Init();

int Read_Serial_3(char *Data);

void Data_Converter(char *Data, char *x, char *y, char *z);

void IMU_Data(int Type, char *x, char *y, char *z);

#endif

