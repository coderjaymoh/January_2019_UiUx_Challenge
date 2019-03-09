# works with both python 2 and 3
from __future__ import print_function

import africastalking

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
		recipients = ["+254717771518"]

		# Set your message
		message = "Testing 2-factor auth";

		try:
			# Thats it, hit send and we'll take care of the rest.
			response = self.sms.send(message, recipients)
			print (response)
		except Exception as e:
			print ('Encountered an error while sending: %s' % str(e))

if __name__ == '__main__':
	SMS().send()
