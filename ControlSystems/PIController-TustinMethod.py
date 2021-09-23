#Este es un controlador PI por metodo de Tustin
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
import RPi.GPIO as GPIO
from adafruit_ads1x15.analog_in import AnalogIn
ReferenciaAltura = 28.0 #(Set point o referencia-18cm)
kp = 200.0 #Constante proporcional
ki = 0.01 #Constante integral
#Variables para error
Erroranterior = 0.0 
Error = 0.0
controlanterior = 0.0
controlpi = 0.0
ADCVal = 0.0
cicloUtil = 0.0
ts = 0.6 #Periodo de muestreo
ErrorSuma = 0.0
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)
pwm13=GPIO.PWM(13,490) #GPIO 13 configurado en modo PWM a 490 Hz (Motobomba)
pwm13.start(0)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)
pwm12=GPIO.PWM(12,490) #GPIO 12 configurado en modo PWM a 490 Hz (Motobomba)
pwm12.start(0)
i2c = busio.I2C(board.SCL, board.SDA)
ts = 0.6 
ads = ADS.ADS1115(i2c) #Instancia para ADC ADS1115
chan = AnalogIn(ads, ADS.P0)
while True:
   Sensor = round(chan.voltage,3)
   Error = round ((ReferenciaAltura*0.0482)-Sensor,3)
   ErrorSuma = ErrorSuma + Error
   controlpi = round (Error * kp + ki * ErrorSuma,3) #Ecuacion de control PI
   if (controlpi > 1.0): #Limitacion (Antiwind-up)
       controlpi = 1.0
   if (cicloUtil < 0.0):
       cicloUtil = 0.0
   if (Error < 0.0):
       Error = 0.0
   if (controlpi < 0.0):
       controlpi = 0.0
   cicloUtil = round (controlpi * 100,3)
   pwm12.ChangeDutyCycle(cicloUtil) #Configuracion de ciclo util deacuerdo a valor de controlador
   time.sleep (ts) #Esperar periodo de muestreo
   controlanterior = controlpi
   Erroranterior = Error
      