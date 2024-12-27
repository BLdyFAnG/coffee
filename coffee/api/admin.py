from django.contrib import admin

from api.models import CoffeeType, Order

# Register your models here.
admin.site.register(CoffeeType)
admin.site.register(Order)
