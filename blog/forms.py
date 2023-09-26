from django import forms
from .models import Post, CommentsModel


class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'descriptions', 'image', 'date',)


class CommentsForm(forms.ModelForm):
    class Meta:
        model = CommentsModel
        fields = ('comments',)
