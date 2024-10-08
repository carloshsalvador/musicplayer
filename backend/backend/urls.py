"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),                            # '/' can avoid conflicts with other URLs, the same for all other URLs, here and other files (e.g., music_player_app/urls.py)
    path('', include('music_player_app.urls')),                 # include URL to drive to the URLs of app 'music_player_app'
    path('accounts/', include('django.contrib.auth.urls')),     # include URL to drive URLs of Django's standart autentification: 'django.contrib.auth.urls' such as login, logout, password reset, etc.
    path('api/', include('api.urls')),                          # to drive to the URLs of app 'api'
]
