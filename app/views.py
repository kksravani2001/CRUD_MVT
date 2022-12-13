from django.shortcuts import render
from django.db.models.functions import Length

# Create your views here.
from app.models import *
def display_topics(request):
    LTO=Topic.objects.all()

    d={'LTO':LTO}
    return render(request,'display_topics.html',d)


def display_webpages(request):
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.filter(topic_name='Cricket')
    LWO=Webpage.objects.exclude(topic_name='Cricket')
    LWO=Webpage.objects.all()[2:5:]
    LWO=Webpage.objects.filter(topic_name='Cricket').order_by('-name')
    LWO=Webpage.objects.all().order_by('name')
    LWO=Webpage.objects.all().order_by(Length('name'))
    LWO=Webpage.objects.all().order_by(Length('name').desc())
    d={'LWO':LWO}
    return render(request,'display_webpages.html',d) 
     


def display_accessrecords(request):
    LAO=AccessRecords.objects.all()
    d={'LAO':LAO}
    return render(request,'display_accessrecords.html',d) 