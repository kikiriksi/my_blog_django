from django.shortcuts import render, redirect
from django.views import View
from .forms import UserCreationForm


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


class LogUsers(View):
    pass
