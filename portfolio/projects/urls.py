from django.conf.urls import url, include
from . import views

app_name = 'projects'

urlpatterns = [
    url(r'^$', views.projects, name='projects'),
    url(r'^githubapi/$', views.githubapi, name='githubapi'),
    url(r'^weatherapi/$', views.weatherapi, name='weatherapi'),
    url(r'^todo/$', views.todo, name='todo'),
    url(r'^(?P<name>[-\w]+)/$', views.projectredirect, name='projectredirect'),
]