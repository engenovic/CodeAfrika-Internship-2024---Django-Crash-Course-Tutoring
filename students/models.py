from django.contrib.auth.models import User
from django.db import models

class Student(models.Model):
    regno = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)


    def __str__(self):
        return self.first_name