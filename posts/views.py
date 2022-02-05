from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.utils import timezone


def index(request):
    """
    posts 목록 출력
    """
    post_list = Post.objects.all().order_by('-create_at')
    context = {'post_list': post_list}
    return render(request, 'posts/post_list.html', context)


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
# Create your views here.
