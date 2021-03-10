from django.shortcuts import HttpResponse
from .models import *
def test(request):
    return HttpResponse("hello mongodb")
