from django.db import models

# Create your models here.

class Phone(models.Model):

    name=models.CharField(max_length=15)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    description=models.TextField()


