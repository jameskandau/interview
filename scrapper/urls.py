
from django.contrib import admin
from django.urls import path, include
from .views import RegistrationView,HomePageView,ProfileView,LoginView,LogoutUser

app_name = "scrapper"
urlpatterns = [
    path('',HomePageView.as_view(),name="home"),
    path('register', RegistrationView.as_view(),name="register"),
    path('profile',ProfileView.as_view(),name="profile"),
    path('logout',LogoutUser.as_view(),name="logout"),
    path('login',LoginView.as_view(),name="login")
]
