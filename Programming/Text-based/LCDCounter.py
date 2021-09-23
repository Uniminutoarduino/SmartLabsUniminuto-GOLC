from RPLCD.i2c import CharLCD #Libreria para LCD

import time #libreria para retrasos
a = None #Para conteo
b = None #Para conversion de conteo a string


lcd=CharLCD('PCF8574',0x27) #Iniciar LCD en direccion seleccionada
a = 0
while True:
  a = a + 1 #incrementar a en 1
  b = str(a) #Convertir a string

  lcd.cursor_pos=(0,0) #Posicionar cursos LCD en fila 1, columna 1
  lcd.write_string(b) #Escribir string con el valor de conteo
  time.sleep(1) #Esperar 1 segundo
   