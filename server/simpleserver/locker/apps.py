from django.apps import AppConfig

import RPi.GPIO as GPIO

isOpen = None

class LockerConfig(AppConfig):
    name = 'locker'

    # Initialize RPi GPIO at the start up
    def ready(self):
        # dummy
        print("I am here")
        # clean up at first
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(3, GPIO.OUT)

        GPIO.output(3, GPIO.HIGH)
        global isOpen
        isOpen = False
        print(isOpen)
