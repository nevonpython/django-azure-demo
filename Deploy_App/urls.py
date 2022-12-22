from django.conf.urls import url
from django.urls import path
from Deploy_App import views


urlpatterns = [
    path('', views.index, name='index'),
]
