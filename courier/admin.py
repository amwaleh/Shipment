from django.contrib import admin
from .models import Customers, Mailbag, Destinations
admin.site.register((Customers, Mailbag, Destinations))
# Register your models here.
