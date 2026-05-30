from django.urls import path #フレームワークからルーティング処理関数をインポートする
from . import views #カレントディレクトリからviewsファイルをインポートする

app_name = 'errornote' 

#Djangではnewをcreateに、editをupdateに統合する方法が主流らしい
urlpatterns = [
  path('', views.dashboard, name='dashboard'),
  path('index/', views.index, name='index'),
  path('create/', views.create, name='create'),
  path('<int:id>/show/', views.show, name='show'),
  path('<int:id>/update/', views.update, name='update'),
  path('<int:id>/destroy/', views.destroy, name='destroy')
]
