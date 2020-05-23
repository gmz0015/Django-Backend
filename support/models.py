from django.db import models

# Create your models here.
class Token(models.Model):
    time = models.DateTimeField('time')
    token = models.CharField(max_length=200)