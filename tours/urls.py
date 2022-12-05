"""tourmate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

from .views import RegisterController, PostsController, CreatePostController, PostUpdateController

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('destination/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path("city/", views.IndexView.as_view(), name="search_results"),
    path('plan', views.IndexPlanView.as_view(), name="plan_list"),
    path('destination', views.IndexDestinationView.as_view(), name="destination_list"),
    path('plan/<int:pk>/', views.DetailPlanView.as_view(), name="detail_plan"),
    path("destination/", views.IndexDestinationView.as_view(), name="search_destination_results"),
    path('register', views.RegisterController.as_view(), name='register'),
    path('login', auth_view.LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True),
         name='login'),
    # path('logins', views.LoginView, name="logins"),
    path('logout', auth_view.LogoutView.as_view(template_name='tours/index.html'), name='logout'),
    path('addPost', CreatePostController.as_view(), name='addPost'),
    path('explore', views.IndexPostView.as_view(), name='indexPost'),
    path('posts/<str:username>/', PostsController.as_view(), name='posts'),
    path('posts/<str:username>/<int:id>/', PostsController.as_view(), name='post'),
    path('posts/<str:username>/<int:id>/update', PostUpdateController.as_view(), name='postUpdate'),
    path('posts/<str:username>/<int:id>/delete', views.PostDeleteController.as_view(), name='postDelete'),
    path('profile', views.UserProfile.as_view(), name='users-profile'),
]
