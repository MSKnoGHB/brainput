from django.shortcuts import render, redirect
from .models import Category
from .forms import NoteForm

# Create your views here.

def index(request):
  return render(request, 'notebook/index.html')

def new(request):
  categories = Category.objects.all()
  return render(request, 'notebook/new.html', {'categories': categories})

def create(request):
  form = NoteForm(request.POST)
  if form.is_valid():
    form.save()
    return redirect('index')
  else:
    categories = Category.objects.all()
    return render(request, 'notebook/new.html', {'categories': categories, 'form':form})