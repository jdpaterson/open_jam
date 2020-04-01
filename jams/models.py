from django.db import models

# Create your models here.
class Jam(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=320)

class JamRequest(models.Model):
  jam = models.ForeignKey(Jam, on_delete=models.CASCADE)

class JamRequestApproval(models.Model):
  jam_request = models.ForeignKey(JamRequest, on_delete=models.CASCADE)