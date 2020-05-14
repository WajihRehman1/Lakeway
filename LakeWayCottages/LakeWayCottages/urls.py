"""LakeWayCottages URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include
from basic_app.views import index
from django.contrib.auth.views import PasswordChangeView,PasswordResetDoneView,PasswordResetView,PasswordResetConfirmView,PasswordResetCompleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('app/',include('basic_app.urls')),
    path('reset_password',PasswordResetView.as_view(template_name='password_resetting/password_reset_form.html'),name='reset_password'),
    path('password_reset_done',PasswordResetDoneView.as_view(template_name='password_resetting/password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='password_resetting/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/',PasswordResetCompleteView.as_view(template_name='password_resetting/password_reset_complete.html'),name='password_reset_complete')
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)