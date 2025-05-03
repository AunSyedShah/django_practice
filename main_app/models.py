from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100, default='None')
    contactNumber = models.CharField(max_length=20, verbose_name="Contact Number", default='None')
    address = models.TextField(default='')
    blood_group = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name