from django.db import models
from datetime import datetime
from author.models import Author

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Quote(models.Model):
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    category = models.ManyToManyField(Category)
    quote = models.TextField(blank = False)
    is_published = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.quote
