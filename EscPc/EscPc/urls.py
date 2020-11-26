"""EscPc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
   https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from EscPc.quickstart import views
from rest_framework import routers

#API
router = routers.DefaultRouter()
router.register(r'motherboard', views.PlacasMadreViewSet)
router.register(r'processor', views.ProcesadorViewSet)
router.register(r'gpu', views.GpuViewSet)
router.register(r'memorias-ram', views.RamViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('catalog.urls')),
   path('accounts/', include('django.contrib.auth.urls')),
   path('accounts/', include('sesion.urls')),
   path('cart/', include('cart.urls')),
   path('', include(router.urls)),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)

if settings.DEBUG:  
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)