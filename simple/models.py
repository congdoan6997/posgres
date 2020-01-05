from django.db import models

# Create your models here.
class Simple(models.Model):
    col = models.CharField(max_length=50)