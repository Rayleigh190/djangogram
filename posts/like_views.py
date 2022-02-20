from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Post


@login_required(login_url='common:login')
def like_post(request, post_id):
    """
    post 좋아요
    """
    post = get_object_or_404(Post, pk=post_id)
    post.image_likes.add(request.user)
    # return redirect("posts:index")
    return redirect('{}#post_{}'.format(
            resolve_url('posts:index'), post.id))


@login_required(login_url='common:login')
def like_delete(request, post_id):
    """
    post 좋아요 삭제
    """
    post = get_object_or_404(Post, pk=post_id)
    post.image_likes.remove(request.user)
    # return redirect('posts:index')
    return redirect('{}#post_{}'.format(
            resolve_url('posts:index'), post.id))