from django.contrib import admin
from .models import Post
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('id', 'content', 'created', 'modified')
    list_display_links = ('id', 'content')



admin.site.register(Post, PostModelAdmin)