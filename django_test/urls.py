"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include,url
from django.contrib import admin
from django.urls import path
from backend.app import views as testUrl
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', testUrl.test,name="test"),
    url(r'^api/v1/book_list$', testUrl.book_list,name="book_list"),
    url(r'^api/v1/book_create$', testUrl.book_create,name="book_create"),
    url(r'^api/v1/book_delete$', testUrl.book_delete,name="book_delete"),
    url(r'^api/v1/book_update$', testUrl.book_update,name="book_update")

]
