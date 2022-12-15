from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request, "Email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(
                username = username, password = password1, email = email,
                last_name = last_name, first_name = first_name)
                user.save()
                print("user created")
        else:
            if User.objects.filter(username = request.GET.get('username')).exists() or User.objects.filter(email = request.GET.get('email')).exists():
            messages.info("password not matching")

            else:
                context = {
                'request':request,
                }
        return render(request, 'register.html', context)