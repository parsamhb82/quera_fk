from django.db import models
from learning.models import Class ,Bootcamp


class User(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    classes = models.ForeignKey(Class ,on_delete=models.CASCADE ,related_name="cls")
    bootcamps = models.ForeignKey(Bootcamp , on_delete=models.CASCADE ,related_name="boot")

    def __str__(self) -> str:  
        return self.email

