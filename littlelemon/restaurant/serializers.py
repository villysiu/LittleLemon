from rest_framework import serializers 
# from django.contrib.auth.models import User
from .models import MenuItem, Booking

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']

class MenuItemSerializer(serializers.ModelSerializer):
    # title = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = MenuItem
        # fields = ['pk','title', 'price', 'inventory']
        fields = '__all__'
       
class BookingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Booking
        fields = '__all__'