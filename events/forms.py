from django import forms
from django.contrib.auth import get_user_model
from .models import Event

class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name","description", "orgniser_name","orgniser_user",'location',
            'number_of_seats', 'booked_seats',
            'datet_time','image',]