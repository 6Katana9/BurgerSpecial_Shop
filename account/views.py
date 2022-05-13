from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import LoginForm, RegisterForm
from .models import UserProfile



def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                # if request.GET and 'next' in request.GET:
                #     return redirect(request.GET['next'])
                return redirect('/')
            else:
                form.add_error('login', 'Bad login or password')
                form.add_error('password', 'Bad login or password')
    else:
        form = LoginForm()

    return render(request, 'account/user.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'account/user.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('/')


def profile(request):
    return render(request, 'account/aboutuser.html')


def user_profiles(request):
    # user_id = User.objects.get(id)
    user_profile = UserProfile.objects.filter(user=request.user).first()
    return render(request, 'account/aboutuser.html', {'userprofile': user_profile})




