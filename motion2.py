import RPi.GPIO as GPIO
import time
import pygame
import random
import os
from pygame.locals import *
pygame.init()
GPIO.setmode(GPIO.BCM)
PIR_PIN = 21
GPIO.setup(PIR_PIN, GPIO.IN)
phrases = list()
#for sounds in repo
#for file_n in os.listdir("sounds"):
#    with open(os.path.join("sounds", file_n),"r") as f:
#        phrases.append(f.name)
#        print(phrases)
phrases.append('rick.ogg')

def MOTION(PIR_PIN):
    pygame.mixer.Sound(random.choice(phrases)).play()
try:
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
    while True:
        time.sleep(10)

except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
