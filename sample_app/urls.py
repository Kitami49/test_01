from django.urls import path
from sample_app import views


app_name = 'sample_app'
urlpatterns = [
    path('neko/create/', views.create_post, name='create_post'),  # 作成
    #path('post/edit/<int:post_id>/', views.edit_post, name='edit_post'),  # 修正
    path('neko/', views.read_post, name='read_post'),   # 一覧表示
    #path('post/delete/<int:post_id>/', views.delete_post, name='delete_post'),   # 削除
    path("calc/",views.calc_view, name='calc'),
]