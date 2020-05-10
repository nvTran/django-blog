from django.db import models
from taggit.managers import TaggableManager
from django.utils.text import slugify


# Create your models here.

class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, default='General')
    slug = models.SlugField(default='')

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

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
    body = models.TextField()
    date = models.DateTimeField(auto_now_add= True)
    thumb = models.ImageField(default='default.jpg', blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete= models.SET_NULL)
    tags = TaggableManager()
    # add in author later

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[0:120] + "..."

    def simiar(self):
        return self.tags.similar_objects()[0:3]
    

