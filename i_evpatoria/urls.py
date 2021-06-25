from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from excursions.admin import guide_site
from .views import *


urlpatterns = [
    path('', include('excursions.urls', namespace='excursions')),
    path('contacts', contacts, name='contacts'),
    path('users/', include('users.urls', namespace='users')),
    path('superadmin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('allauth.urls')),
    path('guide-admin/', guide_site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
                          
admin.site.index_title = 'Админка'
admin.site.site_header = 'Я-Евпатория!'
admin.site.site_title = 'Я-Евпатория!'
