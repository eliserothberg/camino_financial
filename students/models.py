from __future__ import unicode_literals

from django.db import models

from django.conf import settings

from phonenumber_field.modelfields import PhoneNumberField
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

TWILIO_ACCOUNT_SID = 'ACe340c958d3475ee038f5a3512d224fee'
TWILIO_AUTH_TOKEN = 'caa016c683a651cd690bee64c9839a08'

SID = 'TWILIO_ACCOUNT_SID'
AUTH = 'TWILIO_AUTH_TOKEN'
# Create your models here.

# from django.utils.encoding import python_2_unicode_compatible

class SMSVerification(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, default='blank')
    verified = models.BooleanField(default=False)
    pin = get_random_string(length=6, allowed_chars='1234567890')
    sent = models.BooleanField(default=False)
    phone = PhoneNumberField(null=False, blank=False)
 
    def send_confirmation(self):
 
        logger.debug('Sending PIN %s to phone %s' % (self.pin, self.phone))
 
        if phonenumbers.is_valid_number(self.phone):
            if all([settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN, settings.TWILIO_FROM_NUMBER]):
                try:
                    twilio_client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
                    twilio_client.messages.create(
                        body="Your PIN is %s" % self.pin,
                        to=str(self.user.userprofile.phone),
                        from_=settings.TWILIO_FROM_NUMBER
                    )
                    self.sent = True
                    self.save()
                    return True
                except TwilioException, e:
                    logger.error(e)
            else:
                logger.warning('Twilio credentials are not set')
        return False
 
    def confirm(self, pin):
        if self.pin == pin:
            self.user.auth_token.delete()
            self.user.auth_token = TokenModel.objects.create(user=self.user)
            self.verified = True
            self.save()
 
        return self.verified
 
 
# @receiver(user_signed_up)
def send_sms_verification(request, user, **kwargs):
    verification = SMSVerification.objects.create(user=user, phone=user.userprofile.phone)
    verification.send_confirmation()

# class Mobile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     mobile_number = models.CharField(max_length=200)
#     pin = models.ForeignKey(SMSVerification, on_delete=models.CASCADE)
#     pub_date = models.DateTimeField('date published')
#     def __str__(self):
#         return self.mobile_number
#         return self.pin

class Student(models.Model):
    name = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pin = models.ForeignKey(SMSVerification, on_delete=models.CASCADE)
    # mobile_number = models.ForeignKey(Mobile, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.name
        return self.mobile_number
        return self.class_name