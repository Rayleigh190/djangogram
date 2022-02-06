from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    """
    posts 목록 출력
    """
    post_list = Post.objects.all().order_by('-create_at')
    context = {'post_list': post_list}
    return render(request, 'posts/post_list.html', context)


@login_required(login_url='common:login')
def post_create(request):
    """
    post 등록
    """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.create_at = timezone.now()
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'posts/post_form.html', context)


@login_required(login_url='common:login')
def post_modify(request, post_id):
    """
    post 수정
    """
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.modify_at = timezone.now()
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm(instance=post)
    context = {'form': form}
    return render(request, 'posts/post_form.html', context)
# Create your views here.
