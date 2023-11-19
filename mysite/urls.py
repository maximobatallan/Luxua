"""
URL configuration for Mecha project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from tasks import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('agregar/<int:producto_id>/', views.agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', views.restar_producto, name="Sub"),
    path('limpiaritems/<int:producto_id>/', views.limpiar_carrito_item, name="CLSK"),
    path('limpiar/', views.limpiar_carrito, name="CLS"),
    path('gallery/', views.galeriaprueba, name='gallery'),
    path('productdetails/<int:producto_id>/', views.detalleproducto, name='PD'),
    path('cargaproducto/', views.producto, name='cargaproducto'),
    path('datos/', views.datos, name='datos'),
    path('catproducto/<str:catproducto>/', views.catproducto, name='catproducto'),
    path('categoria/', views.categoria, name='categoria'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)