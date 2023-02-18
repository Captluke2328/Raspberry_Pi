
from gpiozero import LED
from time import sleep

class rpi_led_on_off():
    def __init__(self):

        self.ledPin = [17,18,27,22,25,12,13,19]
        self.LED    = [1,2,3,4,5,6,7,8]

        for i in range(len(self.ledPin)):
            self.LED[i] = LED(self.ledPin[i])
    
    def functions(self):
        while True:
            for i in range(len(self.ledPin)):
                self.LED[i].on()

                sleep(1)

            for i in range(len(self.ledPin)):
                self.LED[i].off()
    
    def functionsOnOff(self):
        while True:

            # Nyalakan semua LED
            self.LED[0].on()
            self.LED[1].on()
            self.LED[2].on()
            self.LED[3].on()
            self.LED[4].on()
            self.LED[5].on()
            self.LED[6].on()
            self.LED[7].on()

            sleep(1)

            # Padamkan smeua LED
            self.LED[0].off()
            self.LED[1].off()
            self.LED[2].off()
            self.LED[3].off()
            self.LED[4].off()
            self.LED[5].off()
            self.LED[6].off()
            self.LED[7].off()

            sleep(1)

if __name__ == "__main__":
    init = rpi_led_on_off()
    init.functions()
    #init.functionsOnOff()
