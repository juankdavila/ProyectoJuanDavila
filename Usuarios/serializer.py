from rest_framework import serializers
from .models import Usuarios,Clientes, Promociones, Promociones_Clientes, Productos, Promociones_Productos,Tiendas,Visita_Tienda_Clientes,HistorialVisita


class UsuariosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Usuarios
        fields ='__all__'
        
class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'

class PromocionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promociones
        fields = ['id_promocion', 'descripcion', 'fecha_inicio', 'fecha_fin', 'estado']

class PromocionesClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promociones_Clientes
        fields = ['id_promocion_cliente', 'id_promocion', 'cedula', 'monto_descuento', 'estado']

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ['id_producto', 'codigo', 'descripcion', 'precio', 'estado']

class PromocionesProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promociones_Productos
        fields = ['id_promocion_producto', 'id_promocion', 'id_producto', 'monto_descuento', 'estado']        
        

class TiendasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiendas
        fields = '__all__'

class VisitaTiendaClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visita_Tienda_Clientes
        fields = '__all__'   
        

class HistorialVisitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialVisita
        fields = '__all__'