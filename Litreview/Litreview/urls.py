"""Litreview URL Configuration

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
import authentication.views
import website.views
from django.conf import settings
from django.conf.urls.static import static
from authentication.models import User


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", authentication.views.login_page, name="login"),
    path("logout/", authentication.views.logout_user, name="logout"),
    path("home/", website.views.home, name="home"),
    path("signup/", authentication.views.signup_page, name="signup"),
    path("create_ticket/", website.views.create_ticket, name="create_ticket"),
    path("update/<str:pk>", website.views.update_ticket, name="update_ticket"),
    path("delete/<str:pk>", website.views.delete_ticket, name="delete_ticket"),
    path("update_review/<str:pk>", website.views.update_review, name="update_review"),
    path("delete_review/<str:pk>", website.views.delete_review, name="delete_review"),
    path("reviewing/<str:pk>", website.views.create_review, name="reviewing"),
    path("followers/", website.views.follow_users, name="followers"),
    path("profile/<int:pk>", website.views.profile, name="profile"),
    path("create_review/", website.views.create_own_review, name="create_review"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
