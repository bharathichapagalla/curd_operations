from django.shortcuts import render
from app.models import *
# Create your views here.
def display_topics(request):
    LOT=Topic.objects.all()
    d={'topic':LOT}
    return render(request,'display_topics.html',d)
    

def display_webpage(request):
    LOW=Webpage.objects.all()
    d={'webpages':LOW}
    return render(request,'display_webpage.html',d)
    

def display_AccessRecords(request):
    LOA=Access_Records.objects.all()
    d={'accessrecord':LOA}
    return render(request,'display_AccessRecord.html',d)
    