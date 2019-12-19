from django.db import models

# Create your models here.
class Post(models.Model):
    judul = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    post = models.TextField()
    def __str__(self):
        return '{}'.format(self.judul)