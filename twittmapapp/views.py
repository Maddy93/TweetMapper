from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from twittmapapp.models import Tweetdata
from django.template import RequestContext, loader

def index(request):
    if request.GET.get('catSelect'):
        cat = request.GET['catSelect']
    else:
        cat = "halloween"
    tweet_list = Tweetdata.objects.filter(category=cat)
    #output = ', '.join([p.question_text for p in latest_question_list])
    template = loader.get_template('twittmapapp/index.html')
    context = RequestContext(request, {
        'tweet_list': tweet_list,
    })
    return HttpResponse(template.render(context))
