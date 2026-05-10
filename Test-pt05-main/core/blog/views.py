from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Post
from .forms import PostForm


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post')
    else:
        form = PostForm()

    return render(request,
                  'blog/add_post.html',
                  {'form': form})


def time(request):
    dt = datetime.now()
    return HttpResponse(f"Текущее время {dt}")


def home(request):

    return HttpResponse("Добро пожаловать на мой первый джанго проект")


def youtube(request):
    return HttpResponse("<a href=https://www.youtube.com>")


def news(request):

    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')


def post_view(request):
    posts = Post.objects.all()

    return render(request,
                  'blog/post.html',
                  context={"posts": posts})

