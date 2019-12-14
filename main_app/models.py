from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    attribute = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    level = models.IntegerField()
    
    def __str__(self):
        return self.name



