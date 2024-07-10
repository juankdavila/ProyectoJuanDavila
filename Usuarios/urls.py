from django.urls import path,include
from rest_framework import routers
from Usuarios import views


router=routers.DefaultRouter()
router.register(r'Usuarios',views.UsuariosViewSet)

urlpatterns = [
path('',include(router.urls))
]
