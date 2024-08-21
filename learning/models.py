from django.db import models
from bank.models import Lesson ,Question

class Bootcamp(models.Model):
    name = models.CharField(max_length=25)
    start_date = models.DateField()
    duration = models.IntegerField()
    price = models.FloatField()

    def __str__(self) -> str:  
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=25)
    assingment = models.ForeignKey(Question , on_delete=models.CASCADE ,related_name="assignments")
    lesson = models.ForeignKey(Lesson , on_delete=models.CASCADE , related_name="lessons")

    def __str__(self) -> str:  
        return self.name

