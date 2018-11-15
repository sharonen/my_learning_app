from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.RandomLinksListView.as_view(), name='list'),
    url(r'^link/$', views.random_link_detail, name='detail'),
     url(r'^new/$', views.RandomLinksCreateView.as_view(), name= 'new'),
    url(r'^delete/(?P<pk>\d+)/$', views.RandonLinksDeleteView.as_view(), name='delete'),
]
