"""
portfolio URL Configuration

"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static


urlpatterns = [
    url(r'', include('home.urls')),
    url(r'^gmadmin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'^about/', include('home.urls')),
    url(r'^projects/', include('home.urls')),
    url(r'^contact/', include('home.urls')),
    url(r'^thanks/', include('home.urls')),
    url(r'^search/', include('home.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

# serving media files only on debug mode
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
	] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# origin patterns before removal
# urlpatterns = [
#     url(r'', include('home.urls')),
#     url(r'^gmadmin/', admin.site.urls),
#     url(r'^blog/', include('blog.urls')),
#     url(r'^about/', include('home.urls')),
#     url(r'^projects/', include('projects.urls')),
#     url(r'^contact/', include('home.urls')),
#     url(r'^thanks/', include('home.urls')),
#     url(r'^search/', include('home.urls')),
#     url(r'^ckeditor/', include('ckeditor_uploader.urls')),
# ]