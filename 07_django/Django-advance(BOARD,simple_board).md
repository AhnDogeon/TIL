# Django-advance/BOARD/simple_board

```
ryungs:~/workspace $ pip list 
# 원래는 pip list 했을때 global에는 Django 있으면 안됨
# 개별 환경 설정이기 때문에, 우리는 계속 여기다가 작업해서 깔려있는 거임
Package    Version
---------- -------
Django     2.1.5  
pip        18.1   
pytz       2018.9 
setuptools 40.6.2 

# mkdir로 새롭게 프로젝트 생성하는 방법
ryungs:~/workspace $ mkdir BOARD
ryungs:~/workspace $ cd BOARD/

# mkdir 자체에 virtualenv, local 씌우기
ryungs:~/workspace/BOARD $ pyenv virtualenv 3.6.8 BOARD                                 ryungs:~/workspace/BOARD $ pyenv local BOARD 

#원하는 프로젝트에 들어가서 Django install하기
(BOARD) ryungs:~/workspace/BOARD $ pip list
Package    Version
---------- -------
pip        18.1   
setuptools 40.6.2 
#이거 3개는 고정
(BOARD) ryungs:~/workspace/BOARD $ pip install django django-extensions ipython 

# startproject 할때 띄워쓰기. 하기
(BOARD) ryungs:~/workspace/BOARD $ django-admin startproject board .
(BOARD) ryungs:~/workspace/BOARD $ django-admin startapp simple_board
(BOARD) ryungs:~/workspace/BOARD $ mkdir -p  simple_board/templates/simple_board
(BOARD) ryungs:~/workspace/BOARD $ python manage.py makemigrations simple_board
(BOARD) ryungs:~/workspace/BOARD $ python manage.py migrate

```

```python
# models.py 가서 class Article, Comment 생성하기

from django.db import models
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default='')
    like = models.IntegerField() # 여기 default 값 비워서 makemigrations 하면 에러 안남
    
    def __str__(self):
        return f'{self.id}: {self.title}'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.article.title}: {self.content}'
 
------------------------------------------------------------------------------       
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default='')
    like = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.id}: {self.title}'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    like = models.IntegerField()# 여기 default 값 비워서 makemigrations 하면 에러 남
    
    def __str__(self):
        return f'{self.article.title}: {self.content}
```

```bash
(BOARD) ryungs:~/workspace/BOARD $ python manage.py makemigrations simple_board
You are trying to add a non-nullable field 'like' to comment without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
 
# 1번 방법 : 자동으로 넣어줘! 좋은 방법 아니다
Select an option: 1
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> 0
Migrations for 'simple_board':
  simple_board/migrations/0002_auto_20190207_1109.py
    - Add field like to comment
    - Alter field like on article
    
# 2번 방법: 일단 나가고 내가 직접 고칠게! 추천
Select an option: 2
# 하고 직접 models.py 파일 가서 수정하기

# 새로 migrate 하기
(BOARD) ryungs:~/workspace/BOARD $ python manage.py migrate
```



```bash
# shell_plus 켜서
(BOARD) ryungs:~/workspace/BOARD $ python manage.py shell_plus

# 1:n 생성하기, views에 들어가는 로직
In [1]: a = Article(title='HI', content='New article')                                                                                                                        
In [2]: a.save()                                                                                                                                                               
In [3]: a                                                                                Out[3]: <Article: 1: HI>

In [4]: a.like                                                                         Out[4]: 0

In [5]: a.comment_set                                                                  
Out[5]: <django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager at 0x7fc6681d91d0>

In [6]: a.comment_set.create(content='wow!')                                           
Out[6]: <Comment: HI: wow!>

In [7]: c = Comment() # 행추가                                                                                                                                                   
In [8]: c.content='Good to see you' # 행에 글만 적음                                     

In [9]: c.article = a # Article id=1 생성 c_id=2
In [10]: c.save() # 이제서야 데이터 베이스에 저장
```

```bash
(BOARD) ryungs:~/workspace/BOARD $ python manage.py runserver $IP:$PORT
(BOARD) ryungs:~/workspace/BOARD $ python manage.py createsuperuser
```

```python
# admin.py가서 등록

from django.contrib import admin
from .models import Article, Comment # models에서 생성된 2개를 가져온다

# Register your models here.
admin.site.register([Article, Comment])
```

```
https://django-advance-ryungs.c9users.io/admin/ 가면
Articles, Comments 생성되어 있음
```

