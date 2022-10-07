
from django.db import models

# Create your models here.


class CarModels(models.Model):

    name = models.CharField(max_length = 15)
    price = models.DecimalField(decimal_places =2,max_digits=8)