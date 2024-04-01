import string
import random

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from app.models import Url


# Create your views here.
def index(request):
    short_url = None
    if request.method == "POST":
        long_url = request.POST['long_url']
        short_url = generate_short_url()
        url = Url(long_url=long_url, short_url=short_url)
        url.save()
    return render(request, 'index.html',{'short_url':short_url})

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url =''.join(random.choice(characters) for i in range(6))
    return short_url

def detail(request,short_url):
    try:
        url = Url.objects.get(short_url=short_url)
        long_url = url.long_url
        url.delete()
        short_url = None
        return HttpResponseRedirect(long_url)

    except url.DoesNotExist:
        return render(request, '404.html')