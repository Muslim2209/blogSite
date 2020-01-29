from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('posts/', views.post_list, name='posts'),
    path('posts/<username>/', views.user_posts, name='posts'),
    path('comments/', views.comments_list, name='comments_list'),
    path('', views.dashboard, name='dashboard'),
]
