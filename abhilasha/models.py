from django.db import models

# Create your models here.


class ComplaintsM(models.Model):

    title = models.CharField(max_length=10, null = True)
    description = models.CharField(max_length=15, null = True)
