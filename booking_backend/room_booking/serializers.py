from rest_framework import serializers
from .models import Room, RoomImage, OccupyData, User
from django.contrib.auth.hashers import make_password


class RoomImageSerializers(serializers.ModelSerializer):
    room = serializers.HyperlinkedRelatedField(view_name = 'room-detail', queryset = Room.objects.all())
    class Meta:
        model = RoomImage
        fields = ['id','image', 'caption', 'room']


class OccupyDataSerializer(serializers.HyperlinkedModelSerializer):
    room = serializers.HyperlinkedRelatedField(
        view_name='room-detail',
        queryset=Room.objects.all()
    )
    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        queryset=User.objects.all()
    )

    class Meta:
        model = OccupyData
        fields = ['url', 'id', 'room', 'user', 'date']

        
class RoomSerializers(serializers.HyperlinkedModelSerializer):
    images= RoomImageSerializers(many=True, read_only = True)
    occupiedDates = OccupyDataSerializer(many=True, read_only= True)
    class Meta:
        model = Room
        fields = ['url','id','name','type','pricePerNight', 'currency','maxOccupancy', 'description', 'images','occupiedDates']



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'full_name']

        #hash password before saving 
    def validate_password(self, value):
        return make_password(value)