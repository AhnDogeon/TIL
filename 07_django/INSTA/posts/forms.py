from django import forms
from .models import Post, Image, Comment

class PostModelForm(forms.ModelForm):
    # content = forms.EmailField(label='Your Email')
    class Meta:
        model = Post
        fields = [
            'content',
        ]
        # fields = ['content', ...]

class ImageModelForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['file', ]
        widgets = {
            'file': forms.FileInput(attrs={'multiple': True})
        }

class CommentModelFrom(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'comment'
        ]