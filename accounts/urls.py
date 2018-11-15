from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'signin/', views.SignIn.as_view(), name='signin'),
]