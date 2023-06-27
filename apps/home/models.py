from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class LoginDevice(models.Model):
    device_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_timestamp = models.DateTimeField(auto_now_add=True)


class User(models.Model):
      name= models.CharField(max_length=50)
      email=models.EmailField(unique=True ,max_length=100)
      password = models.CharField(max_length=100)
      image = models.ImageField(upload_to='photos/%y/%m/%d' ,default='std_prof_Img.png')     #'photos/1/1/2000/standardimg.png'
      status= models.BooleanField(default=True)
      createdAcc = models.DateTimeField(auto_now_add=True)
      
      def __str__(self):
          return self.name 
     
      class Meta:
         ordering = ['-createdAcc']



class Customer(models.Model):
     customer_name = models.CharField(max_length=50)
     email = models.EmailField(max_length=100)
     mobile = models.CharField(max_length=50)
     address = models.CharField(max_length=50)
     JoinedDate = models.DateTimeField(default=datetime.now)
   #  customer_time = models.TimeField(null=True)
     
     def __str__(self):
          return self.customer_name
     
     class Meta:
          ordering = ['-JoinedDate']


#if he a Customer
class Login(models.Model):
     usernameL = models.CharField(max_length=50)
     passwordL = models.CharField(max_length=100)
     email=models.EmailField(max_length=100 ,default='customer0@gmail.com')
     
     def __str__(self):
           return self.username
 
 
class Company(models.Model):
     name = models.CharField(max_length=50)
     mobile = models.CharField(max_length=50)
     location = models.CharField(max_length=50)
     company_date = models.DateField(default=datetime.now)
     #industry
     
 
 
 
 
 
   
'''
class OrderItemStockCustomer(models.Model):
     
     orderitemstockcustomer_name = models.CharField(max_length=50)
     orderitemstockcustomer_quantity = models.CharField(max_length=50)
     orderitemstockcustomer_price = models.DecimalField(max_digits=6,decimal_places=2 ,default=00.00)
     orderitemstockcustomer_total = models.CharField(max_length=50)
     orderitemstockcustomer_date = models.DateField(default=datetime.now)
     orderitemstockcustomer_time = models.TimeField(null=True)
     
     def __str__(self):
          return self.orderitemstockcustomer_name

  ''' 
