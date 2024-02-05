# Here I register models from ./models
""" 
    Commands to apply migrations:
        python manage.py makemigrations - prevents from brakes durning making new model
        python manage.py migrate - apply migrations and update database
"""
from django.contrib import admin
from .models import ItemNo1

# Register your models here.
admin.site.register(ItemNo1)
