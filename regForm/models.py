from django.db import models

class RegisteredUser(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    contact = models.CharField(max_length=255)
    dob = models.DateField()
