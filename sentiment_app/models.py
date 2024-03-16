from django.db import models

# Create your models here.

class SentimentModel(models.Model):
    text = models.TextField()
    label = models.CharField(max_length=500)
    score = models.FloatField()

