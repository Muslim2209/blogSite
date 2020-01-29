from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog.models import Post
from .forms import UserRegistrationForm
from .models import User


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST, request.FILES)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'users/register_done.html', {'news_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'users/register.html', {'user_form': user_form})


@login_required
def users_list(request):
    users = User.objects.exclude(blocked=request.user)
    return render(request, 'users/users_list.html', {'users': users})


@login_required
def user_detail(request, username):
    try:
        user = User.objects.get(username=username)
        posts = Post.objects.filter(author=user)
    except User.DoesNotExist:
        return HttpResponse('User not found')
    return render(request, 'users/user_detail.html', {'user': user, 'posts': posts})


@login_required
def followers_list(request):
    try:
        followers = User.objects.get(id=request.user.id).followers.all()
    except User.DoesNotExist:
        return HttpResponse('Nobody')
    return render(request, 'users/followers_list.html', {'followers': followers})


@login_required
def followed_to_list(request):
    try:
        followed_tos = User.objects.get(id=request.user.id).followed.all()
    except User.DoesNotExist:
        return HttpResponse('Nobody')
    return render(request, 'users/followed_to_list.html', {'followed_tos': followed_tos})


@login_required
def follow_to_user(request, pk):
    user = User.objects.get(id=request.user.id)
    user_to_follow = User.objects.get(id=pk)
    user.followed.add(user_to_follow)
    return redirect('users:users_list')


@login_required
def unfollow_from_user(request, pk):
    user = User.objects.get(id=request.user.id)
    user_to_unfollow = User.objects.get(id=pk)
    user.followed.remove(user_to_unfollow)
    return redirect('users:users_list')


@login_required
def block_user(request, username):
    user = User.objects.get(id=request.user.id)
    user_to_block = User.objects.get(username=username)
    user.blocked.add(user_to_block)
    return redirect('users:user_detail', username)


@login_required
def unblock_user(request, username):
    user = User.objects.get(id=request.user.id)
    user_to_unblock = User.objects.get(username=username)
    user.blocked.remove(user_to_unblock)
    return redirect('users:user_detail', username)
