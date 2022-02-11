from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    """
    posts 목록 출력
    """
    post_list = Post.objects.all().order_by('-create_at')
    form = CommentForm()
    context = {'post_list': post_list, 'form': form}
    return render(request, 'posts/post_list.html', context)


@login_required(login_url='common:login')
def post_create(request):
    """
    post 등록
    """
    print("0")
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


@login_required(login_url='common:login')
def post_delete(request, post_id):
    """
    post 삭제
    """
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('posts:index', post_id=post.id)
    post.delete()
    return redirect('posts:index')


@login_required(login_url='common:login')
def comment_create(request, post_id):
    """
    post 댓글 등록
    """
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_at = timezone.now()
            comment.post = post
            comment.save()
            return redirect('posts:index')


@login_required(login_url='common:login')
def comment_delete(request, comment_id):
    """
    post 댓글 삭제
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('posts:index')
    else:
        comment.delete()
    return redirect('posts:index')


@login_required(login_url='common:login')
def comment_modify(request, comment_id):
    """
    post 댓글 수정
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_at = timezone.now()
            comment.save()
            return redirect('posts:index')
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'posts/comment_form.html', context)
# Create your views here.
