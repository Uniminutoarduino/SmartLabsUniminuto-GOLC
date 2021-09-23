#Este es un control Proporcional Integral (PI) por metodo ZOH (Zero Order Holder)
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
import RPi.GPIO as GPIO
#Libreria para conversor analogo digital ADS1115
from adafruit_ads1x15.analog_in import AnalogIn

ReferenciaAltura = 25.0 #Valor de referencia-setpoint (altura)
kp = 350.0 #Valor constante proporcional
Erroranterior = 0.0 #Variables para error
Error = 0.0 
Sensor = 0.0
controlanterior = 0.0
controlpi = 0.0
cicloUtil = 0.0
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)
pwm13=GPIO.PWM(13,490) #GPIO 13 configurado para PWM a frecuencia de 490Hz
pwm13.start(0)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(12,GPIO.OUT)
pwm12=GPIO.PWM(12,490) #GPIO 12 configurado para PWM a frecuencia de 490Hz (Vaciado de tanque-si es requerido)
pwm12.start(0)
i2c = busio.I2C(board.SCL, board.SDA)
ts = 0.6 #Tiempo de muestreo para control
ads = ADS.ADS1115(i2c) #instancia para conversor ADS1115
chan = AnalogIn(ads, ADS.P0)
while True: #Ciclo infinito para realizar el conntrol
    Sensor = round(chan.voltage,3)
    Error = round ((ReferenciaAltura*0.0482)-Sensor,3)
    controlpi = round (Error * kp - 119.4 * Erroranterior + controlanterior,3) #Ecuacion de control
    if (controlpi > 1.0):
        controlpi = 1.0

    if (cicloUtil < 0.0): #Limitador (antiwind-up) para el control PI
        cicloUtil = 0.0
    if (Error < 0.0):
        Error = 0.0
    if (controlpi < 0.0):
        controlpi = 0.0
    cicloUtil = round (controlpi * 100,3)
    pwm12.ChangeDutyCycle(cicloUtil) #Modificacion del ciclo util de pwm para motobombas
    time.sleep (ts)
    controlanterior = controlpi
    Erroranterior = Error
      