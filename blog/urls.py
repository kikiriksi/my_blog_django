from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllPost.as_view(), name='home'),
    path('<int:pk>', views.OnePost.as_view(), name='onepost'),
    path('addblog', views.AddPost.as_view(), name='addblog'),
    path('addbcomment/<int:pk>/', views.Comments.as_view(), name='addbcomment'),
    path('delpost/<int:pk>/', views.delpost, name='delpost')
]
