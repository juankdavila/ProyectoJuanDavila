from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Usuarios,Clientes, Productos,Promociones, Promociones_Clientes,  Promociones_Productos,Tiendas,Visita_Tienda_Clientes,HistorialVisita
from .serializer import UsuariosSerializer,ClientesSerializer, ProductosSerializer, PromocionesSerializer,PromocionesClienteSerializer, PromocionesProductoSerializer, TiendasSerializer, VisitaTiendaClientesSerializer,HistorialVisitaSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    
class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    
    @action(detail=True, methods=['get'])
    def historial_visitas(self, request, pk=None):
        cliente = self.get_object()
        visitas = HistorialVisita.objects.filter(cliente=cliente)
        serializer = HistorialVisitaSerializer(visitas, many=True)
        return Response(serializer.data)

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
    
    @action(detail=True, methods=['get'])
    def visitas(self, request, pk=None):
        tienda = self.get_object()
        visitas = Visita_Tienda_Clientes.objects.filter(id_tienda=tienda)
        serializer = VisitaTiendaClientesSerializer(visitas, many=True)
        return Response(serializer.data)

class VisitaTiendaClientesViewSet(viewsets.ModelViewSet):
    queryset = Visita_Tienda_Clientes.objects.all()
    serializer_class = VisitaTiendaClientesSerializer  
    
class HistorialVisitaViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['get'], url_path='cedula/(?P<cedulaHistorial>[^/.]+)')
    def get_historial_visitas(self, request, cedulaHistorial=None):
        visitas = HistorialVisita.objects.filter(cliente__cedula=cedulaHistorial)
        serializer = HistorialVisitaSerializer(visitas, many=True)
        return Response(serializer.data)    
    

    

    
    







    
    
# Create your views here.
