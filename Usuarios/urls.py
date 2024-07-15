from django.urls import path,include
from rest_framework import routers
from .views import UsuariosViewSet, ClientesViewSet, ProductosViewSet,PromocionesViewSet, PromocionesClienteViewSet, PromocionesProductoViewSet,TiendasViewSet,VisitaTiendaClientesViewSet,get_visitas


router=routers.DefaultRouter()
router.register(r'Usuarios',UsuariosViewSet)
router.register(r'clientes', ClientesViewSet)
router.register(r'productos', ProductosViewSet)
router.register(r'promociones', PromocionesViewSet)
router.register(r'promociones_clientes', PromocionesClienteViewSet)
router.register(r'promociones_productos', PromocionesProductoViewSet)
router.register(r'Tiendas', TiendasViewSet)
router.register(r'visita_tienda_clientes', VisitaTiendaClientesViewSet)



urlpatterns = [
path('',include(router.urls)),
path('visitas/<str:cedula>/', get_visitas, name='get_visitas'),


]


