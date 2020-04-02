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
  api_key = '46593382'
  opentok = OpenTok(api_key, '78c15c4ccb015d203e6412f12f5fbb9436b4cd16')
  jam = get_object_or_404(Jam, pk=jam_id)
  opentok_token = opentok.generate_token(jam.open_tok_session_id)
  context = {
    'jam': jam,
    'api_key': api_key,
    'session_id': jam.open_tok_session_id,
    'opentok_token': opentok_token
  }
  return render(request, 'jams/detail.html', context)