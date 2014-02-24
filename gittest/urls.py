from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'gittest.views.home', name='home'),
    url(r'^blog/', include('blog.urls')),
    url(r'^newsite/', 'gittest.views.home', name='newsite'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', 'gittest.views.test', name='test'),
)
