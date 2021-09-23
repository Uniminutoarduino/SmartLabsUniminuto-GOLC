import tm1637
import time
from time import sleep, localtime
from tm1637 import TM1637
DIO = 4 #pines para display tm1637
CLK = 5

class Clock:
    def __init__(self, tm_instance):
        self.tm = tm_instance
        self.show_colon = False

    def run(self):
        while True: #bucle para mostrar hora continuamente
            t = localtime()
            self.show_colon = not self.show_colon
            tm.numbers(t.tm_hour, t.tm_min, self.show_colon)
            sleep(1)

if __name__ == '__main__': #funcion principal para activar display y obtener hora
    tm = TM1637(CLK, DIO) #Configuracion de TM1637
    tm.brightness(1) #ajuste de brillo de display
    clock = Clock(tm)
    clock.run()
    

