"""Site URL Configuration

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
from main.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index, name='index'),
    path('cadastro/', cadastro, name='cadastro'),
    path('login/',login, name='login'),
    path('plataforma',plataforma, name='plataforma'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('perfil',perfil, name='perfil'),
    path('usuariocadastrado',usuario_cadastrado,name='usuariocadastrado'),
    path('mercado/', mercado, name="mercado"),
    path('produto/', produto, name="produto"),
    path('detalhe/<int:id>',detalhe, name='detalhe'),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)