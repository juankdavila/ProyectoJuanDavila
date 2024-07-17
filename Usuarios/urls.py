from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UsuariosViewSet, ClientesViewSet, ProductosViewSet,PromocionesViewSet, PromocionesClienteViewSet, PromocionesProductoViewSet,TiendasViewSet,VisitaTiendaClientesViewSet,HistorialVisitaViewSet


router = DefaultRouter()
router.register(r'usuarios', UsuariosViewSet)
router.register(r'clientes', ClientesViewSet)
router.register(r'promociones', PromocionesViewSet)
router.register(r'promociones_cliente', PromocionesClienteViewSet)
router.register(r'productos', ProductosViewSet)
router.register(r'promociones_producto', PromocionesProductoViewSet)
router.register(r'tiendas', TiendasViewSet)
router.register(r'visita_tienda_clientes', VisitaTiendaClientesViewSet)
router.register(r'historial_visita', HistorialVisitaViewSet, basename='historial-visita')



urlpatterns = [
     path('',include(router.urls)),



]


