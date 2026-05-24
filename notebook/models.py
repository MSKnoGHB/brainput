from django.db import models

# Create your models here.

# memo → Djangoでは null=False, blank=False が自動で適用される

class MainCategory(models.Model):
  name = models.CharField(max_length=15)
  def __str__(self):
    return self.name

class SubCategory(models.Model):
  main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
  name = models.CharField(max_length=15)
  def __str__(self):
    return self.name
  
class Note(models.Model):
  sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
  title = models.CharField(max_length=50)
  command = models.TextField()
  description =  models.TextField(blank=True, null=True) 
  reference = models.TextField(blank=True, null=True) 
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)