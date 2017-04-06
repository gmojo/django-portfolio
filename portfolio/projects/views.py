from django.shortcuts import render, HttpResponse, redirect
from django.utils import timezone
from .models import Projects
import requests

def projectredirect(name):
    return redirect(name)

def projects(request):
    title_text = 'Projects - GarethMoger.com'
    projects = Projects.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'projects/projects.html', {'title': title_text, 'projects': projects})

def githubapi(request):
    title_text = 'GitHub API - GarethMoger.com'

    parsedData = []
    if request.method == 'POST':
        username = request.POST.get('user')
        req = requests.get('https://api.github.com/users/' + username)
        jsonList = []
        jsonList.append(req.json())
        userData = {}
        for data in jsonList:
            userData['name'] = data['name']
            userData['blog'] = data['blog']
            userData['email'] = data['email']
            userData['public_gists'] = data['public_gists']
            userData['public_repos'] = data['public_repos']
            userData['avatar_url'] = data['avatar_url']
            userData['followers'] = data['followers']
            userData['following'] = data['following']
        parsedData.append(userData)
    return render(request, 'projects/githubapi.html', {'data': parsedData, 'title': title_text})
