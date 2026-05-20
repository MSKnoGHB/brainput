from django.urls import path
from . import views

urlpatterns = [
  path('', views.dashboard, name='dashboard'),
  path('index/', views.index, name='index'),
  path('create/', views.create, name='create'),
  path('<int:id>/show/', views.show, name='show'),
  path('<int:id>/edit/', views.edit, name='edit'),  
  path('<int:id>/update/', views.update, name='update'),
  path('<int:id>/destroy/', views.destroy, name='destroy'),
  
  path('api/main_categories/', views.api_main_categories, name='api_main_categories'),
  path('api/sub_categories/', views.api_sub_categories, name='api_sub_categories')
  path('api/select_reset/', views.api_select_reset, name='api_select_reset')
]