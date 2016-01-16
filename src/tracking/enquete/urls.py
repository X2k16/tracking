from django.conf.urls import include, url
from tracking.enquete import views
urlpatterns = [
    url(r'^$', views.index, name='enquete_index'),
    url(r'^program/(\d+)/$', views.program_enquete, name='enquete_program'),
]