```python
# views.py랑 urls.py 가서 맴핑하기

# 5개 urls 생성
from django.urls import path
from . import views

app_name = 'simple_board'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('create/', views.article_create, name='article_create'),
    path('<int:id>/', views.article_detail, name='article_detail'),
    path('<int:id>/update/', views.article_update, name='article_update'),
    path('<int:id>/delete/', views.article_delete, name='article_delete'),
]

# 5개 urls 생성에서 <int:article_id>를 명시적으로 수정

from django.urls import path
from . import views

app_name = 'simple_board' # app name 지정

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('create/', views.article_create, name='article_create'),
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    path('<int:article_id>/update/', views.article_update, name='article_update'),
    path('<int:article_id>/delete/', views.article_delete, name='article_delete'),
]



# views.py 생성

from django.shortcuts import render, get_object_or_404
from .models import Article, Comment

# Create your views here.
def article_list(request):
    articles = Article.objects.all()
    
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    
    
def article_create(request):
    if request.method == 'GET':
        pass #template
    
    else:
        article = Article()
        article.title = request.POST #unknown
        article.content = request.POST #unknown
        article.save()

def article_update(request):
    pass
    
def article_delete(request):
    pass

# html 생성
- base.html
- detail. html
- list.html
- edit.html
- new.html



#view.py 가서 detail. html list.html 채우기
from django.shortcuts import render, get_object_or_404

from .models import Article, Comment

# Create your views here.
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'simple_board/list.html', {
        'articles' : articles, 
    })
    
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'simple_board/detail.html', {
        'article' : article, 
    })
    
    
def article_create(request):
    if request.method == 'GET':
        pass #template
    
    else:
        article = Article()
        article.title = request.POST #unknown
        article.content = request.POST #unknown
        article.save()

def article_update(request):
    pass
    
def article_delete(request):
    pass

```

```html
<!-- list html 채워나가기 -->
{% extends 'simple_board/base.html' %}

{% block body %}
<h1>All Articles</h1>
{% if articles %}
<ul>
    {% for article in articles %}
        <li><a href="{% url 'simple_board:article_detail' article.id %}">
             {{ article.title }}
            </a>
        </li>
    {% endfor %}
    
</ul>
{% endif %}

{% endblock %}
```





```html
<!-- detail html 채워나가기 -->

{% extends 'simple_board/base.html' %}

{% block body %}
<h1>{{ article.title }}</h1> 

<p>
    {{ article.content }}
</p>

<hr/>

<div>
    <a href="{% url 'simple_board:article_list' %}"><button>목록으로 가기</button></a>
</div>
<div>
    <a href="{% url 'simple_board:article_update' article.id %}"></a><button>수정하러 가기</button></a>
</div> 
<form action="{% url 'simple_board:article_delete' article.id %}" method="POST"><button>삭제하러 가기</button></form>

<hr/>

<form action="#" method="POST">
    {% csrf_token %}
    <label for="comment">leave comment</label>
    <input id="comment" type="text" name="comment"/>
    <input type="submit" value="댓글작성"/>
</form>
{% endblock %}
```



```python
# new.html, edit.html 채우는건 뒤 후순위로 미루고
# 댓글의 new가 더 중요하니까 이거 먼저하겠다
# 다시 views.py로 가서
# 댓글을 생성하는 create가 필요하기 때문에 comment_create라고 지었다
# 추가하기

"""
actions about model Comment
"""
def comment_create(request):
    pass
       
def comment_delete(request):
    pass 
```



```python
# urls.py 가서 생성한 def 등록하기

# URL about comments
    # /simple_board/1/comments/create
    path('<int:article_id>/comments/create/', views.comment_create, name='comment_create'),
    # /simple_board/1/comments/2/delete
    path('<int:article_id>/comments/<int:comment_id>/delete/', views.comment_delete, name="comment_delete"),  
```



```python
# 다시 views.py로 가서

"""
actions about model Comment
"""
def comment_create(request, article_id):
    if request.method == 'POST':
        comment = Comment()
        comment.content = request.POST.get('content')
        comment.article = get_object_or_404(Article, id=article_id) 
        # 여기서 comment.article 뒤에 적을 말을 생각해보자! 
        # detail.html에서 input을 hidden으로 만드는 방법과 
        # urls.py에서 직접 id를 넣어주는 방법이 있다. 여기서는 후자 선택
        # comment.article_id = article_id 이렇게 적어도 됨
        comment.save()
    return redirect('simple_board:article_detail', article_id)
    
def comment_delete(request):
    pass
```



