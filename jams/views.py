import os
from django.core import serializers
from django.shortcuts import get_object_or_404, render
from .models import Jam
from opentok import OpenTok

def index(request):
  jams = Jam.objects.all()
  context = {
    'jams': jams
  }
  return render(request, 'jams/index.html', context)

def detail(request, jam_id):
  api_key = os.getenv("OPENTOK_API_KEY")
  opentok = OpenTok(api_key, os.getenv("OPENTOK_SECRET"))
  jam = Jam.objects.filter(pk=jam_id).first()
  opentok_token = opentok.generate_token(jam.open_tok_session_id)
  can_moderate = jam.coordinator.id == request.user.id
  can_publish = jam.jamrequest_set.filter(publisher_id=request.user.id).exists()
  context = {
    'jam': serializers.serialize('json', [jam]),
    'api_key': api_key,
    'session_id': jam.open_tok_session_id,
    'opentok_token': opentok_token,
    'permissions': {
      'can_moderate': can_moderate,
      'can_publish': can_publish
    },
    'current_user': serializers.serialize('json', [request.user])
  }
  return render(request, 'jams/detail.html', context)