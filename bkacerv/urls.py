"""bkacerv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from proj import views
from django.views.generic import RedirectView  
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('obra/all/',views.list_all_obras),
    path('obra/user/',views.list_user_obras),
    path('obra/detail/<id>/',views.obra_detail),
    path('login/',views.login_user),
    path('login/submit',views.submit_login),
    path('logout/',views.logout_user),
    path('obra/register/',views.register_obra),
    path('obra/register/submit',views.set_obra),
    path('obra/delete/<id>/', views.delete_obra),
    path('',RedirectView.as_view(url='obra/all/'))

]
