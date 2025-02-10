"""
URL configuration for djangoblogsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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





'''
client ID : Ov23liRUt23B8qRMJcvw

client Secret : 55cd84848333645bb843bfdb8e88fa346f03c61e
'''



from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from allauth.account.views import SignupView
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("articles/", include("app.urls")),
    path("", SignupView.as_view(), name="account_signup"),
    path("account/signup/", RedirectView.as_view(url="/")),
    path("account/",include("allauth.urls")),
    # path("", RedirectView.as_view(pattern_name="home")),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
        path("__reload__/", include("django_browser_reload.urls")),
    ]