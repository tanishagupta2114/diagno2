from django.db import models

# Create your models here.
class disease(models.Model):
    q1 = models.TextField()
    a1 = models.TextField()
    d=models.CharField(max_length=30,default='diabetes')