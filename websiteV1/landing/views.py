from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.contrib.auth import logout

# Create your views here.
def index(request):
    return render(request,'landing/index.html')
