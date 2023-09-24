from django.shortcuts import render, redirect
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

    def post(self, request):
        form = AddBlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'blog/addpost.html', context={'form': form})
