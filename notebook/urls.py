from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('new/', views.new, name='new'),
  path('create/', views.create, name='create'),
  path('<int:id>/show/', views.show, name='show'),
  path('<int:id>/edit/', views.edit, name='edit'),  
  path('<int:id>/update/', views.update, name='update'),
  path('<int:id>/destroy/', views.destroy, name='destroy')
]