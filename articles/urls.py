from django.urls import path, include
from . import views 

# app_name = "articles"

urlpatterns = [
    path('', views.homepage, name='list'),
    path('articles', views.article_list, name='list'),
    path('articles/<slug>', views.article_details, name="detail"),
    path('articles/tag/<tag>', views.tag_view, name='tag_view'),
    path('categories', views.category_list, name="categories_list"),
    path('categories/<slug>', views.category_detail, name="category"),
    path('search/',include('haystack.urls'))
]
