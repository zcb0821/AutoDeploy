"""bigdata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

from account import views as account_views
from deployment import views as deployment_views

urlpatterns = [
    url(r'^$', deployment_views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', account_views.login, name='login'),
    url(r'^accounts/logout/$', account_views.logout, name='logout'),
    url(r'^accounts/register/$', account_views.register, name='register'),
]

urlpatterns += [
    url(r'^clusters/$', deployment_views.clusters, name='clusters'),
    url(r'^clusters/([a-z\-\d]+)/$', deployment_views.cluster),
    url(r'^rest/clusters/$', deployment_views.rest_clusters),
    url(r'^rest/clusters/([a-z\-\d]+)/$', deployment_views.rest_cluster),
    url(r'^rest/clusters/([a-z\-\d]+)/status/$', deployment_views.rest_status),
    url(r'^rest/uuid/', deployment_views.generate_uuid)
]

urlpatterns += [
    url(r'^rest/assist/', deployment_views.assist),
    url(r'^rest/selectsystem/', deployment_views.selectsystems)
]
