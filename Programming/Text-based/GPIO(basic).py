#Inserta tu codigo de Raspberry Pi aqui (Nota: comentarios sin tildes!)
import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BCM) #Modo de configuracion BCM

#Configuramos el pin GPIO 22 como una salida
GPIO.setup(22,GPIO.OUT)

#Configuramos el pin GPIO 22 con un valor de 0V o LOW 
GPIO.output(22,0)

while True:
    GPIO.output(22,1)
    time.sleep(2)
    GPIO.output(22,0)
    time.sleep(1)
