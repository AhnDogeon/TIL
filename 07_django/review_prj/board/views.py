from django.shortcuts import render
from .models import Article

# Create your views here.

# id 불필요
def article_new(request):
    pass

def article_create(request):
    pass

# id 필요
def article_list(request):
    pass

def article_detail(request):
    pass

def article_edit(request):
    pass


def article_update(request):
    pass

def article_delete(request):
    pass







def index(request):
    return render(request, 'board/index.html')


def greeting(request, name, role):
    if role == 'admin':
        return render(request, 'board/greeting.html', {
            'role': 'MASTER USER',
            'name': name.upper(),
        })
    else:
        return render(request, 'board/greeting.html', {
            'role': role,
            'name': name,
        })
