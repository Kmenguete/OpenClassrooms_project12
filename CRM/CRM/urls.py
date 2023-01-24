"""CRM URL Configuration

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
from django.urls import path, include
from rest_framework import routers


import authentication.views
import client.views
import contract.views
import event.views

router = routers.SimpleRouter()

router.register('login', authentication.views.LoginViewSet, basename='login')
router.register('logout', authentication.views.LogoutViewSet, basename='logout')
router.register('user', authentication.views.UserViewSet, basename='user')
router.register('client', client.views.ClientViewSet, basename='client')
router.register('contract', contract.views.ContractViewSet, basename='contract')
router.register('event', event.views.EventViewSet, basename='event')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
