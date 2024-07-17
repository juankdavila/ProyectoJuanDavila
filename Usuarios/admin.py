from django.contrib import admin
from .models import Usuarios,Opciones,Opciones_Usuarios
from .models import Clientes,Productos,Promociones,Promociones_Clientes,Promociones_Productos,Tiendas,Visita_Tienda_Clientes,HistorialVisita



admin.site.register(Usuarios)
admin.site.register(Opciones)
admin.site.register(Opciones_Usuarios)
admin.site.register(Clientes)
admin.site.register(Productos)
admin.site.register(Promociones)
admin.site.register(Promociones_Clientes)
admin.site.register(Promociones_Productos)
admin.site.register(Tiendas)
admin.site.register(Visita_Tienda_Clientes)
admin.site.register(HistorialVisita)





