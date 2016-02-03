"""tracking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from tracking import views
from tracking.api.views import router as api_router
from tracking.api.internal.views import router as internalapi_router

urlpatterns = [
    url(r'^l/$', views.token_login, name='token_login'),
    url(r'^unauthorized/$', views.unauthorized, name='unauthorized'),
    url(r'^enquete/', include("tracking.enquete.urls")),
    url(r'^api/', include(api_router.urls)),
    url(r'^internalapi/', include(internalapi_router.urls)),
    url(r'^lottery/', "tracking.lottery.views.get_lottery", name='get_lottery'),
    url(r'^admin/', include(admin.site.urls)),
]
