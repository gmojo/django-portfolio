from django.conf.urls import url, include
from . import views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.home),
    url(r'^contact/$', views.home),
    url(r'^thanks/$', views.home),
    url(r'^search/$', views.home),
    url(r'^blog/$', views.home),
    url(r'^projects/$', views.home)
]

# urlpatterns = [
#     url(r'^$', views.home, name='home'),
#     url(r'^about/$', views.about, name='about'),
#     url(r'^contact/$', views.contact, name='contact'),
#     url(r'^thanks/$', views.thanks, name='thanks'),
#     url(r'^search/$', views.search, name='search'),
# ]