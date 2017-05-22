from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, health, viewfb

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^health$', health),
    url(r'^firebase$', viewfb),
    url(r'^admin/', include(admin.site.urls)),
]
