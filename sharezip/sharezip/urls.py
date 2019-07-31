"""sharezip URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
import browse.views
import hosting.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',browse.views.home, name='home'),
    path('base/',browse.views.base, name='base'),
    path('condition/',browse.views.condition, name='condition'),
    path('result/', browse.views.result, name='result'),
    path('hosting1/', hosting.views.hosting1, name="hosting1"),
    path('create1/', hosting.views.create1, name="create1"),
    path('create2/', hosting.views.create2, name="create2"),
    path('hosting2/', hosting.views.hosting2, name="hosting2"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

