from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone
from blog.models import Post
from projects.models import Projects
from django.db.models import Q
from .forms import ContactForm


def search(request):
    query = request.GET.get('query')
    title = 'Search: ' + query
    description = 'Search results'
    results = Post.objects.filter(Q(title__icontains=query) | Q(text__icontains=query)).order_by('-published_date')
    return render(request, 'home/search.html', {
        'results': results,
        'title': title,
        'description': description
    })


def home(request):
    title_text = 'GarethMoger.com - Data & Development'
    description = 'Data & Development - Building skills together in data analysis and software development'
    post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0:2]
    projects = Projects.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0:4]
    return render(request, 'home/home.html', {
        'posts': post_list,
        'title': title_text,
        'projects': projects,
        'description': description
    })


def about(request):
    title_text = 'About - GarethMoger.com'
    description = "I support the full developement cycle of corporate systems and provide key information from them, utilising SQL, Python, database knowledge and analysis techniques. Currently I am interested in managing and visualising data online using Python's Django framework from which to build on."
    return render(request, 'home/about.html', {'title': title_text, 'description': description})


def contact(request):
    title_text = 'Contact - GarethMoger.com'
    description = 'Contact me on the form or via the social media links at the top of the page'
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            content = form.cleaned_data['content']
            try:
                email = EmailMessage(contact_name,
                                    content,
                                    contact_email,
                                    ['mogerweb@gmail.com'],
                                     reply_to=[contact_email],
                                   )
                email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('./thanks/')
    return render(request, 'home/contact.html', {'title': title_text, 'form': form, 'description': description})


def thanks(request):
    title_text = 'Thank you! - GarethMoger.com'
    return render(request, 'home/thanks.html', {'title': title_text})
