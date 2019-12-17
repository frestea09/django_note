from django.db import models

# Create your models here.
class Post(models.Model):
    judul = models.CharField(max_length=250)
    post = models.TextField()
    def __str__(self):
        return "{}".format(self.judul)