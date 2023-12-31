from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from . import models


# Create your views here.
def greet(request):
    return HttpResponse(loader.get_template("html/greet.html").render({},request))
