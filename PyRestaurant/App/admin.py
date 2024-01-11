from django.contrib import admin
from . import models

# Register your models here.
modelList = [
    models.Order,
    models.User

]

for model in modelList:
  admin.site.register(model)
