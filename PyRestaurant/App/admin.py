from django.contrib import admin
from . import models

# Register your models here.
modelList = [
    models.Order

]

for model in modelList:
  admin.site.register(model)
