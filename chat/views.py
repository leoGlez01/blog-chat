from django.shortcuts import render, redirect
from .forms import FormLogin
from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == 'POST':
        form = FormLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('chat-page')


    else:
        form = FormLogin()
    return render(request, 'loginPage.html', {'form': form})


def home(request):
    context={}
    return render(request, 'chatPage.html', context=context)