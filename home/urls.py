from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('create', views.create, name='create'),
    path('on', views.on, name='on'),
    path('read', views.read, name='read'),
    path('write', views.write, name='write')
]


