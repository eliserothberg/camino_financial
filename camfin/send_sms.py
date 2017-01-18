# we import the Twilio client from the dependency we just installed
from twilio.rest import TwilioRestClient

# the following line needs your Twilio Account SID and Auth Token
client = TwilioRestClient("ACe340c958d3475ee038f5a3512d224fee", "caa016c683a651cd690bee64c9839a08")
# accountSID = 'ACe340c958d3475ee038f5a3512d224fee'
# authToken = 'caa016c683a651cd690bee64c9839a08'
# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+12134351393", from_="+12138143752", 
                       body="Hello from Python!")