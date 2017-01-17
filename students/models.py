from __future__ import unicode_literals

from django.db import models

from django.conf import settings

from phonenumber_field.modelfields import PhoneNumberField


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


# Create your models here.

# from django.utils.encoding import python_2_unicode_compatible

class Mobile(models.Model):
    mobile_number = models.CharField(max_length=200)
    pin_number = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.mobile_number
        return self.pin_number

class Student(models.Model):
    name = models.CharField(max_length=200)
    pin = models.ForeignKey(Mobile, on_delete=models.CASCADE)
    # mobile_number = models.ForeignKey(Mobile, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.name
        return self.mobile_number
        return self.class_name