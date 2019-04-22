from django.shortcuts import render,redirect,get_object_or_404, HttpResponseRedirect
from django.views.decorators.http import require_GET,require_POST,require_http_methods
from .forms import CustomUserCreateForm, CustomUserAuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from posts.forms import CommentModelFrom
from .models import User
# from django.contrib.auth import get_user_model # 밑에랑 둘중하나 선택
# Create your views here.


@require_http_methods(['GET','POST'])
def signup(request):
   if request.method == 'POST':
       form = CustomUserCreateForm(data=request.POST)
       if form.is_valid():
           user = form.save()
           return redirect('posts:post_list')

   else:
       form = CustomUserCreateForm()

   return render(request,'accounts/signup.html',{
       'form':form
   })


@require_http_methods(['GET', 'POST'])
def login(request):
   # 우선 사용자가 로그인 되어 있는지?
   if request.user.is_authenticated:
       return redirect('posts:post_list')
   # 로그인 안 되어 있다면
   else:
       # 사용자가 로그인 데이터를 넘겼을 때
       if request.method == 'POST':
           form = CustomUserAuthenticationForm(request, data=request.POST)
           if form.is_valid():
               user = form.get_user()
               auth_login(request, form.get_user())
               messages.add_message(request, messages.SUCCESS, f'Welcome back', {user.username})
               messages.add_message(request, messages.INFO, f'Last login', {user.last_login})
               return redirect(request.GET.get('next') or 'posts:post_list')
       # 사용자가 로그인 화면을 요구할 때
       else:
           form = CustomUserAuthenticationForm()
       return render(request, 'accounts/login.html', {
           'form': form,
       })


def logout(request):
   auth_logout(request)
   messages.add_message(request, messages.SUCCESS, f'Logout Successfully')
   return redirect('posts:post_list')


def user_detail(request, username):
    user_info = User.objects.get(username=username)
    return render(request, 'accounts/user_detail.html', {
        'user_info': user_info,
        'comment_form': CommentModelFrom()
    })


@login_required
@require_POST
def toggle_follow(request, username):
    sender = request.user
    receiver = get_object_or_404(User, username=username)

    if sender != receiver:
        if receiver in sender.followings.all():
            # unfollow
            sender.followings.remove(receiver)
        else:
            # follow
            sender.followings.add(receiver)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/insta/'))