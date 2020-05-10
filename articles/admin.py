from django.contrib import admin
from .models import Article, Category
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

# admin.site.unregister(Article)

admin.site.register(Article, PostAdmin)
admin.site.register(Category)




