from django.db import models

# Create your models here.

# memo → Djangoでは null=False, blank=False が自動で適用される

class Category(models.Model):
  name = models.CharField(max_length=10)

class SubCategory(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  name = models.CharField(max_length=10)
  
class Note(models.Model):
  category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
  title = models.CharField(max_length=30)
  command = models.TextField()
  description =  models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)