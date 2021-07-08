from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', views.ProductoViewset)

urlpatterns = [
    path('', views.home, name= "home"),
    path('contacto/', views.contacto, name= "contacto"),
    path('galeria/', views.galeria, name= "galeria"),
    path('tienda/', views.tienda, name= "tienda"),
    path('agregar-producto/', views.agregar_producto, name="agregar_producto"),
    path('listar-productos/', views.listar_productos, name="listar_productos"),
    path('modificar-productos/<id>/', views.modificar_producto, name="modificar_productos"),
    path('eliminar-producto/<id>/', views.eliminar_producto, name="eliminar_producto"),
    path('registro/', views.registro, name ="registro"),
    path('api/', include(router.urls), name="api"),
]

