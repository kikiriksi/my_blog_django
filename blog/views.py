from django.shortcuts import render
from django.views import View
from .models import Post
from .forms import AddBlogForm


# Create your views here.
class AllPost(View):
    '''вывод записей из модели Post'''

    def get(self, request):
        model = Post.objects.all()
        return render(request, 'blog/home.html', context={
            'all_post': model
        })


class OnePost(View):
    '''Выводит отдельный пост по id'''

    def get(self, request, pk: int):
        context = {"post": Post.objects.get(id=pk)}
        return render(request, 'blog/oneblog.html', context)


class AddPost(View):
    '''Добавить блог'''
    def get(self, request):
        context = {"form": AddBlogForm}
        return render(request, 'blog/addpost.html', context)
