from django.db import models

# Create your models here.
#model is a class which represents a table in a databases

class Article(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    #add in thumbnail
    #add in autor
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]+'...'
