from django.conf.urls import include, url
from . import views
from django.contrib import admin
from django.views.decorators import csrf
from students import views

urlpatterns = [
  url(r'^$', views.home, name='home'),
    # url(r'^students/', include('students.urls')),
    # url(r'^admin/', admin.site.urls),
    # url(r'^hello/$', students.views.hello, name='hello'),

    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^sms/$', students.views.sms, name='sms'),
    # url(r'^ring/$', students.views.ring, name='ring'),
    # url(r'^accounts/login/$', students.views.login, name ='login'),
    # url(r'^accounts/auth/$', students.views.auth_view, name ='auth_view'),
    # url(r'^accounts/logout/$', students.views.logout, name ='logout'),
    # url(r'^accounts/loggedin/$', students.views.loggedin, name ='loggedin'),
    # url(r'^accounts/invalid/$', students.views.invalid_login, name ='invalid_login'),
 

]