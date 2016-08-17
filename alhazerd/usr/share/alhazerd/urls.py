from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'alhazerd.views.home', name='home'),
    # url(r'^alhazerd/', include('alhazerd.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'alhazerd.uploader.views.index'),
    url(r'^logon/$', 'alhazerd.uploader.views.logon'),
    url(r'^logoff/$', 'alhazerd.uploader.views.logoff'),
    url(r'^register/$', 'alhazerd.uploader.views.register'),
    url(r'^send/$', 'alhazerd.uploader.views.upload_picture'),
    url(r'^picture/(?P<picture_id>\d+)/$', 'alhazerd.uploader.views.show_user_picture'),
    url(r'^picture/(?P<picture_id>\d+)/delete/$', 'alhazerd.uploader.views.delete_user_picture'),
    url(r'^user/(?P<username>[0-9a-zA-Z@_\+\.\-]+)/$', 'alhazerd.uploader.views.list_user_gallery'),
)
