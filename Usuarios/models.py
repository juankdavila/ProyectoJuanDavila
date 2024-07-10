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
        return f'{self.nombres} {self.apellidos}'
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
         
            
    
    
    



# Create your models here.
