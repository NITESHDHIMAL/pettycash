"""pettycash URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from accounts.serializers import AccountHeadSerializer
from accounts.views import AccountHeadViewSet, ExpenseTitleViewSet, ExpenseViewSet, TopupViewset

#viewsets
from users.views import UserViewSet

#routers
router = routers.DefaultRouter()

#viewsets
router.register('user',UserViewSet,basename='user')
router.register('expense-title',ExpenseTitleViewSet,basename='expens-title')
router.register('expense',ExpenseViewSet,basename='expense')
router.register('topup',TopupViewset,basename='topup')
router.register('account-head',AccountHeadViewSet,basename='account-head')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),

]



