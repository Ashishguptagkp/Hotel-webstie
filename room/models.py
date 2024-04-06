from django.db import models
# from .views import * 

# Create your models here.

class Categary(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 250)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)
    
    def __str__(self):
        return self.name
    
class Aminities(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 250)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)
    
    def __str__(self):
        return self.name

class Rooms(models.Model):
    id = models.AutoField(primary_key=True)
    roomcategary = models.ForeignKey(Categary, on_delete = models.CASCADE)
    roomnumber = models.IntegerField() 
    aminities = models.ManyToManyField(Aminities)
    isbooked = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)
    
    def __str__(self):
        return self.roomcategary.name
    
    
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 250)
    phone = models.IntegerField()
    address = models.CharField(max_length = 250)
    email = models.CharField(max_length = 250)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)
    
    def __str__(self):
        return self.name
    
    
class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete = models.CASCADE)
    checkIn = models.DateTimeField(auto_now_add = False)
    checkOut = models.DateTimeField(auto_now_add = False)
    ischeckOut = models.BooleanField(default= False)
    
    def __str__(self):
        return self.customername
    
       
        
    
    
    
       