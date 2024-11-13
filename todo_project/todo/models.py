from django.db import models

# Create your models here.
#This step should create the table task in our db where our attributes will be our column names
class Task(models.Model):
    #Attributes
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
