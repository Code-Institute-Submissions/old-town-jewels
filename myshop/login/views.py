from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def login(request):
    if request.method == 'POST':
        #Login form
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, "User logged in successfully")
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR, "Invalid username or password")
            return redirect('login')

    else:
        context = {
            'request':request,
        }
        return render(request, 'login.html', context)

