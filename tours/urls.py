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

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('destination/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path("city/", views.IndexView.as_view(), name="search_results"),
    path('plan', views.IndexPlanView.as_view(), name="plan_list"),
    path('destination', views.IndexDestinationView.as_view(), name="destination_list"),
    path('plan/<int:pk>/', views.DetailPlanView.as_view(), name="detail_plan"),

]
