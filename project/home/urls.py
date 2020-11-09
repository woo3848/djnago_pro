"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.main),
    path('login/', views.Login.as_view()),
    path('logout/', views.logout),
    path('signup/', views.Signup.as_view()),
    path('board/index/', views.index),
    path('board/notice/<int:idx>/', views.notice),
    path('board/write/', views.Write.as_view()),
    path('board/delete/<int:idx>/', views.delete),
    path('board/modify/<int:idx>/', views.Modify.as_view()),
    path('video/', views.video)

]
