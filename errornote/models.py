from django.db import models
from notebook.models import MainCategory, SubCategory
# Create your models here.


class ErrorNote(models.Model):
  order = models.IntegerField(default=0)
  main_category = models.ForeignKey(MainCategory, on_delete=models.PROTECT)
  sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
  title = models.CharField(max_length=255)
  error_message = models.TextField()
  target_file = models.TextField(blank=True)
  resolution = models.TextField(blank=True)
  reference = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    ordering = ['order', 'id']
    
  def __str__(self):
    return self.title