#Inserta tu codigo de Raspberry Pi aqui (Nota: comentarios sin tildes!)
from RPLCD.i2c import CharLCD #Libreria para LCD
lcd=CharLCD('PCF8574',0x27) #Direcccion de LCD por protocolo I2C

lcd.write_string('Hello  \r\n GOLC!') #Enviar mensaje a LCD en 2 filas
