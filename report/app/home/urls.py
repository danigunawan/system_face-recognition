from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.index),
    path('upload/',views.upload,name ='upload')
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

urlpatterns += static(settings.IMG_URL,document_root = settings.IMG_ROOT)