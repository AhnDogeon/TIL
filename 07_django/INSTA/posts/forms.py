from django import forms
from .models import Post, Image

class PostModelForm(forms.ModelForm):
    # content = forms.EmailField(label='Your email')
    class Meta:
        model = Post
        fields = '__all__'
        # 이렇게 사용하면 지정한 것만 들어가고 all하면 다 들어감
        # fields = ['content', ...]


class ImageModelForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['file',]
        widgets = {
            'file': forms.FileInput(attrs={'multiple': True})
        }