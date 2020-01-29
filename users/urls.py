from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('users/', views.users_list, name='users_list'),
    path('users/follow/<int:pk>/', views.follow_to_user, name='follow_to_user'),
    path('users/unfollow/<int:pk>/', views.unfollow_from_user, name='unfollow_from_user'),
    path('users/block/<username>/', views.block_user, name='block_user'),
    path('users/unblock/<username>/', views.unblock_user, name='unblock_user'),
    path('users/followed/', views.followed_to_list, name='followed_to_list'),
    path('users/followers/', views.followers_list, name='followers_list'),
    path('users/<username>/', views.user_detail, name='user_detail'),
    path('', include('django.contrib.auth.urls')),
]
