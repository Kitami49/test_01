from django.urls import path
from sample_app import views


app_name = 'sample_app'
urlpatterns = [
    path('neko/create/', views.create_post, name='create_post'),  # 作成
    path('neko/', views.read_post, name='read_post'),   # 一覧表示
    path("calc/",views.calc_view, name='calc'), #計算ページ
]