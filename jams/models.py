import json
from django.contrib.auth.models import User
from django.db import models
from opentok import Roles

from jams.opentok_service import OpentokService

class Jam(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=320)
  moderator = models.ForeignKey(User, on_delete=models.CASCADE)
  opentok_session_id = models.CharField(
                          max_length=250,
                          default=OpentokService.gen_opentok_session_id()
                        )
  def user_opentok_permission(self, user_id):
    if(self.coordinator.id == user_id):
      return Roles.moderator
    elif(self.jamrequest_set.filter(publisher_id=user_id).exists()):
      return Roles.publisher
    else:
      return Roles.subscriber
  def opentok_token(self, user_id):
    return OpentokService.opentok().generate_token(
      self.opentok_session_id,
      role=self.user_opentok_permission(user_id),
      data=json.dumps({})
    )
class JamRequest(models.Model):
  jam = models.ForeignKey(Jam, on_delete=models.CASCADE)
  publisher = models.ForeignKey(User, on_delete=models.CASCADE)


class JamRequestApproval(models.Model):
  jam_request = models.ForeignKey(JamRequest, on_delete=models.CASCADE)