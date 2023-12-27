from django.db import models


# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    booking_date = models.DateTimeField()
    no_of_guests = models.IntegerField() 

    def __str__(self): 
        return self.name


# Add code to create Menu model
class MenuItem(models.Model):
    title = models.CharField(max_length=255) 
    price = models.DecimalField(max_digits=10, decimal_places=2)
  #  menu_item_description = models.TextField(max_length=1000, default='') 
    inventory = models.IntegerField() 
    def __str__(self):
        return f'{self.title} : {str(self.price)}'
    