from django.shortcuts import render, redirect
from .models import Category, SubCategory, Note
from .forms import NoteForm

# Create your views here.

def index(request):
  notes = Note.objects.all()
  return render(request, 'notebook/index.html',{'notes': notes})

def new(request):
  categories = Category.objects.all()
  sub_categories = SubCategory.objects.all()
  return render(request, 'notebook/new.html', {'categories': categories, 'sub_categories': sub_categories})

def create(request):
  form = NoteForm(request.POST)
  if form.is_valid():
    form.save()
    return redirect('index')
  else:
    categories = Category.objects.all()
    return render(request, 'notebook/new.html', {'categories': categories, 'form':form})