from django.db import models

# Create your models here.

class Product(models.Model):

    title=models.CharField(max_length=15)
    description=models.TextField(blank=True,null=True)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    box=models.BooleanField(null=True,blank=False)
    box2=models.BooleanField()


class Example(models.Model):
    title = models.CharField(max_length = 15)
    description = models.CharField(max_length = 20,null = True)