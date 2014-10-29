from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from twittmapapp.models import Tweetdata

def index(request):
    return render(request, 'twittmapapp/index.html')