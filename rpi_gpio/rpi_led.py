from gpiozero import LED
from time import sleep

class rpi_led():
    def __init__(self):
        self.LED1 = LED(17)
        self.LED2 = LED(18)
        self.LED3 = LED(27)
        self.LED4 = LED(22)
        self.LED5 = LED(25)
        self.LED6 = LED(12)
        self.LED7 = LED(13)
        self.LED8 = LED(19)
    
    def functions(self):
        while True:
            self.LED1.on()
            self.LED8.on()
            sleep(0.5)
            self.LED1.off()
            self.LED8.off()
            
            self.LED2.on()
            self.LED7.on()
            sleep(0.5)
            self.LED2.off()
            self.LED7.off()

            self.LED3.on()
            self.LED6.on()
            sleep(0.5)
            self.LED3.off()
            self.LED6.off()

            self.LED4.on()
            self.LED5.on()
            sleep(0.5)
            self.LED4.off()
            self.LED5.off()

if __name__ == "__main__":
    init = rpi_led()
    init.functions()

