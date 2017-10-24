from django.conf.urls import url, include
from django.views.generic import RedirectView
from . import views

app_name = 'projects'

urlpatterns = [
    url(r'^$', views.projects, name='projects'),
    url(r'^githubapi/$', views.githubapi, name='githubapi'),
    url(r'^weatherapi/$', views.weatherapi, name='weatherapi'),
    url(r'^todo/$', views.todo, name='todo'),
    url(r'^calculator/$', views.calculator, name='calculator'),
    url(r'^tictactoe/$', views.tictactoe, name='tictactoe'),
    url(r'^simonsays/$', views.simonsays, name='simonsays'),
    url(r'^votingapp/$', RedirectView.as_view(url='https://fcc-gmojo-vote.herokuapp.com/')),
    url(r'^markdown/$', RedirectView.as_view(url='https://fcc-markdown.herokuapp.com/')),
    url(r'^leaderboard/$', RedirectView.as_view(url='https://fcc-leaderboard-gmojo.herokuapp.com/')),
    url(r'^recipebox/$', RedirectView.as_view(url='https://fcc-gmojo-recipes.herokuapp.com/')),
    url(r'^metadata/$', RedirectView.as_view(url='https://file-metadata-gmojo.glitch.me/')),
    url(r'^imagesearch/$', RedirectView.as_view(url='https://image-search-gmojo.glitch.me/')),
    url(r'^timestamp/$', RedirectView.as_view(url='https://timestamp-gmojo.glitch.me/')),
    url(r'^whoami/$', RedirectView.as_view(url='https://header-parser-gmojo.glitch.me/')),
    url(r'^shorturl/$', RedirectView.as_view(url='https://gmfcc.glitch.me/')),
    url(r'^(?P<name>[-\w]+)/$', views.projectredirect, name='projectredirect'),
]