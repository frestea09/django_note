from django.db import models

# Create your models here.
class Post(models.Model):
    judul = models.CharField(max_length=50)
    article = models.TextField()
    author = models.CharField(max_length=50)
    def __str__(self):
        return '{}.{}'.format(self.id,self.judul)