from __future__ import print_function
from smsauth.sms import SMS as sms
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import signupForm, verifyForm
from .models import signup, verify
import africastalking
import random

message = ''.join(random.sample("0123456789", 4))

class SMS:
	def __init__(self):
		# Set your app credentials
		self.username = "hairwayskenya"
		self.api_key = "cf3cc2363d56f31846e96b2bc006c37ebd5f623bcc4982dbf2b0c6783c31d485"

		# Initialize the SDK
		africastalking.initialize(self.username, self.api_key)

		# Get the SMS service
		self.sms = africastalking.SMS

	def send(self):
		# Set the numbers you want to send to in international format
		recipient = ["+254717771518"]

		try:
			# Thats it, hit send and we'll take care of the rest.
			response = self.sms.send(message, recipient)
			print (response)
		except Exception as e:
			print ('Encountered an error while sending: %s' % str(e))

if __name__ == '__main__':
	SMS().send()


def register(request):
    details = signup.objects.all()

    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['username']
            recipient = form.cleaned_data['phone']
            print(name)
            print(recipient)

            sending = SMS()
            sending.send()
            print(message)

            print('*****************************   Sending activation code ' + message + ' to ' + recipient)
            register = form.save()
            return redirect('verifyUser')
    form = signupForm()
    return render(request, "signup.html", {'form' : form, 'details' : details})

def verifyUser(request):
    if request.method == 'POST':
        form = verifyForm(request.POST)
        if form.is_valid():
            print(message)
            code = form.cleaned_data['smscode']
            if message != code:
                print('Input code matches Sent Code')
                return redirect('verifyUser')

            else:
                print('Input code matches sent code')
                return redirect('signupsuccess')

            print('___________________valid sms form')
            verify = form.save()

    form = verifyForm()
    return render(request, "verify.html", {'form' : form})

def signupsuccess(request):
    return render(request, 'signupsuccess.html')
