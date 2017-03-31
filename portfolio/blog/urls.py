from django.conf.urls import url, include
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.posts, name='posts'),
    url(r'^post/(?P<pk>\d+)/(?P<slug>[\w-]+)$', views.post_detail, name='post_detail'),
    url(r'^category/(?P<name>[-\w]+)/$', views.category, name='category'),
    url(r'^tag/(?P<name>[-\w]+)/$', views.tag, name='tag'),
]