```python
# detail.html가서 comment_delete 부분 추가

{% if comments %}
<ul>
    {% for comment in comments %}
    <li>
        {{ comment.content }}
        <form action="{% url 'simple_board:comment_delete' article.id comment.id %}" method="POST" >
            {% csrf_token %}
            <input type="submit" value="Delete"/>
        </form>
    </li>
    {% endfor %}
</ul>
{% endif %}

{% endblock %}


#views.py 로 가서 comment_delete 부분 추가
def comment_delete(request, article_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('simple_board:article_detail', article_id)


# new.html에 가서
{% extends 'simple_board/base.html' %}

{% block body %}
<form action="{% url 'simple_board:article_create' %}" method="POST">
    {% csrf_token %}
    <div>
        <label for="title">Article's title</label>
        <input type="text" name="title" id="title" />    
    </div>
    <div>
        <label for="content">Article's content</label>
        <textarea name="content" id="content"></textarea>
    </div>
    <div>
        <input type="submit" value="Submit"/>
    </div>
</form>
{% endblock %}


# views.py 로 가서 article_create 부분 추가
def article_create(request):
    if request.method == 'GET':
        return render(request, 'simple_board/new.html')
    
    else:
        article = Article()
        article.title = request.POST. get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('simple_board:article_detail', article.id)
    
# 그렇다면 new.html에 가서 줄일 수 있는 코드는 뭐가 있을까요?
{% extends 'simple_board/base.html' %}

{% block body %}
<form method="POST"> 요기요 action 없어도 됌!
    {% csrf_token %}
    <div>
        <label for="title">Article's title</label>
        <input type="text" name="title" id="title" />    
    </div>
    <div>
        <label for="content">Article's content</label>
        <textarea name="content" id="content"></textarea>
    </div>
    <div>
        <input type="submit" value="Submit"/>
    </div>
</form>
{% endblock %}
```

```html
<!--detail.html에는 article에 관한 것만 있었으면 좋겠는데 comment도 섞여있어서 
 _comment.html 생성한 후  detail.html에 있는 comment있는 부분 잘라옴-->

<form action="{% url 'simple_board:comment_create' article.id %}" method="POST">
    {% csrf_token %}
    <label for="comment">leave comment</label>
    <!--<input type="hidden" value="{{ article.id }}"/>--> 
    <input id="comment" type="text" name="content"/>
    <input type="submit" value="댓글작성"/>
</form>

{% if comments %}
<ul>
    {% for comment in comments %}
    <li>
        {{ comment.content }}
        <form action="{% url 'simple_board:comment_delete' article.id comment.id %}" method="POST" >
            {% csrf_token %}
            <input type="submit" value="Delete"/>
        </form>
    </li>
    {% endfor %}
</ul>
{% endif %}
```

```html
<!-- detail.html에서 include 해주기-->
{% extends 'simple_board/base.html' %}

{% block body %}
<h1>{{ article.title }}</h1> 

<p>
    {{ article.content }}
</p>

<hr/>

<div>
    <a href="{% url 'simple_board:article_list' %}"><button>목록으로 가기</button></a>
</div>
<div>
    <a href="{% url 'simple_board:article_update' article.id %}"></a><button>수정하러 가기</button></a>
</div> 
<form action="{% url 'simple_board:article_delete' article.id %}" method="POST"><button>삭제하러 가기</button></form>

<hr/>
{% include 'simple_board/_comment.html' %}

{% endblock %}
```

```
# edit.html delete.html 추가하기
```

```
# css 넣기
simple_board > static > simple_board 생성
- css
- js
- images 폴더 생성

- css 안에 
bootstrap.css (bootstrap ->download ->css -> bootstrap 복사 붙여넣기)
index.css

-js 폴더 안에
bootstrap.js (bootstrap ->download -> js -> bootstrap 복사 붙여넣기)
index.js

-images 폴더 안에
 header.png
```

```html
<!-- base.html에 css는 link태그로 js는 script로 추가  -->
<!DOCTYPE html>
<html lang="en">
<head>
    {% load static %} <!--이거 추가 -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="{% static 'simple_board/css/bootstrap.css' %}" type="text/css" />
    <link rel="stylesheet" href="{% static 'simple_board/css/index.css' %}" type="text/css" />
    <title>Simple Board</title>
</head>
<body>
    {% block body %}
    {% endblock %}
    <script type="text/javascript" src="{% static 'simple_board/js/bootstrap.js' %}"></script>
    <script type="text/javascript" src="{% static 'simple_board/js/index.js' %}"></script>
</body>
</html>
```

```html
<!-- base.html에 _navbar.html _footer_html 추가하고 파일 생성  -->
<!DOCTYPE html>
<html lang="en">
<head>
    {% load static %}
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="{% static 'simple_board/css/bootstrap.css' %}" type="text/css" />
    <link rel="stylesheet" href="{% static 'simple_board/css/index.css' %}" type="text/css" />
    <title>Simple Board</title>
</head>
<body>
    {% include 'simple_board/_navbar.html' %}
    <div class="container">
        {% block body %}
        {% endblock %}
    </div>
    {% include 'simple_board/_footer.html' %}
    <script type="text/javascript" src="{% static 'simple_board/js/bootstrap.js' %}"></script>
    <script type="text/javascript" src="{% static 'simple_board/js/index.js' %}"></script>
</body>
</html>
```



- create.html. 인가요? index.html 인가요? 그러면 id 값 필요 없고 나머지는 다 id 있음
- GET POST의 차이는 data에 영향을 주면 POST
- form 태그를 써야 POST 에 담을 수 있다





### 나중에 프로젝트시 pip 한 번에 다운받기

```bash
pip freeze > requirements.txt (requirements 텍스트파일에 install 되어 있는 pip 리스트 저장)

pip install -r requirements.txt (한 번에 다운)
```



