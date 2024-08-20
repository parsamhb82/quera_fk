from django.db import models
from accounts.models import User

class Bootcamp(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    price = models.IntegerField()
    about_bootcamp = models.TextField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.name



class comment_for_bootcamp(models.Model):
    user = models.ForeignKey('accounts.User', on_delete= models.CASCADE)
    text = models.TextField(blank=True, null=True)
    bootcamp = models.ForeignKey(Bootcamp, on_delete=models.CASCADE)

