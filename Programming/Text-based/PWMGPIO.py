#Inserta tu codigo de Raspberry Pi aqui (Nota: comentarios sin tildes!)
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) #Modo de configuracion BCM

import time

GPIO.setup(17,GPIO.OUT) #pin 17 como salida
pwm17=GPIO.PWM(17,500) #pin 17 en modo pwm con frecuencia de 500Hz
pwm17.start(50) #Iniciar pwm en pin 17 con ciclo util del 50 porciento
i = 0 #Variable de conteo para ciclo util
while True:
  if i < 100: #si i es menor a 100 incrementar en pasos de 20
    i = i + 20
  else:
    i = 0
  pwm17.ChangeDutyCycle(i) #Cambiar ciclo util para pin 17 de acuerdo a variable i
  time.sleep(0.3) #Esperar 0.3 segundos      