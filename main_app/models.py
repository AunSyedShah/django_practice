from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    contactNumber = models.CharField(max_length=20, verbose_name="Contact Number")

    def __str__(self):
        return self.name