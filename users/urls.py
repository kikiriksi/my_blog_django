from django.urls import path
from . import views

urlpatterns = [
    path('reg', views.RegUsers.as_view(), name='reg'),
    path('log', views.LogUsers.as_view(), name='log'),
    path('logaut', views.logaut, name='logaut'),
]
