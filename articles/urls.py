from django.urls import path
from . import views 

# app_name = "articles"

urlpatterns = [
    path('', views.article_list, name='list'),
    path('/<slug>', views.article_details, name="detail"),
    path('/tag/<tag>', views.tag_view, name='tag_view')
]
