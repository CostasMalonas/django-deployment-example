"""learning_templates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from basic_app import views
urlpatterns = [

    # Basically the line below says that when someone goes to
    # 127.0.0.800 bring me the index view, so it calls the view
    # directly from the function.

    url(r'^$', views.index, name = 'index'),
    url(r'^admin/', admin.site.urls),

    # What the below line does is that when someone hits,
    # let's say basic_app/relative or basic_app/other e.t.c it goes
    # to the urls.py file inside the application and from there the view
    # gets called.
    #
    url(r'^basic_app/', include('basic_app.urls'))
]
