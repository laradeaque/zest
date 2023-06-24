from django.db import models

# Create your models here.
class Order(models.Model):
    email = models.CharField(max_length=64)
    size = models.IntegerField()
    occasion = models.TextField()
    specs = models.TextField()
    delivery_date = models.DateField()
    
    def __str__(self):
        return f'{self.email}\'s Order for {self.occasion} on {self.delivery_date}'
    
class Newsletter(models.Model):
    email = models.CharField(max_length=64)
    
    def __str__(self):
        return f'{self.email}\'s newsletter'
