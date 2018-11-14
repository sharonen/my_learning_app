from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.urls_list, name='list'),
    url(r'^(?P<pk>\d+)/$', views.urls_detail, name='detail'),
]
