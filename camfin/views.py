# from django.shortcuts import render

# def index(request)
#   return render(request, 'index.html')
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from twilio.twiml import Response
 
@csrf_exempt
def sms(request):
    # r = Response()
    # r.message('Hello from your Django app!')
    # return HttpResponse(r.toxml(), content_type='text/xml')
    twiml = '<Response><Message>Hello from your Django app!</Message></Response>'
    return HttpResponse(twiml, content_type='text/xml')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
          form.save()
          return HttpResponseRedirect('/accounts/register/complete')

    else:
        form = UserCreationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form
    return render(request, 'accounts/register.html', token)

def registration_complete(request):
    return render(request, 'accounts/registration_complete.html')