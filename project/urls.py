from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'project.views.home'),
    
    url(r'^sys', 'project.views.sys'),
    
    
    url(r'^accounts/login/$', 'project.views.login'),
    url(r'^accounts/auth/$', 'project.views.auth_views'),
    url(r'^accounts/logout/$', 'project.views.logout'),
    url(r'^accounts/loggedin/$', 'project.views.loggedin'),
    url(r'^accounts/invalid/$', 'project.views.invalid_login'),
    url(r'^accounts/register/$', 'project.views.register_user'),
    url(r'^accounts/register_success/$', 'project.views.register_success'),
    
)
