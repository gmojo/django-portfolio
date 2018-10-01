from django.conf.urls import url, include
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.posts, name='posts'),
    url(r'^category/(?P<cat>[-\w]+)/$', views.posts, name='posts'),
    url(r'^tag/(?P<tag>[-\w]+)/$', views.posts, name='posts'),
    url(r'^post/(?P<pk>\d+)/(?P<slug>[\w-]+)$', views.post_detail, name='post_detail'),
]

# urlpatterns = [
#     url(r'^$', views.posts, name='posts'),
#     url(r'^category/(?P<cat>[-\w]+)/$', views.posts, name='posts'),
#     url(r'^tag/(?P<tag>[-\w]+)/$', views.posts, name='posts'),
#     url(r'^post/(?P<pk>\d+)/(?P<slug>[\w-]+)$', views.post_detail, name='post_detail'),
# ]