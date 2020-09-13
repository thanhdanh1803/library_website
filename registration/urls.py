from django.contrib import admin
from django.urls import path
from django import urls
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from registration import views

app_name = 'registration'
urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^login/$',views.user_login,name='login'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)