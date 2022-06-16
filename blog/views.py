from django.shortcuts import render
from .models import Post
from .models import Comment


# Create your views here.


def Blog_post(request):

    posts = Post.objects.all()
    coms = Comment.objects.all()
    context = {
        'posts': posts,
        "coms": coms
    }
    return render(request, 'blog_detail.html', context)


def blog_index(request, pk):
    com = Comment.objects.filter(pk=pk)
    context = {
        'com': com
    }
    return render(request, 'blog_index.html', context)


