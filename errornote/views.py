from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q 
from commandnote.models import MainCategory, SubCategory
from .models import ErrorNote
from .forms import ErrorNoteForm

# Create your views here.

def index(request):
  search = request.GET.get('search_word')
  if search:
    error_notes = ErrorNote.objects.filter(
      Q(sub_category__main_category__name__icontains=search)|
      Q(sub_category__name__icontains=search)|
      Q(title__icontains=search)|
      Q(error_message__icontains=search)|
      Q(target_file__icontains=search)|
      Q(resolution__icontains=search)|
      Q(reference__icontains=search)
    ).distinct()
  else:
    error_notes = ErrorNote.objects.all()
  return render(request, 'errornote/index.html', {'error_notes': error_notes, 'search':search})


def create(request):
  error_notes = ErrorNote.objects.all()
  main_categories =  MainCategory.objects.all()
  sub_categories = SubCategory.objects.all()
  error_note_form = ErrorNoteForm(request.POST or None)
  print("form:",error_note_form)
  print("Method:",request.method)
  if request.method == 'POST' and error_note_form.is_valid():
    error_note = error_note_form.save()
    return redirect('errornote:show', id=error_note.id)
  return render(request, 'errornote/create.html',{'error_notes': error_notes, 'main_categories':main_categories,'sub_categories':sub_categories,'error_note_form':error_note_form})


def show(request, id):
  error_note = ErrorNote.objects.get(id=id)
  return render(request, 'errornote/show.html',{'error_note':error_note})

  
def update(request, id):
  main_categories =  MainCategory.objects.all()
  sub_categories = SubCategory.objects.all()
  error_note = ErrorNote.objects.get(id=id)
  error_note_form = ErrorNoteForm(request.POST, instance=error_note)
  if request.method =='POST' and error_note_form.is_valid():
    error_note_form.save()
    return redirect('errornote:show', id=error_note.id)
  return render(request, 'errornote/update.html',{'error_note':error_note, 'error_note_form':error_note_form, 'main_categories':main_categories, 'sub_categories':sub_categories})

  
def destroy(request, id):
  error_note = ErrorNote.objects.get(id=id) 
  error_note.delete()
  return redirect('errornote:index')