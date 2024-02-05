# Here I declare models (as classes)
from django.db import models

class ItemNo1(models.Model):
    title = models.CharField(max_length=200)
    value = models.TextField(unique=True)
