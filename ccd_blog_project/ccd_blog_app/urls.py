from django.urls import path
from ccd_blog_app import views

urlpatterns = [
  path('', views.index, name='index'),
  path('help', views.help, name='help'),
]