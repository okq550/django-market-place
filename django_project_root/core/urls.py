"""
URL configuration for configuration_root project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from .forms import SignInForm

app_name = 'core'

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name='signup'),
    path("signin/", auth_views.LoginView.as_view(template_name='core/signin.html', authentication_form=SignInForm), name="signin"),
    path("signout", views.signout, name='signout'),
    path("contact/", views.contact, name="contact"),
]
