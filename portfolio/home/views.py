from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone
from blog.models import Post
from .forms import ContactForm

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

def contact(request):
    title_text = 'Contact'
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            content = form.cleaned_data['content']
            try:
                send_mail(contact_name, content, contact_email, ['mogerweb@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('./thanks/')
    return render(request, 'home/contact.html', {'title': title_text,'form': form})

def thanks(request):
    title_text = 'Thank you!'
    return render(request, 'home/thanks.html', {'title': title_text})