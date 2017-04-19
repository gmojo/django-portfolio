from django.shortcuts import render, HttpResponse, redirect
from django.utils import timezone
from .models import Projects
import requests
from string import capwords
import json
import pandas as pd

def weatherapi(request):
    title_text = 'Weather API - GarethMoger.com'
    description = Projects.objects.get(slug='weatherapi').description

    table_data = []
    if request.method == 'POST':
        form_site = request.POST.get('location')

        sitelist = requests.get('http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/sitelist?key=9f60b7c4-c1b8-4c99-beb3-0c0b697ea587')
        site_ids = sitelist.json()['Locations']['Location']

        site_id = ''
        for site in site_ids:
            if capwords(form_site) in site['name']:
                site_id += str(site['id'])
                break

        if not site_id:
            error = 'Location not found'
            return render(request, 'projects/weatherapi.html',
                          {'data': table_data, 'title': title_text, 'error': error})

        request_json = requests.get(
            'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/' +
            site_id +
            '?res=3hourly&key=9f60b7c4-c1b8-4c99-beb3-0c0b697ea587')

        period = request_json.json()['SiteRep']['DV']['Location']['Period']

        parsedData = []
        for day in period:
            for instance in day['Rep']:
                forecast = {}
                forecast['Date'] = day['value'][0:10]
                forecast['TempMax'] = int(instance['T'])
                forecast['TempMin'] = int(instance['T'])
                forecast['Wind'] = int(instance['S'])
                forecast['Rain'] = int(instance['Pp'])
                parsedData.append(forecast)

        df = pd.DataFrame(parsedData)
        df_agg = df.groupby('Date').agg({
            'TempMax': 'max',
            'TempMin': 'min',
            'Wind': 'mean',
            'Rain': 'max'
        })

        df_agg = df_agg.round(0)

        table_data.extend(json.loads(df_agg.reset_index().to_json(orient='records')))

    return render(request, 'projects/weatherapi.html', {
        'data': table_data,
        'title': title_text,
        'description': description
    })


def projectredirect(name):
    return redirect(name)


def projects(request):
    title_text = 'Projects - GarethMoger.com'
    description = 'My latest projects on the quest to further my data analysis and web development skills'
    projects = Projects.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'projects/projects.html', {
        'title': title_text,
        'projects': projects,
        'description': description
    })

def githubapi(request):
    title_text = 'GitHub API - GarethMoger.com'
    description = Projects.objects.get(slug='githubapi').description

    parsedData = []
    if request.method == 'POST':
        username = request.POST.get('user')
        req = requests.get('https://api.github.com/users/' + username)
        jsonList = []
        jsonList.append(req.json())

        if 'message' in jsonList[0]:
            error = 'User not found'
            return render(request, 'projects/githubapi.html', {'data': parsedData, 'title': title_text, 'error': error})

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
    return render(request, 'projects/githubapi.html', {
        'data': parsedData,
        'title': title_text,
        'description': description
    })
