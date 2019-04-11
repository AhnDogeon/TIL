from django import forms
from .models import Post

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # 이렇게 사용하면 지정한 것만 들어가고 all하면 다 들어감
        # fields = ['content', ...]