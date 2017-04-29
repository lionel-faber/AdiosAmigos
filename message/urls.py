from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<num>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<num>[0-9]+)/submit/$', views.submit, name='submit'),
    url(r'^dearsenior/$', views.dear, name='dear'),
    url(r'^dearsenior/(?P<num>[0-9]+)/$', views.viewmsg, name='viewmsg'),
]
