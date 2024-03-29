from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.


def index(request):
    return render(request, 'accounts/index.html')


def signup(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:index')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })


def signin(request):
    # 이미 로그인 했는데 또 로그인 하러 간다하면
    if request.user.is_authenticated:
        return redirect('accounts:index')
    # 로그인 시켜주세요
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid(): # 검증성공
            login(request, form.get_user()) # 로그인 하기

            if request.GET.get('next'): # 이전에 없던 페이지가 있다면,
                return redirect(request.GET.get('next'))

            return redirect('accounts:index')
    # 로그인 화면주세요
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/signin.html', {
            'form': form
        })


def signout(request):
    logout(request)
    return redirect('accounts:index')