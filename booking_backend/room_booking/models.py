from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class Room(models.Model):
    ROOM_TYPES = [
        ('suite', 'suite'),
        ('standard', 'Standard Room'),
        ('deluxe', 'Deluxe Room'),
    ]
    CURRENCY_TYPE = [
        ('USD', 'USD'),
        ('USD','EUR'),
    ]
    name = models.CharField(max_length=100, blank=True, default='')
    type = models.CharField(max_length=100, choices=ROOM_TYPES)
    pricePerNight = models.IntegerField(default=150)
    currency = models.CharField(default="USD", max_length=10, choices = CURRENCY_TYPE)
    maxOccupancy = models.IntegerField(default=1)
    description = models.TextField(max_length=1000)


    def __str__(self):
        return f"{self.name}"
    

class RoomImage(models.Model):
    image = models.ImageField(upload_to='room_images/')
    caption = models.CharField(max_length=255, blank=True, null= True)
    room = models.ForeignKey(Room, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return f"image for {self.room.name} - {self.caption or 'No caption'}"
    

class OccupyData(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings")
    date = models.DateField()

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        unique_together = ('room', 'date')  # Prevent double-booking a room for the same date

    def __str__(self):
        return f"{self.room.name} booked by {self.user.username} on {self.date}"

class User(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100, default="")


