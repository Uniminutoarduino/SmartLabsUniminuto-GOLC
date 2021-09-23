#Inserta tu codigo de Raspberry Pi aqui (Nota: comentarios sin tildes!)
import tm1637
import time
tm = tm1637.TM1637(clk=5, dio=4) #Pines para tm1647 (no cambiar)
tm.brightness(val=1)
#tm.show('help')
while True:
    tm.scroll('Hello GOLC',delay=250) #Escribir en display con una periodo de 250ms
    time.sleep(1) #retraso de 1 sec