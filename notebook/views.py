from django.shortcuts import render, redirect
from .models import Category, SubCategory, Note
from .forms import NoteForm

# Create your views here.

#一覧画面(ルート画面)
def index(request):
  notes = Note.objects.all()
  return render(request, 'notebook/index.html',{'notes': notes})

#新規作成画面
def new(request):
  categories = Category.objects.all()
  sub_categories = SubCategory.objects.all()
  return render(request, 'notebook/new.html', {'categories': categories, 'sub_categories': sub_categories})

#新規作成処理
def create(request):
  form = NoteForm(request.POST)
  if form.is_valid():
    form.save()
    return redirect('index')
  else:
    categories = Category.objects.all()
    sub_categories = SubCategory.objects.all()
    return render(request, 'notebook/new.html', {'categories': categories, 'sub_categories': sub_categories, 'form':form})
  
#詳細画面
def show(request, id):
  note = Note.objects.get(id=id)
  return render(request, 'notebook/show.html', {'note':note})

#編集画面
def edit(request, id):
  note = Note.objects.get(id=id)
  categories = Category.objects.all()
  sub_categories = SubCategory.objects.all()
  return render(request, 'notebook/edit.html',{ 'note':note, 'categories': categories, 'sub_categories': sub_categories})
  
#更新処理
def update(request, id):
  note = Note.objects.get(id=id)
  #instans=noteでPATCHになる
  form = NoteForm(request.POST, instance=note)
  if form.is_valid():
    form.save()
    return redirect('show', id=note.id)
  else:
    categories = Category.objects.all()
    sub_categories = SubCategory.objects.all()
    return render(request, 'notebook/edit.html', {'note': note, 'categories': categories, 'sub_categories': sub_categories, 'form':form})
  
#削除処理
def destroy(request, id):
  note = Note.objects.get(id=id)
  note.delete()
  return redirect('index')


    
    
    