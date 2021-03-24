from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('story/', views.story, name='story'),
    path('collection/', views.collection, name='collections'),
    path('collection/<slug:slug>/', views.collection, name='collection'),
    path('product/<int:id>/<slug:slug>/',
         views.product, name='product'),
    path('contact/', views.contact, name='contact'),
]
