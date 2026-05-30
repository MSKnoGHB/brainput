from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q 
from .models import ErrorNote
from .forms import ErrorNoteForm

# Create your views here.
def dashboard(request):
  
  return render(request, '',{})




def index(request):

  return render(request, '',{})



def create(request):
  
  return render(request, '',{})

  
  
def show(request, id):
  
  return render(request, '',{})

  
  
def update(request, id):
  
  return render(request, '',{})

  
  
def destroy(request, id):
  
  return render(request, '',{})
