[TOC]



# Django

## 1. 프로젝트 만들기

```python
$ django-admin startproject <project_name>
```



## 2. 앱 만들기

```python
$ django-admin startapp <app_name>
```



## 3. 앱 등록하기

`<project_name>/settings.py` 에서 INSTALLED_APPS에 <app_name> 추가



## 4. 서버 작동시키기

```python
$ django-admin runserver $IP:$PORT
```



## 5. models 만들기

#### 5-1 model 작성하기

`<project_name>/models.py` 에서

```python 
from django.db import models

class Class_name(models.Model):
    문자열 = models.CharField(max_length=n) #최대길이가 있는 문자열
    문자열 = models.TextField() #최대길이가 없는 문자열
    숫자 = models.IntegerField(null=true) #null값 가능
    날짜 = models.DateTimeField('date published')
    boolean = models.BooleanField()    
    
    def __str__(self):
        return f'{self.문자}: {self.숫자}' #우리가 보기 쉽게 정리해놓는 것
```

* Django가 제공하는 `django.db` 의 `models.Model` 클래스를 상속받는다. 상속받은 메소드를 통해 `<Class_name>` 의 객체들이 DB 조작을 수행한다



#### 5-2 model 생성하기

```python
$ python manage.py makemigrations <app_name>
```



#### 5-3 DB에 등록하기

```python
$ python manage.py migrate
```



#### 5-4 DB Reset하기

* DB에 존재하는 모든 데이터 레코드를 삭제하기

```python
$ python manage.py sqlflush
```

* 특정 app의 모든 데이터 레코드를 삭제하기

```python
$ python manage.py sqlflush <app_name>
```

* 특정 app의 모든 테이블을 삭제한다

```python
$ python manage.py migrate <app_name> zero
```



#### 5-5 DB CRUD via Django Shell

```python
$ python manage.py shell
>>> from <app_name>.model import <Class_name>
>>> object = <Class_name>(속성=value)
>>> object.save()
#ex. b = Band(name='Queen')
#  	 b.save()  >name이 Queen인 DB가 추가된다
>>> object.속성
>>> value
```



## 6. Admin page 관리하기

#### 6-1 슈퍼계정 생성

```python
$ python manage.py createsuperuser
# username과 password를 설정한다
```



#### 6-2  서버에 접속하기

```python
$ python manage.py runserver
```



#### 6-3 관리할 모델을 관리자 페이지에서 등록

`admin.py` 에서

```python
from .models import Class_name1, Class_name2 ...
#현재 위치의 models에서 각각의 클래스를 import
admin.site.register([Class_name1, Class_name2 ...])
#해당 클래스를 admin.site에서 관리할 수 있도록 등록
```



## 7. Views 만들기 (CRUD)

#### 7-0 필요한 module을 import하기

```python
from django.shortcuts import render, redirect, resolve_url
from .models import Class_name
```



#### 7-1 Create

```python
def create(request):
    if request.method == "GET":
        return render(request,'생성 html')
        
    else: #request.method == "POST"
        input_속성1 = request.POST.get('html에서 input의 name')
        input_속성2 = request.POST.get('html에서 input의 name')
        ....
        #사용자 input을 속성으로 갖는 객체를 정의하는 단계
        instance_name = Class_name(속성1=input_속성1, 속성2=input_속성2 ..)
        # 객체를 실제 DB에 저장하는 단계
        instance_name.save()
        return redirect(resolve_url(<app_name>:path_name))
    	#ex. return redirect(resolve_url('menupan:menupan_index'))
```



#### 7-2 Read

```python
def read(request): # 모든 객체를 받아오기    
    instance_name = Class_name.objects.all()
    return render(request, '위치/읽기 html', {'변수명': instance_name})
	
'''	menu = Menu.objects.all()
	return render(request, menupan/read.html, {'menu': menu})'''
	
def read(request, id): # 특정 id를 가진 객체만 받아오기       
    instance_name = Class_name.objects.get(id=id)
    return render(request, '위치/읽기 html', {'변수명': instance_name})
	
'''	menu = Menu.objects.get(id=id)
	return render(request, menupan/read.html, {'menu': menu})'''
	
```



#### 7-3 Update

```python
def update(request, id):
    instance_name = Class_name.objects.get(id=id)
    
    if request.method == "GET":
    	return render(request, '위치/수정 html', {'변수명': instance_name})
    else:
        instance_name.속성1 = request.POST.get('html에서 input의 name')
        instance_name.속성2 = request.POST.get('html에서 input의 name')
        ...
        instance_name.save()
        return redirect(resolve_url('<app_name>:path_name'))
   	 	#ex. return redirect(resolve_url('menupan:menupan_index'))
```



#### 7-4 Delete

```python
def delete(request, id):
    instance_name = Class_name.objects.get(id=id)
    if request.method == "GET":
        return redirect(resolve_url('<app_name>:path_name', id))
    else:
        instance_name.delete()
        return redirect(resolve_url('<app_name>:path_name'))
    	#ex. return redirect(resolve_url('menupan:menupan_index'))
```



## 8. urls.py 만들기 

#### 8-1 project urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpattens = [
    path('admin/', admin.site.urls),
    path('<app_name>/', include('<app_name>.urls')), #app의 urls.py로 이동하도록 설정
]
```



#### 8-2 app_name/urls.py

`/<app_name>` 에 urls.py를 새로 만든다

```python
from django.urls import path
from . import views

app_name = '<app_name>'

urlpatterns = [
    path('주소값', views.해당views, name='<app_name>_해당views')
]
'''ex. path('', views.index, name='menupan_index')
	   path('delete/<int:id>', views.delete, name='menupan_delete')'''
```



## 9. HTML templates 만들기

#### 9-1 settings.py 설정

`settings.py` 에서

```python
TEMPLATES = [
    {
        'BACKEND': ~
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # 이것을 추가한다
    }    
]
```



#### 9-2 templats 디렉토리 만들기

`<app_name>/templates/<app_name> ` 을 만든다. 그리고 해당 디렉토리 아래에 base.html을 생성한다



#### 9-3 base.html 만들기

```html
<body>
    {% block body %}
    {% endblock %}
</body>
```



#### 9-4 base.html을 적용하는 example.html을 만들기

```python
{% extends '<app_name>/base.html' %} #특정 디렉토리 아래에 있는 base.html을 적용

{% block body %}
<h1>{{ <instance_name>.속성 }}</h1>  #views의 instance와 속성을 이용하는 방법

#form문 사용하기
<form action="{% url '<app_name>:<app_name>_해당views' id=<instance_name>.id %}" method="POST">
	{% csrf_token %}
	<input type="text" name="input_속성" value="{{ instance.속성 }}"
</form>

#for문 사용하기
{% for instance in instances %}
속성값: {{ instance.속성 }}
{% endfor %}

{% endblock %}
```

