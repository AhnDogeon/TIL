from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

# id 불필요
def article_new(request):
    return render(request, 'board_ad/new.html')

def article_create(request):
    article = Article()
    article.title = request.POST.get('input_title')
    article.content = request.POST.get('input_content')
    article.save()
    return redirect(f'/board_ad/articles/{article.id}')

# id 필요
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'board_ad/list.html', {
        'articles': articles,
    })


def article_detail(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'board_ad/detail.html', {
        'article': article,
    })


def article_edit(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'board_ad/edit.html', {
        'article': article,
    })


def article_update(request, id):
    article = Article.objects.get(id=id)
    article.title = request.POST.get('input_title')
    article.content = request.POST.get('input_content')
    article.save()
    return redirect(f'/board_ad/articles/{article.id}')


def article_delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('/board_ad/articles/')



def index(request):
    return render(request, 'board_ad/index.html')


def greeting(request, name, role):
    if role == 'admin':
        return render(request, 'board_ad/greeting.html', {
            'role': 'MASTER USER',
            'name': name.upper(),
        })
    else:
        return render(request, 'board_ad/greeting.html', {
            'role': role,
            'name': name,
        })
