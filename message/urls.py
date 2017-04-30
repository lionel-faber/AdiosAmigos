from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<num>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<num>[0-9]+)/submit/$', views.submit, name='submit'),
    url(r'^dearsenior/$', views.dear, name='dear'),
    url(r'^dearsenior/reg/$', views.reg, name='reg'),
    url(r'^dearsenior/login/$', views.login, name='login'),
    url(r'^dearsenior/reg/show$', views.regviewmsg, name='regviewmsg'),
    url(r'^dearsenior/login/show/$', views.loginviewmsg, name='loginviewmsg'),
]
