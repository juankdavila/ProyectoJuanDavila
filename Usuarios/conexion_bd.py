from .models import Usuarios

class ConexionBD:
    @staticmethod
    def get_Usuarios():
        return Usuarios.objects.all()
    
  




