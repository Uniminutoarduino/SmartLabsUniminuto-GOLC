#Este es un controlador Proporcional P
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
import RPi.GPIO as GPIO
from adafruit_ads1x15.analog_in import AnalogIn
ReferenciaAltura = 30 #Referencia-setpoint (30 cm)
kp = 100.0 #Constante proporcional
cicloUtil = 0
Error = 0.0
Sensor = 0.0
ControlP = 0.0
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)
pwm13=GPIO.PWM(13,490) #Configuracion de GPIO13 en modo PWM con frecuencia de 490Hz
pwm13.start(0)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)
pwm12=GPIO.PWM(12,490) #Configuracion de GPIO12 en modo PWM con frecuencia de 490Hz
pwm12.start(0)
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
chan = AnalogIn(ads, ADS.P0)

while True:
    Sensor = round(chan.voltage,3) #Lectura de ADC1115 con sensor ultrasonido US016
    Error = round ((ReferenciaAltura*0.0482)-Sensor,3)
    ControlP = round (Error * kp,3) #Ecuacion de control
    ControlP = round (ControlP * 0.08333,3)
    if (ControlP>1.0):
        ControlP = 1.0
        
    if (Error<0.0): #Limitacion para PWM
        Error = 0.0
        
    if (ControlP<0.0):
        ControlP = 0.0
        
    cicloUtil = round (ControlP * 100.0,3)
    pwm12.ChangeDutyCycle(cicloUtil) #Configuracion de PWM deacuerdo a salida de controlador
    time.sleep(0.1) #Tiempo de muestreo de 0.1 segundos
      