from django.apps import AppConfig

#import RPI.GPIO as GPIO

class LockerConfig(AppConfig):
    name = 'locker'

    # Initialize RPi GPIO at the start up
    def ready(self):
        # dummy
        print("I am here")
        #GPIO.setmode(GPIO.BOARD)
        #GPIO.setup(3, GPIO.OUT)

        #GPIO.output(3, GPIO.HIGH)
