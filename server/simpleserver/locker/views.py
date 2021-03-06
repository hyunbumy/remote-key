from rest_framework.views import APIView
from rest_framework.response import Response
from .apps import isOpen

import RPi.GPIO as GPIO

# Create your views here.
class OpenCloseView(APIView):
    # request has the arguments from the client
    # need to parse the request and make a context to pass into the html render
    # template uses the passed in context (dictionary) to populate its data

    # If GET, simply show the page
    def get(self, request, format=None):
        return Response("GET")

    # If POST, then open / close
    def post(self, request, format=None):
        #TODO: Find a way to store state info of the lock
        global isOpen
        if isOpen:
            print("Closing")
            GPIO.output(3, GPIO.HIGH)
            isOpen = False
        else:
            print("Opening")
            GPIO.output(3, GPIO.LOW)
            isOpen = True
        return Response(isOpen)
