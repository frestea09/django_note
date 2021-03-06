from django.db import models
from django.utils.text import slugify
# Create your models here.
class Post(models.Model):
    judul = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    article = models.TextField()
    publish = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    def save(self):
        self.slug = slugify(self.judul)
        super(Post,self).save()
    def __str__(self):
        return "{}.{}".format(self.id,self.judul)