from django.db import models
from datetime import datetime


class Stocks(models.Model):
     ticker = models.CharField(max_length=10)
     stock_name = models.CharField(unique=True ,max_length=50)
     date = models.DateTimeField(default=datetime.now)
     open_price = models.FloatField(default=00.00)
     high_price = models.FloatField(default=00.00)
     low_price = models.FloatField(default=00.00)
     close_price = models.FloatField(default=00.00)
    
     stock_quantity = models.IntegerField()
     stock_total = models.CharField(max_length=50)
     status= models.BooleanField(default=True)
     
     def __str__(self):
          return self.stock_name


class Prediction(models.Model): 

     stock = models.ForeignKey(Stocks, on_delete=models.CASCADE) 
     date = models.DateField() 
     predicted_price = models.FloatField(default=00.00) 
     actual_price = models.FloatField(null=True, blank=True)
     
     
class DataPoint(models.Model):
    x = models.FloatField()
    y = models.FloatField()


class TrainedModel(models.Model):
    coefficient = models.FloatField()
    intercept = models.FloatField()
    



'''
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass
'''
