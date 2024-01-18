from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib import messages

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

def homePage(request,customer):
    orders = customer.orders.all()
    template = loader.get_template("html/home.html")
    context = {
        "orders" : orders
    }
    return HttpResponse(template.render(context,request))


def loginPage(request):
    return HttpResponse(loader.get_template("html/login.html").render({},request))

def addNewCustomer(username,password):
    newCustomer = Customer(username=username,password=password)
    newCustomer.save()
    return newCustomer

def getCustomer(username,password):
    return Customer.objects.get(username=username,password=password)

def customerExists(username,password):
    try:
        customer = Customer.objects.get(username=username,password=password)
        return True
    except Customer.DoesNotExist:
        return False

def loginCustomer(request):
    username = request.POST["username"]
    password = request.POST["password"]
    if customerExists(username=username,password=password): 
       return homePage(request,Customer.objects.get(username=username,password=password))
    else:
       return HttpResponse(loader.get_template("html/login.html").render({},request))



def addOrder(orderName,customer):
    newOrder = Order(name=orderName,customer=customer)
    newOrder.save()
    print(f"Order Added: {orderName}")
