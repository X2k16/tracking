from django.conf.urls import include, url
from tracking.demo import views

urlpatterns = [
    url(r'^$', views.index, name='demo_index'),
]
