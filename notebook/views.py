from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import MainCategory, SubCategory, Note
from .forms import NoteForm

# Create your views here.

#ダッシュボード(ルート画面/新規作成画面)
def dashboard(request):
  notes = Note.objects.all()
  main_categories = MainCategory.objects.all()
  sub_categories = SubCategory.objects.all()
  return render(request, 'notebook/dashboard.html',{'notes': notes, 'main_categories': main_categories, 'sub_categories': sub_categories})

#一覧画面
def index(request):
  notes = Note.objects.all()
  return render(request, 'notebook/index.html',{'notes': notes})

#新規作成処理
def create(request):
  form = NoteForm(request.POST)
  if form.is_valid():
    note = form.save()
    return redirect('show', id=note.id)
  else:
    main_categories = MainCategory.objects.all()
    sub_categories = SubCategory.objects.all()
    return render(request, 'notebook/dashboard.html', {'main_categories': main_categories, 'sub_categories': sub_categories, 'form':form})
  
#詳細画面
def show(request, id):
  note = Note.objects.get(id=id)
  return render(request, 'notebook/show.html', {'note':note})

#編集画面
def edit(request, id):
  note = Note.objects.get(id=id)
  main_categories = MainCategory.objects.all()
  sub_categories = SubCategory.objects.all()
  return render(request, 'notebook/edit.html',{ 'note':note, 'main_categories': main_categories, 'sub_categories': sub_categories})
  
#更新処理
def update(request, id):
  note = Note.objects.get(id=id)
  #instans=noteでPATCHになる
  form = NoteForm(request.POST, instance=note)
  if form.is_valid():
    form.save()
    return redirect('show', id=note.id)
  else:
    main_categories = MainCategory.objects.all()
    sub_categories = SubCategory.objects.all()
    return render(request, 'notebook/edit.html', {'note': note, 'main_categories': main_categories, 'sub_categories': sub_categories, 'form':form})
  
#削除処理
def destroy(request, id):
  note = Note.objects.get(id=id)
  note.delete()
  return redirect('index')

def api_main_categories(request):
  sub_category_id = request.GET.get('sub_category_id')
  if sub_category_id == "blank" :
    main_categories = MainCategory.objects.all()
  else:
    sub_category = SubCategory.objects.get(id=sub_category_id)
    main_category_id = sub_category.main_category.id
    main_categories = MainCategory.objects.filter(id=main_category_id)
  data =  list(main_categories.values('id', 'name'))
  return JsonResponse(data, safe=False)

def api_sub_categories(request):
  main_category_id = request.GET.get('main_category_id')
  if main_category_id == "blank":
    sub_categories = SubCategory.objects.all()
  else:
    sub_categories = SubCategory.objects.filter(main_category_id=main_category_id)
    
  data = list(sub_categories.values('id', 'name'))
  return JsonResponse(data, safe=False)
    
def api_select_reset(request):
  main_category_id = request.GET.get('main_category_id')
  sub_category_id =  request.GET.get('sub_category_id')
  
  main_categories = MainCategory.objects.all()
  sub_categories = MainCategory.objects.all()
  
  main_categories_data= list(main_categories.values('id','name'))
  sub_categories_data= list(sub_categories.values('id','name'))
  return JsonResponse({'main_categories_data':main_categories_data, 'sub_categories_data':sub_categories_data}, safe=False)
  
