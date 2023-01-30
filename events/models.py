from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Event (models.Model):
    name = models.TextField()
    number_of_seats = models.PositiveIntegerField()
    description = models.TextField()
    location = models.TextField()
    datet_time = models.DateTimeField()
    orgniser_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')


class Booking(models.Model):
    seat_booking = models.PositiveIntegerField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='seats')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seats')