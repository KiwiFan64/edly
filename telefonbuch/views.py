from django.shortcuts import render
from django.http import HttpResponse
from .models import TelefonbuchEintrag
# Create your views here.

def hello(request):
    return HttpResponse("sfgzdui")

def einträge(request):
    einträge = TelefonbuchEintrag.objects.all()
    return render(request, 'einträge.html', context={'einträge': einträge})
def test():
    return "test"