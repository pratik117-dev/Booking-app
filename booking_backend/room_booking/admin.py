from django.contrib import admin
from .models import Room, RoomImage, OccupyData,User

# Register your models here.
admin.site.register(Room)
admin.site.register(User)
admin.site.register(RoomImage)
admin.site.register(OccupyData)