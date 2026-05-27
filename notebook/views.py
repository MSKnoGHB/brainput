from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import MainCategory, SubCategory, Note, Command
from .forms import NoteForm, CommandForm

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
  note_form = NoteForm(request.POST)
  command_form = CommandForm(request.POST)

  if note_form.is_valid() and command_form.is_valid():
    note = note_form.save()
    command = command_form.save(commit=False)
    command.note = note
    command.save()
    return redirect('show', id=note.id)
  else:
    main_categories = MainCategory.objects.all()
    sub_categories = SubCategory.objects.all()
    return render(request, 'notebook/dashboard.html', {'main_categories': main_categories, 'sub_categories': sub_categories, 'note_form':note_form, 'command_form':command_form})


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
  #最初の1件を取得してcommandという変数
  command = note.command_set.first()
  #instans=noteでPATCHになる
  
  note_form = NoteForm(request.POST, instance=note)
  command_form = CommandForm(request.POST, instance=command)
  
  if note_form.is_valid() and command_form.is_valid():
    note_form.save()
    command_form.save()
    return redirect('show', id=note.id)
  else:
    main_categories = MainCategory.objects.all()
    sub_categories = SubCategory.objects.all()
    
    return render(request, 'notebook/edit.html', {'note': note, 'main_categories': main_categories, 'sub_categories': sub_categories, 'note_form':note_form, 'command_form':command_form})
  
#削除処理
def destroy(request, id):
  note = Note.objects.get(id=id) 
  note.delete()
  return redirect('index')

#プルダウンリスト項目リセット
def api_list_reset(request):
  category_type = request.GET.get('category_type')
  if category_type == "main":
    main_categories = MainCategory.objects.all()
    data= list(main_categories.values('id','name'))
  else:
    sub_categories = SubCategory.objects.all()
    data= list(sub_categories.values('id','name'))
  return JsonResponse(data, safe=False)  

#メイン選択によるサブデータのフィルタリング
def api_filtering_main(request):
  main_category_id = request.GET.get('main_category_id')
  sub_categories = SubCategory.objects.filter(main_category_id=main_category_id)
  #リストデータを生成＆レスポンス
  data= list(sub_categories.values('id','name'))
  return JsonResponse(data, safe=False)

#サブ選択によるメインデータのフィルタリング
def api_filtering_sub(request):
  sub_category_id = request.GET.get('sub_category_id')
  sub_category = SubCategory.objects.get(id=sub_category_id)
  main_categories = MainCategory.objects.filter(id=sub_category.main_category.id)
  #リストデータを生成＆レスポンス
  data= list(main_categories.values('id','name'))
  return JsonResponse(data, safe=False)
  
