from django.urls import path
from . import views

app_name ='notebook'

urlpatterns = [
  path('', views.dashboard, name='dashboard'),
  path('index/', views.index, name='index'),
  path('create/', views.create, name='create'),
  path('<int:id>/show/', views.show, name='show'),
  path('<int:id>/edit/', views.edit, name='edit'),  
  path('<int:id>/update/', views.update, name='update'),
  path('<int:id>/destroy/', views.destroy, name='destroy'),
  
  path('api/list_reset/', views.api_list_reset, name='api_list_reset'),
  
  path('api/filtering_main/', views.api_filtering_main, name='api_filtering_main'),
  path('api/filtering_sub/', views.api_filtering_sub, name='api_filtering_sub')
]