import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

buzzer=22

GPIO.setup(buzzer,GPIO.OUT)
while True:
    GPIO.output(buzzer,GPIO.HIGH)
    print("Beep")
    sleep(1)
    GPIO.output(buzzer,GPIO.LOW)
    sleep(1)