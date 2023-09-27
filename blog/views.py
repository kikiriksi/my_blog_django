from django.shortcuts import render, redirect
from django.views import View
from .models import Post, CommentsModel
from .forms import AddBlogForm, CommentsForm
from users.models import CustomUser


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
        context = {"post": Post.objects.get(id=pk),
                   "coments": CommentsModel.objects.filter(post=Post.objects.get(id=pk)),
                   "formcomit": CommentsForm}
        return render(request, 'blog/oneblog.html', context)


class AddPost(View):
    '''Добавить блог'''

    def get(self, request):
        context = {"form": AddBlogForm}
        return render(request, 'blog/addpost.html', context)

    def post(self, request):
        form = AddBlogForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = CustomUser.objects.get(username=request.user)
            form.save()
            return redirect('home')
        return render(request, 'blog/addpost.html', context={'form': form})


class Comments(View):
    '''Коментарии'''

    def post(self, request, pk: int):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form.post = Post.objects.get(id=pk).title
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')


def delpost(request, pk: int):
    post = CommentsModel.objects.get(id=pk)
    post.delete()
    return redirect('home')
