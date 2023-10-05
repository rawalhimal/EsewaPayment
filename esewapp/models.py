from django.db import models

# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    
    def __str__(self):
        return self.title