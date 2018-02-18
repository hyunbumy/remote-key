import RPi.GPIO as GPIO
import time

# Need to connect common ground (connect both Pi's ground and Ardunio's ground)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)

GPIO.output(3, GPIO.HIGH)
while(1):
    command = input("Open or close: ")
    if (command == 'open'):
        # To open output a definitive 0
        GPIO.output(3, GPIO.LOW)
        print("Open")
    else:
        # To close output a non-zero (3.3V)
        GPIO.output(3, GPIO.HIGH)
        #time.sleep(3)
        print("Close")
