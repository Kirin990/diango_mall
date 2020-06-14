"""django_mall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from django_mall import views

import xadmin
xadmin.autodiscover()

# The version module automatically registers models that require version control
from xadmin.plugins import xversion
xversion.register_models()


urlpatterns = [
    # Django's own background management
    url(r'^admin/', admin.site.urls),
    # xadmin configuration
    url(r'xadmin/', include(xadmin.site.urls)),
    url(r'^$', views.index, name='index'),
    # Commodity part
    url(r'^mall/', include('mall.urls', namespace='mall')),
    # User account module
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    # System module
    url(r'^sys/', include('system.urls', namespace='system')),
    # Personal center
    url(r'^m/', include('mine.urls', namespace='mine')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
