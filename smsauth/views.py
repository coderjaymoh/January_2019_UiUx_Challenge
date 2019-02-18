from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import signupForm, verifyForm
from .models import signup, verify

import africastalking

def register(request):
    details = signup.objects.all()

    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            print('__________________valid registration form')
            register = form.save()
            return redirect('verifyUser')
    form = signupForm()
    return render(request, "signup.html", {'form' : form, 'details' : details})

def verifyUser(request):
    if request.method == 'POST':
        form = verifyForm(request.POST)
        if form.is_valid():
            print('___________________valid sms form')
            verify = form.save()
            return redirect('verifyUser')
    form = verifyForm()
    return render(request, "verify.html", {'form' : form})
