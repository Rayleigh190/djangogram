from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    """
    posts 목록 출력
    """
    post_list = Post.objects.all().order_by('-create_at')
    context = {'post_list': post_list}
    return render(request, 'posts/post_list.html', context)

# Create your views here.
