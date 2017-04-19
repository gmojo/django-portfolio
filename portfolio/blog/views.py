from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag
from django.db.models import Count
from django.utils import timezone


def posts(request, cat='', tag=''):
    title_text = 'Blog - GarethMoger.com'
    description = 'My latest blog posts to share knowledge and ideas in data analysis and web development'

    #Generate post list according to URL
    if cat:
        catPK = Category.objects.get(name=cat).id
        post_list = Post.objects.filter(category=catPK).order_by('-published_date')
    elif tag:
        tagPK = Tag.objects.get(slug=tag).id
        post_list = Post.objects.filter(tags=tagPK).order_by('-published_date')
    else:
        post_list = Post.objects.all().order_by('-published_date')

    #Data for side list groups
    latest_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0:4]
    cat_count = Category.objects.all().annotate(catcount=Count('post'))
    tag_count = Tag.objects.all().annotate(tagcount=Count('post'))
    post_count = Post.objects.count()

    #Pagination
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
        'posts': posts,
        'title': title_text,
        'latest': latest_list,
        'categories': cat_count,
        'page_range': page_range,
        'tag_count': tag_count,
        'post_count': post_count,
        'description': description
    })

def post_detail(request, pk, slug):
    title_text = Post.objects.only('pk').get(pk=pk).title
    description = Post.objects.only('pk').get(pk=pk).description

    latest_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0:4]
    post = get_object_or_404(Post, pk=pk)
    tags = Tag.objects.all()
    cat_count = Category.objects.all().annotate(catcount=Count('post'))
    tag_count = Tag.objects.all().annotate(tagcount=Count('post'))
    post_count = Post.objects.count()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'title': title_text,
        'latest': latest_list,
        'tags': tags,
        'categories': cat_count,
        'tag_count': tag_count,
        'post_count': post_count,
        'description': description
        })
