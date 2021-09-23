#Este codigo es para un controlador PID
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
import RPi.GPIO as GPIO
from adafruit_ads1x15.analog_in import AnalogIn

ReferenciaAltura = 10.0 #Variable de setpoint-referencia (10cm)
#Variables para error y controlador PID
Erroranterior_1 = 0.0
Erroranterior_2 = 0.0
Error = 0.0 
controlanterior_1 = 0.0
controlanterior_2 = 0.0
control_PID = 0.0
cicloUtil = 0.0
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)
pwm13=GPIO.PWM(13,490)
pwm13.start(0)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(12,GPIO.OUT)
pwm12=GPIO.PWM(12,490)
pwm12.start(0)
i2c = busio.I2C(board.SCL, board.SDA)
ts = 0.6 #Tiempo de muestreo de 0.6 segundos
ads = ADS.ADS1115(i2c) #Configuracion de ADC1115
chan = AnalogIn(ads, ADS.P0)
while True:
    Sensor = round(chan.voltage,3)
    Error = round ((ReferenciaAltura*0.0482)-Sensor,3)
    #Ecuacion de control
    control_PID = round (7.754 * Error - 15.47 * Erroranterior_1 + 7.716 * Erroranterior_2 + controlanterior_2,3)
    if (control_PID > 1.0): #Limitacion de salida de controlador
        control_PID = 1.0

    if (cicloUtil < 0.0):
        cicloUtil = 0.0
    if (Error < 0.0):
        Error = 0.0
    if (control_PID < 0.0):
        control_PID = 0.0
    cicloUtil = round (control_PID * 100,3)
    pwm12.ChangeDutyCycle(cicloUtil) #Cambio de ciclo util en funcion de la salida del controlador
    time.sleep (ts) #Esperar 1 periodo de muestreo
    controlanterior_1 = control_PID
    Erroranterior_1 = Error
    Erroranterior_2 = Erroranterior_1
    controlanterior_2 = controlanterior_1
      