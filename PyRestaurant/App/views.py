from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse

import os
import sys
import django

django_project_path = os.path.join(os.path.dirname(__file__), '..', '')
sys.path.append(django_project_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PyRestaurant.settings")
django.setup()

from App.models import Order,Customer

# Create your views here.
def greet(request):
    return HttpResponse(loader.get_template("html/greet.html").render({},request))

def homePage(request):
    orders = Order.objects.all().values()
    template = loader.get_template("html/home.html")
    context = {
        "orders" : orders
    }
    return HttpResponse(template.render(context,request))

def addNewCustomer(username,password):
    newCustomer = Customer(username=username,password=password)
    newCustomer.save()
    print(f"New User Added: {username}")

def addOrder(orderName):
    newOrder = Order(name=orderName)
    newOrder.save()
    print(f"Order Added: {orderName}")
