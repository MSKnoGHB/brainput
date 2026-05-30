from django.db import models

# Create your models here.

# memo → Djangoでは null=False, blank=False が自動で適用される

class MainCategory(models.Model):
  order = models.IntegerField(default=0)
  name = models.CharField(max_length=15)
  # orderの昇順に並べる、orderが同じ場合はidで並べる
  class Meta:
    ordering = ['order', 'id']
  # 管理画面で名前を表示
  def __str__(self):
    return self.name


class SubCategory(models.Model):
  order = models.IntegerField(default=0)
  main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
  name = models.CharField(max_length=15)
  
  class Meta:
    ordering = ['order', 'id']
  
  def __str__(self):
    return self.name


class Note(models.Model):
  order = models.IntegerField(default=0)
  sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
  title = models.CharField(max_length=50)
  description =  models.TextField(blank=True, null=True)
  reference = models.TextField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    ordering = ['order', 'id']
  
  def __str__(self):
    return self.title


class Command(models.Model):
  order = models.IntegerField(default=0)
  note = models.ForeignKey(Note, on_delete=models.CASCADE)
  code = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    ordering = ['order', 'id']
  
  def __str__(self):
    return self.code[:50]
