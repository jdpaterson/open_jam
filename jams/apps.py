from django.apps import AppConfig
from django.core.signals import request_finished

class JamsConfig(AppConfig):
    name = 'jams'
    label = 'jams'

def my_callback(sender, **kwargs):
    print("Request finished!")

def ready(self):
    print("HELLOHELLO")
    request_finished.connect(my_callback)