from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about', views.about, name='about'),
    path('add', views.add, name='add'),
    path('contact', views.contact, name='contact'),

]