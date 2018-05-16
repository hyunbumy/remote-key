from django.shortcuts import render
from django.http import HttpRequest
from locker.apps import isOpen

#import RPI.GPIO as GPIO

# Create your views here.
def open_and_close(request):
    # request has the arguments from the client
    # need to parse the request and make a context to pass into the html render
    # template uses the passed in context (dictionary) to populate its data

    # If GET, simply show the page
    if (request.method == 'GET'):
        return render(request,'locker/test.html')

    # If POST, then open / close
    elif (request.method == 'POST'):
        #TODO: Find a way to store state info of the lock
        global isOpen
        if isOpen:
            print("Closing")
            isOpen = False
        else:
            print("Opening")
            isOpen = True
        return render(request,'locker/test.html')
