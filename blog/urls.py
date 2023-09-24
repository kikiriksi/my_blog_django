from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllPost.as_view(), name='home'),
    path('<int:pk>', views.OnePost.as_view(), name='onepost'),
]
