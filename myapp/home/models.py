from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=22)
    email = models.CharField(max_length= 22)
    phone = models.CharField(max_length=15)
    desc = models.CharField(max_length=222)
    date = models.DateField()

    def __str__(self) :
        return self.name