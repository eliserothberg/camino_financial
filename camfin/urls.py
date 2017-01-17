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
from django.contrib import admin

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]
# from django.contrib.auth import views as auth_views
# from camfin import views as camfin_views
from students import views


from django.conf.urls import include, url
 
# from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
 
urlpatterns = [
    # Examples:
    # url(r'^$', 'djtwilio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
 
    url(r'^admin/', include(admin.site.urls)),
 
    # Here we add our Twilio URLs
    # url(r'^sms/$', camfin.views.sms, name='sms'),
    # url(r'^ring/$', camfin.views.ring, name='ring'),
]