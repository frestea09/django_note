from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    article = models.TextField()
    author = models.CharField(max_length=10)
    publish = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "{}.{}".format(self.id,self.title)