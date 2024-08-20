from django.db import models


class User(models.Model):
    STATUS_CHOICE = (('male', 'Male'), ('female', 'Female'))
    name = models.CharField(max_length=50, verbose_name="Name")
    last_name = models.CharField(max_length=50, verbose_name="Last_Name")
    email = models.EmailField()
    city = models.CharField(max_length= 50, verbose_name="City")
    kod_meli = models.CharField(max_length= 16, verbose_name="User_id")
    phone_number = models.CharField(max_length=12, verbose_name="Your_number")
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices= STATUS_CHOICE)
    about_user = models.TextField()
    bootcamp = models.ManyToManyField('bootcamp.Bootcamp', blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.last_name}"


    

