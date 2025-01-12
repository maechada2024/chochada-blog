from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
  my_dict = {'insert_me': "Hello I am from views.py !"}
  
  return render(request, 'ccd_blog_app/index.html', context=my_dict)

def help(request):
  help_me = {'help_me': "Help me please in views.py"}
  
  return render(request, 'ccd_blog_app/help.html', context=help_me)
