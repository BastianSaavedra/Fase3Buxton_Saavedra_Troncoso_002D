
from rest_framework import viewsets, permissions
from .serializers import PlacasMadreSerializer, ProcesadorSerializer, GpuSerializer, RamSerializer, UserSerializer
from catalog.models import PlacasMadre, Procesadore, Gpu, Ram
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all().order_by('-date_joined')
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated]
   
class PlacasMadreViewSet(viewsets.ModelViewSet):
   serializer_class = PlacasMadreSerializer
   queryset = PlacasMadre.objects.all()
   
class ProcesadorViewSet(viewsets.ModelViewSet):
   serializer_class = ProcesadorSerializer
   queryset = Procesadore.objects.all()
   
class GpuViewSet(viewsets.ModelViewSet):
   serializer_class = GpuSerializer
   queryset = Gpu.objects.all()
   
class RamViewSet(viewsets.ModelViewSet):
   serializer_class = RamSerializer
   queryset = Ram.objects.all()
   
   

