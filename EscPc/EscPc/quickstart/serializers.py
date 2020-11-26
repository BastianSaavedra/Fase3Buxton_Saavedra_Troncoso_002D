from rest_framework import serializers
from catalog.models import PlacasMadre, Procesadore, Gpu, Ram
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
   
   class Meta:
      model = User
      fields = ['url', 'username', 'email', 'first_name', 'last_name']


class PlacasMadreSerializer(serializers.ModelSerializer):
   
   class Meta:
      model = PlacasMadre
      fields = '__all__'
   
   def validate_modelo(self, value):
      existe = PlacasMadre.objects.filter(modelo_iexact=value).exists()
      
      if existe:
         raise serializers.ValidationError("Este producto ya existe")
      return value
   
   
class ProcesadorSerializer(serializers.ModelSerializer):
   
   class Meta:
      model = Procesadore
      fields = '__all__'
   
   def validate_modelo(self, value):
      existe = Procesadore.objects.filter(modelo_iexact=value).exists()
      
      if existe:
         raise serializers.ValidationError("Este producto ya existe")
      return value
   
class GpuSerializer(serializers.ModelSerializer):
   
   class Meta:
      model = Gpu
      fields = '__all__'
   
   def validate_modelo(self, value):
      existe = Gpu.objects.filter(modelo_iexact=value).exists()
      
      if existe:
         raise serializers.ValidationError("Este producto ya existe")
      return value

class RamSerializer(serializers.ModelSerializer):
   
   class Meta:
      model = Ram
      fields = '__all__'
      