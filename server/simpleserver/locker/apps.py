from django.apps import AppConfig


class LockerConfig(AppConfig):
    name = 'locker'

    # Initialize RPi GPIO at the start up
    def ready(self):
        # dummy
        print("I am here")
