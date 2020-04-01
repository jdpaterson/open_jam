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
  jam = get_object_or_404(Jam, pk=jam_id)
  opentok_token = opentok.generate_token(jam.open_tok_session_id)
  context = {
    'jam': jam,
    'opentok_token': opentok_token
  }
  return render(request, 'jams/detail.html', context)