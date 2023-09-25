from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserCreationForm, LogForm
from django.contrib.auth import authenticate, login

# Create your views here.
class RegUsers(View):
    def get(self, request):
        context = {'form': UserCreationForm()}
        return render(request, 'users/reg.html', context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'users/reg.html', context={'form': form})


class LogUsers(LoginView):
    def get(self, request):
        form = LogForm
        return render(request, 'users/log.html', context={'form': form})

    def post(self, request):
        data = request.POST
        user = authenticate(request, username=data['username'], password=data['password'])
        if user is None:
            form = LogForm(request.POST)
            return render(request, 'users/log.html', context={'form': form})
        login(request, user)
        return redirect('home')




class LogautUser(View):
    pass
