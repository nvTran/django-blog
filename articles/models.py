from django.db import models
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.

class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, default='General')
    slug = models.SlugField(default='')

    def __str__(self):
        return self.title



    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class Article(models.Model):
    TAGGIT_CASE_INSENSITIVE = True

    title = models.CharField(max_length=200)
    slug = models.SlugField()  
    snippet = models.TextField(default='', blank=True)  
    body = models.TextField()
    date = models.DateTimeField(auto_now_add= True)
    thumb = models.ImageField(default='default.jpg', blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete= models.SET_NULL)
    tags = TaggableManager()
    views = models.IntegerField(default=0)


    def __str__(self):
        return self.title

    def simiar(self):
        return self.tags.similar_objects()[0:3]
    

