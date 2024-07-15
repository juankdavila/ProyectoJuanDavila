from django.db import models


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=50)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    mail = models.EmailField()
    fecha_nacimiento = models.DateField()
    contrasena = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    fecha_ultima_conexion = models.DateTimeField()
    usuario_creacion = models.IntegerField()
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.IntegerField()
    fecha_modificacion = models.DateTimeField()
    
    def __str__(self):
        return f'{self.id_usuario} {self.codigo} {self.nombres} {self.apellidos}'
                 
    class Meta:
        db_table = 'Usuarios'
        

class Opciones(models.Model):
    id_opcion = models.AutoField(primary_key=True)          
    usuario_creacion= models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.id_opcion}{self.usuario_creacion}'
    class Meta:
         db_table = 'Opciones'
           
            
class Opciones_Usuarios(models.Model):
    id_opcion_usuario = models.AutoField(primary_key=True) 
    usuario_modificacion = models.IntegerField() 
    fecha_modificacion = models.DateTimeField()
    Usuarios=models.ForeignKey(Usuarios,on_delete=models.CASCADE)
    Opciones=models.ForeignKey(Opciones,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.id_opcion_usuario}{self.usuario_modificacion}{self.fecha_modificacion}' 
    class Meta:
         db_table ="Opciones_Usuarios"
         
         
class Clientes(models.Model):
    cedula = models.CharField(max_length=20, primary_key=True) 
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=1)
    
    def __str__(self):
        return f'{self.cedula} {self.nombre}{self.estado}' 
    class Meta:
        db_table = 'Clientes'


class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True) 
    codigo = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=100)  
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=1) 
    
    def __str__(self):
        return f'{self.id_producto} {self.codigo} {self.descripcion} {self.precio} {self.estado}'
    class Meta:
        db_table = 'Productos'    
        
        
class Promociones(models.Model):
    id_promocion = models.AutoField(primary_key=True) 
    descripcion = models.CharField(max_length=100)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    estado =   models.CharField(max_length=1)  
    
    def __str__(self):
        return f'{self.id_promocion} {self.descripcion} {self.fecha_inicio} {self.fecha_fin} {self.estado}'
    class Meta:
        db_table = 'Promociones'   
    
    
class Promociones_Clientes(models.Model):
    id_promocion_cliente = models.AutoField(primary_key=True) 
    id_promocion= models.ForeignKey('Promociones', on_delete=models.CASCADE)
    cedula = models.ForeignKey('Clientes', on_delete=models.CASCADE)
    monto_descuento = models.DecimalField(max_digits=10, decimal_places=2)
    estado =   models.CharField(max_length=1) 
    
    def __str__(self):
        return f'{self.monto_descuento} {self.estado}'
    class Meta:
        db_table = 'Promociones_Clientes'                   
            
    
class Promociones_Productos(models.Model):
    id_promocion_producto = models.AutoField(primary_key=True)
    id_promocion=  models.ForeignKey('Promociones', on_delete=models.CASCADE) 
    id_producto= models.ForeignKey('Productos', on_delete=models.CASCADE)
    monto_descuento = models.DecimalField(max_digits=10, decimal_places=2)
    estado =   models.CharField(max_length=1)    
    
    def __str__(self):
        return f'{self.monto_descuento} {self.estado}'
    class Meta:
        db_table = 'Promociones_Productos'   
        
         
    
    
class Tiendas(models.Model):
    id_tienda = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=1)
    
    def __str__(self):
        return f'{self.descripcion} {self.estado}'
    class Meta:
        db_table = 'Tiendas'   
    
class Visita_Tienda_Clientes(models.Model):
    id_Tienda_Visita_Cliente = models.AutoField(primary_key=True)
    id_tienda = models.ForeignKey('Tiendas', on_delete=models.CASCADE)    
    fecha_visita =  models.DateTimeField()
    cedula =models.ForeignKey('Clientes',on_delete=models.CASCADE)
     
    def __str__(self):
        return f' {self.id_tienda}{self.fecha_visita} {self.cedula}'
    class Meta:
        db_table = 'Visita_Tienda_Clientes' 
        
        
  
        

        
    



# Create your models here.
