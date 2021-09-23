#Inserta tu codigo de Raspberry Pi aqui (Nota: comentarios sin tildes!)
import RPi.GPIO as GPIO
from RpiMotorLib import rpiservolib #Libreria para manejo de servomotores

#instancia de servo, frecuencia 50Hz
#Desplazamiento de 3=0 grados a 11=180 grados (No exceder el valor de 11)
myservotest  = rpiservolib.SG90servo('servoone', 50, 3, 11) 

# Ejecutar barrido de servomotor para robot. GPIO23 para base de robot, GPIO24 para pinza
#5 repeticiones con una periodo de 0.8 segundos
myservotest.servo_sweep(24, 6, 3, 12, 0.8, True, 0.01, 5)

# Limpiar todos los pines antes de salir de codigo
GPIO.cleanup()