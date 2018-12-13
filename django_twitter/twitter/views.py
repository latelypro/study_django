from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader
from .models import Tweet,User
# Create your views here.

def index(request):
    latest_tweet_list = Tweet.objects.order_by('-date')[:5]
    template = loader.get_template('twitter/index.html')
    context = {
        'latest_tweet_list' : latest_tweet_list,
    }
    return HttpResponse(template.render(context, request))