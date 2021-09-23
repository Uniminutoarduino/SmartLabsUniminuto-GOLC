#Inserta tu codigo de Raspberry Pi aqui (Nota: comentarios sin tildes!)

import smbus #Libreria i2c
from graficador import *
import time #Libreria para retrasos

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) #Modo de configuracion BCM
GPIO.setup(25,GPIO.OUT) #Pin 25 como salida para prender lampara

I2C_BUS = 1 #Numero de bus en Raspberry Pi

bus = smbus.SMBus(I2C_BUS) #Asignar el bus a una variable para tratamiento posterior

DEVICE_ADDRESS = 0x48 #Direccion TMP102 ADD0->GND (Ver datasheet)

def LeerTMP102(): #Funcion para lectura de TMP102
  temp_reg_12bit = bus.read_word_data(DEVICE_ADDRESS , 0 )
  temp_low = (temp_reg_12bit & 0xff00) >> 8
  temp_high = (temp_reg_12bit & 0x00ff)
  temp  = ((( temp_high * 256 ) + temp_low) >> 4 )
  temp_C = float(temp) * 0.0625
  return temp_C


tempera = 0.0
while True:
  tempera = LeerTMP102() #Leer TMP102 en bucle infinito
  tempu = str(tempera) # Convertir temperatura leida a string
  GPIO.output(25,1) # Encender pin 25 para activar lampara
  graficar1m(tempu) #Graficar en tiempo real la temperatura-se envia el string
  time.sleep(1) #retraso de 1 segundo    
