import RPi.GPIO as GPIO
import time
import pygame
import random
from pygame.locals import *
pygame.init()
GPIO.setmode(GPIO.BCM)
PIR_PIN = 21
GPIO.setup(PIR_PIN, GPIO.IN)
phrases = list()
phrases.append("hello.ogg")
phrases.append("rus.ogg")
phrases.append("kenobi.ogg")
phrases.append("lina.ogg")
def MOTION(PIR_PIN):
    pygame.mixer.Sound(random.choice(phrases)).play()

try:
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)#,bouncetime=2000 
    while True:
        time.sleep(10)

except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
