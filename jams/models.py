from django.db import models
from django.db.models.signals import pre_save
from opentok import MediaModes, OpenTok
from django.contrib.auth.models import User

def set_open_tok_session_id():
    opentok = OpenTok('46593382', '78c15c4ccb015d203e6412f12f5fbb9436b4cd16')
    session = opentok.create_session(media_mode=MediaModes.routed)
    return session.session_id

# Create your models here.
class Jam(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=320)
  coordinator = models.ForeignKey(User, on_delete=models.CASCADE)
  open_tok_session_id = models.CharField(max_length=250, default=set_open_tok_session_id())

class JamRequest(models.Model):
  jam = models.ForeignKey(Jam, on_delete=models.CASCADE)
  publisher = models.ForeignKey(User, on_delete=models.CASCADE)


class JamRequestApproval(models.Model):
  jam_request = models.ForeignKey(JamRequest, on_delete=models.CASCADE)