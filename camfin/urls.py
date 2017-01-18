"""camfin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
# from django.conf.urls import url
# from django.contrib import admin

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]
# from django.contrib.auth import views as auth_views
# from camfin import views as camfin_views

from django.views.decorators import csrf
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib import auth
from django.contrib import admindocs
# from students.views import hello
from django.contrib.auth import views as auth_views
from students.forms import LoginForm
from students.forms import ModelForm
# from students.forms import LogoutForm
from students import views as student_views
from camfin import views as camfin_views
# from django.contrib.auth import signup
# from camfin import views as camfin_views


admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'djtwilio.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'', include('students.urls')),
    url(r'^accounts/register/$', camfin_views.register, name='register'),
    url(r'^accounts/register/complete/$', camfin_views.registration_complete, name='registration_complete'),

    # url(r'^signup/$', auth_views.signup, {'template_name': 'signup.html', 'model_form': ModelForm}), 
    url(r'^login/$', auth_views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}), 
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}),
    url(r'^$', student_views.index, name='index'),
       # url(r'^blog/', include('blog.urls')),
    url(r'^hello/$', student_views.hello, name='hello'),


    # url(r'^admin/doc/', include(django.contrib.admindocs.urls)),
    url(r'^sms/$', student_views.sms, name='sms'),
    url(r'^sms_two/$', student_views.sms_two, name='sms_two'),
    url(r'^ring/$', student_views.ring, name='ring'),
    # url(r'^accounts/login/$', student_views.login, name ='login'),
    # url(r'^accounts/auth/$', student_views.auth_view, name ='auth_view'),
    # url(r'^accounts/logout/$', student_views.logout, name ='logout'),
    # url(r'^accounts/loggedin/$', student_views.loggedin, name ='loggedin'),
    # url(r'^accounts/invalid/$', student_views.invalid_login, name ='invalid_login'),
 
    # Here we add our Twilio URLs
    # url(r'^sms/$', camfin.views.sms, name='sms'),
    # url(r'^ring/$', camfin.views.ring, name='ring'),
]