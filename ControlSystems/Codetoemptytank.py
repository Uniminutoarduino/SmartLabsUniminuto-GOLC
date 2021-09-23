import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
import RPi.GPIO as GPIO
from adafruit_ads1x15.analog_in import AnalogIn
Sensor = 0.0 #Variable para obtener valor de sensado por ultrasonido US016
GPIO.setmode(GPIO.BCM) 
GPIO.setup(12,GPIO.OUT)
pwm12=GPIO.PWM(12,490) #GPIO 12 configurado en modo PWM con frecuencia de 490Hz (Motobomba tanque principal)
pwm12.start(0)
GPIO.setup(13,GPIO.OUT)
pwm13=GPIO.PWM(13,490) #GPIO 12 configurado en modo PWM con frecuencia de 490Hz (Motobomba tanque auxiliar)
pwm13.start(0)
i2c = busio.I2C(board.SCL, board.SDA) #Configuracion de ADC ADS1115
ads = ADS.ADS1115(i2c)
chan = AnalogIn(ads, ADS.P0)
while True:
   Sensor = round(chan.voltage,3) #Lectura de valor de voltaje con acondicionamiento de sensor
   if (Sensor <=0.006): #Si valor de sensor menor a 0.0006 detener motobomba de vaciado
       pwm13.ChangeDutyCycle(0)
       pwm12.ChangeDutyCycle(0)
   else: 
       pwm13.ChangeDutyCycle(100) #Si valor de sensor mayor a 0.0006 activar motobomba de vaciado
       pwm12.ChangeDutyCycle(0)
      