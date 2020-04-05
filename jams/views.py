import os
from django.core import serializers
from django.shortcuts import render
from .models import Jam

def index(request):
  jams = Jam.objects.all()
  context = {
    'jams': jams
  }
  return render(request, 'jams/index.html', context)

def detail(request, jam_id):
  jam = Jam.objects.filter(pk=jam_id).first()
  opentok_token = jam.opentok_token(request.user.id)
  context = {
    'jam': serializers.serialize('json', [jam]),
    'api_key': os.getenv("OPENTOK_API_KEY"),
    'session_id': jam.opentok_session_id,
    'opentok_token': opentok_token
  }
  return render(request, 'jams/detail.html', context)