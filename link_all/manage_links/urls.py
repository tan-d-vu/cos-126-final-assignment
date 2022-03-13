"""
manage_links URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('link/create/', views.LinkCreateView.as_view(), name='link_create'),
    path('link/<pk>/update', views.LinkUpdateView.as_view(), name='link_update'),
    path('link/<pk>/delete', views.LinkDeleteView.as_view(), name='link_delete'),
    path('social/create/', views.SocialMediaCreateView.as_view(), name='social_create'),
    path('social/<pk>/update', views.SocialMediaUpdateView.as_view(), name='social_update'),
    path('social/<pk>/delete', views.SocialMediaDeleteView.as_view(), name='social_delete'),
]
