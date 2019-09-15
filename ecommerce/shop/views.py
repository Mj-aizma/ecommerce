from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Object

# from .models import ContactUs
######################################
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

import datetime
# Create your views here.

def index(request):
    object = Object.objects.reverse().all()[:4]
    context = {
        'objects' : object,
    }
    return render(request, 'shop/index.html', context)


# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('/')
#     else:
#         form = UserCreationForm()
#     return render(request, 'shop/signup.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'shop/signup.html', {'form': form})
