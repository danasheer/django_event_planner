from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model

class Event (models.Model):
    name = models.TextField()
    number_of_seats = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')


class Seat (models.Model):
    seat_booking = models.PositiveIntegerField()
    event_seat = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='seats')
    user_seat = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seats')