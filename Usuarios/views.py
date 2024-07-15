from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import Usuarios,Clientes, Productos,Promociones, Promociones_Clientes,  Promociones_Productos,Tiendas,Visita_Tienda_Clientes
from .serializer import UsuariosSerializer,ClientesSerializer, ProductosSerializer, PromocionesSerializer,PromocionesClienteSerializer, PromocionesProductoSerializer, TiendasSerializer, VisitaTiendaClientesSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    
class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer

class PromocionesViewSet(viewsets.ModelViewSet):
    queryset = Promociones.objects.all()
    serializer_class = PromocionesSerializer

class PromocionesClienteViewSet(viewsets.ModelViewSet):
    queryset = Promociones_Clientes.objects.all()
    serializer_class = PromocionesClienteSerializer

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

class PromocionesProductoViewSet(viewsets.ModelViewSet):
    queryset = Promociones_Productos.objects.all()
    serializer_class = PromocionesProductoSerializer  
        
    
class TiendasViewSet(viewsets.ModelViewSet):
    queryset = Tiendas.objects.all()
    serializer_class = TiendasSerializer

class VisitaTiendaClientesViewSet(viewsets.ModelViewSet):
    queryset = Visita_Tienda_Clientes.objects.all()
    serializer_class = VisitaTiendaClientesSerializer  
    
@api_view(['GET'])
def get_visitas(request, cedula):
    visitas = Visita_Tienda_Clientes.objects.filter(cedula=cedula).order_by('fecha_visita')
    serializer = VisitaTiendaClientesSerializer(visitas, many=True)
    return Response(serializer.data)  
    

    
    







    
    
# Create your views here.
