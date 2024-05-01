from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Students(models.Model):
    register_number = models.PositiveIntegerField(unique=True)  # Unique constraint
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=10)

    def __str__(self):
        return self.full_name
    
