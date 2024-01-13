from django.db import models

# Create your models here.

class Customer(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username

class Order(models.Model):
      name = models.CharField(max_length=50)
      customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,related_name="orders")
      def __str__(self):
          return self.name

