from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
        