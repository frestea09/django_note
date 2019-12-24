from django.contrib import admin
from . import models
# Register your models here.
# class PostAdmin(admin.ModelAdmin):
#     readonly_fields = ['slug',]
# admin.site.register(models.post,PostAdmin)
admin.site.register(models.Post)