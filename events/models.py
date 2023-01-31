from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Event (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    orgniser_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    location = models.TextField()
    number_of_seats = models.PositiveIntegerField()
    booked_seats = models.PositiveIntegerField(default=0)
    datet_time = models.DateTimeField()
    image = models.ImageField(upload_to='events/')
    

    def __str__(self) -> str:
        return self.name

class Booking(models.Model):
    seat_booking = models.PositiveIntegerField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='seats')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seats')