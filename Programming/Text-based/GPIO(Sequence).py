#Inserta tu codigo de Raspberry Pi aqui (Nota: comentarios sin tildes!)

import RPi.GPIO as GPIO
import time #Necesario para los delays

GPIO.setmode(GPIO.BCM) #Modo de configuracion BCM
#configuracion de pines
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.output(17, GPIO.LOW)
GPIO.output(22, GPIO.LOW)
GPIO.output(27, GPIO.LOW)
#secuenci-bucle infinito
while True:
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    time.sleep(1)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(27, GPIO.LOW)
    time.sleep(1)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(27, GPIO.HIGH)
    time.sleep(1)

