from django.contrib import admin

# Register your models here.
from .models import Event, Booking

admin.site.register([Event, Booking])