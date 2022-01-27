from django.db import models
import datetime


# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    load_date = models.DateField(auto_now_add=datetime.datetime.now().strftime("%Y-%m-%d"))
    ac_advisor = models.CharField(max_length=40)
    originality = models.IntegerField()

    def __str__(self):
        return f'{self.title} - {self.load_date} - {self.ac_advisor} - {self.originality}%'
