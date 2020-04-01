from django.db.models.signals import pre_init, pre_save, request_finished
from django.dispatch import receiver
from django.db import transaction

from jams.models import Jam

# @receiver([pre_init, pre_save], sender=Jam)
# def pre_save_handler(sender, **kwargs):
#   print("hello")
#   # jam = kwargs.get(‘instance’, None)
#   # created = kwargs.get(‘created’, False)
#   # raw = kwargs.get(‘raw’, False)
#   # return None

# # @receiver(pre_init, sender=Jam)
# # def do_stuff(sender, instance, **kwargs):
# #   print("hello")