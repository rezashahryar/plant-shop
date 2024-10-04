"""
URL configuration for config project.

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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from azbankgateways.urls import az_bank_gateways_urls

urlpatterns =  i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path(_('post/'), include('blog.urls')),
    path(_('product/'), include('products.urls')),
    path(_('auth/'), include('django.contrib.auth.urls')),
    path(_('auth/'), include('accounts.urls')),
    path(_('shop/'), include('shop.urls')),
    path('', include('pages.urls')),
    # third party pack
    path('summernote/', include('django_summernote.urls')),
    path('rosetta/', include('rosetta.urls')),
    path("bankgateways/", az_bank_gateways_urls()),
) + debug_toolbar_urls()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
