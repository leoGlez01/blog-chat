from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', user_login, name='login'),
    path("auth/logout/", LogoutView.as_view(), name='logout-user')
]