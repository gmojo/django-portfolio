from django.shortcuts import render
from django.utils import timezone
from blog.models import Post


def home(request):
    title_text = 'Home'
    post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0:2]
    return render(request, 'home/home.html', {'posts': post_list, 'title': title_text})

def about(request):
    title_text = 'About'
    return render(request, 'home/about.html', {'title': title_text})

def projects(request):
    title_text = 'Projects'
    return render(request, 'home/projects.html', {'title': title_text})