from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    pincode = models.CharField(max_length=6)
    contact = models.CharField(max_length=10)

    def __str__(self):
        return self.name

