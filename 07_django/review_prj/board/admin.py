from django.contrib import admin
from .models import Article

# Register your models here.

# Article 모델을 관리자 페이지(admin site)에서 확인할래!

admin.site.register(Article)