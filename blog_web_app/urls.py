from django.contrib import admin
from django.urls import path, include
from .views import about
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('articles', include("articles.urls")),
    path('about/', about),
    path('', include("articles.urls")),
    path('summernote/', include('django_summernote.urls')),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)