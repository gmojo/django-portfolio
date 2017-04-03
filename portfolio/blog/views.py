from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag
from django.utils import timezone


def tag(request, name):
    title_text = name + ' - GarethMoger.com'
    tagPK = Tag.objects.only('pk').get(slug=name).id
    post_list = Post.objects.filter(tags=tagPK)
    latest_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0:4]
    tags = Tag.objects.all()
    categories = Category.objects.all()

    paginator = Paginator(post_list, 5)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    index = posts.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 7 if index >= 7 else 0
    end_index = index + 7 if index <= max_index - 7 else max_index
    page_range = paginator.page_range[start_index:end_index]

    return render(request, 'blog/posts.html', {
        'posts': posts, 'title': title_text, 'latest': latest_list, 'tags': tags, 'categories': categories, 'page_range': page_range
    })

def category(request, name):
    title_text = name + ' - GarethMoger.com'
    catPK = Category.objects.only('pk').get(name=name).id
    post_list = Post.objects.filter(category=catPK)
    latest_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0:4]
    tags = Tag.objects.all()
    categories = Category.objects.all()

    paginator = Paginator(post_list, 5)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    index = posts.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 7 if index >= 7 else 0
    end_index = index + 7 if index <= max_index - 7 else max_index
    page_range = paginator.page_range[start_index:end_index]

    return render(request, 'blog/posts.html', {
        'posts': posts, 'title': title_text, 'latest': latest_list, 'tags': tags, 'categories': categories, 'page_range': page_range
    })

def posts(request):
    title_text = 'Blog - GarethMoger.com'
    post_list = Post.objects.all().order_by('-published_date')
    latest_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0:4]
    tags = Tag.objects.all()
    categories = Category.objects.all()

    paginator = Paginator(post_list, 5)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    index = posts.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 7 if index >= 7 else 0
    end_index = index + 7 if index <= max_index - 7 else max_index
    page_range = paginator.page_range[start_index:end_index]

    return render(request, 'blog/posts.html', {
        'posts': posts, 'title': title_text, 'latest': latest_list, 'tags': tags, 'categories': categories, 'page_range': page_range
    })

def post_detail(request, pk, slug):
    title_text = Post.objects.only('pk').get(pk=pk).title
    latest_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0:4]
    post = get_object_or_404(Post, pk=pk)
    tags = Tag.objects.all()
    categories = Category.objects.all()

    return render(request, 'blog/post_detail.html', {'post': post, 'title': title_text, 'latest': latest_list, 'tags': tags, 'categories': categories})
