"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sports/$', sports_list),
    url(r'^get_sport/(?P<pk>[0-9]+)$', get_sport),
    url(r'^add_sport/$', new_sport),

    url(r'^players/$', players_list),
    url(r'^get_player/(?P<pk>[0-9]+)$', get_player),
    url(r'^add_player/$', new_player),

    url(r'^players_from_sport/(?P<fk>[0-9]+)$', players_list_from_sport),


]
