from django.conf.urls import url
from basic_app import views

#TEMPLATE TAGGING
"""
Whenever we are going to use template tagging we should
set up a global variable 'app_name'. Django is automatically going to
look for this and it will look under the basic_app and will
find the url that matches.
"""
app_name = 'basic_app'

urlpatterns = [
    url(r'^relative/$', views.relative, name = 'relative'),
    url(r'^other/$', views.other, name = 'other'),
]
