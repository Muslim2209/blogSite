from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from users.models import User
from .forms import PostCreateForm, CommentAddForm
from .models import Post, Comment


@login_required
def dashboard(request):
    posts = Post.objects.exclude(author=request.user)
    user = request.user
    followed = user.followed.values_list('id', flat=True)
    posts = posts.filter(author__in=followed)
    comments = Comment.objects.all().order_by('-id')[:3]
    if request.method == 'POST':
        comment_form = CommentAddForm(request.POST)
        post_form = PostCreateForm(request.POST, request.FILES)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return render(request, 'blog/dashboard.html', {'new_post': new_post})
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.save()
            return render(request, 'blog/dashboard.html', {'comment': new_comment})
    else:
        post_form = PostCreateForm()
        comment_form = CommentAddForm()
    context = {
        'section': 'dashboard',
        'posts': posts,
        'comments': comments,
        'post_form': post_form,
        'comment_form': comment_form
    }
    return render(request, 'blog/dashboard.html', context)


@login_required
def post_list(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'blog/list.html', {'section': 'posts', 'posts': posts})


@login_required
def comments_list(request):
    comments = Comment.objects.all().order_by('-id')
    return render(request, 'blog/comments_list.html', {'comments': comments})


@login_required
def user_posts(request, username):
    user = User.objects.get_by_natural_key(username=username)
    posts = Post.objects.filter(author=user)
    return render(request, 'blog/user_posts.html', {'user': user, 'posts': posts})
