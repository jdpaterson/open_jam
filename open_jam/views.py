from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render

def index(request):
  return render(request, 'home.html', {})

def register(request):
  if request.method == 'POST':
    user = User.objects.create_user(
      request.POST['username'],
      request.POST['email'],
      request.POST['password']
    )
    # user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    login(request, user)
    return render(request, "home.html", {})
  else:
    return render(request, 'registration/register.html', {})