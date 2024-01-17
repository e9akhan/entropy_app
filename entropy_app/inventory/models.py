from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=50)
    depreciation_percent = models.IntegerField(default=10)

class Commodities(models.Model):
    quantity = models.IntegerField(default=0)
    price = models.FloatField()
    current_price = models.FloatField()
    buy_date = models.DateField()
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)

class Commodity(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    commoditity_name = models.ForeignKey(Commodities, on_delete=models.CASCADE)
    assign_to = models.ForeignKey(User, on_delete=models.CASCADE)