from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q 
from .models import ErrorNote
from .forms import ErrorNoteForm

# Create your views here.

def index(request):
  error_notes = ErrorNote.objects.all()
  return render(request, 'errornote/index.html', {'error_notes': error_notes})


def create(request):
  error_note_form = ErrorNoteForm(request.POST or None)
  if request.method == 'POST' and error_note_form.is_valid():
    error_note = error_note_form.save()
    return redirect('errornote:show', id=error_note.id)
  return render(request, 'errornote/create.html',{'error_note_form':error_note_form})


def show(request, id):
  error_note = ErrorNote.objects.get(id=id)
  return render(request, 'errornote/show.html',{'error_note':error_note})

  
def update(request, id):
  error_note = ErrorNote.objects.get(id=id)
  error_note_form = ErrorNoteForm(request.POST, instance=error_note)
  if request.method =='POST' and error_note_form.is_valid():
    error_note_form.save()
    return redirect('errornote:show',{'error_note':error_note, 'error_note_form':error_note_form})
  return render(request, 'errornote/update.html',{'error_note':error_note, 'error_note_form':error_note_form})

  
def destroy(request, id):
  error_note = ErrorNote.objects.get(id=id) 
  error_note.delete()
  return redirect('errornote:index')