from django.db import models
from taggit.managers import TaggableManager
# from taggit.models import Tag


# Create your models here.
class Article(models.Model):
    TAGGIT_CASE_INSENSITIVE = True

    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add= True)
    thumb = models.ImageField(default='default.jpg', blank=True)
    tags = TaggableManager()
    # add in author later

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[0:120] + "..."

    def simiar(self):
        return self.tags.similar_objects()[0:3]
    
