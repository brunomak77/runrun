from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def register_view(request):
    if request.method == 'POST':
        new_userForm = UserCreationForm(request.POST)
        if new_userForm.is_valid():
            new_userForm.save()
            return redirect('login')
    else:
        new_userForm = UserCreationForm()

    return render(request, 'register.html', {'new_user': new_userForm})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/calendario')
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form})


def logout_view(request):
    logout(request)
    return redirect('login')