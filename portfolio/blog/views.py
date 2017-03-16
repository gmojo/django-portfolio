from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def category(request, name):
    title_text = name
    catPK = Category.objects.only('pk').get(name=name).id
    post_list = Post.objects.filter(category=catPK)

    paginator = Paginator(post_list, 2)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/posts.html', {'posts': posts, 'title': title_text})

def posts(request):
    title_text = 'Blog'
    post_list = Post.objects.all().order_by('-published_date')

    paginator = Paginator(post_list, 2)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/posts.html', {'posts': posts, 'title': title_text})

def post_detail(request, pk, slug):
    title_text = Post.objects.only('pk').get(pk=pk).title
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post, 'title': title_text})