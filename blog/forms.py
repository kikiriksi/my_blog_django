from django import forms
from .models import Post


class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'descriptions', 'author', 'image', 'date')