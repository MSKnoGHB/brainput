from django.shortcuts import render
from .models import Category

# Create your views here.

def index(request):
  return render(request, 'notebook/index.html')

def new(request):
  categories = Category.objects.all()
  return render(request, 'notebook/new.html', {'categories': categories})

def create(request):
  
  return render()