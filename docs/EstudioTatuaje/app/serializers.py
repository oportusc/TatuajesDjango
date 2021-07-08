from django.db.models import fields, query
from .models import Marca, Producto
from rest_framework import serializers

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'



class ProductoSerializer(serializers.ModelSerializer):
    marca = serializers.CharField(read_only = True, source="marca.nombre")
    # marca = MarcaSerializer(read_only=True)
    marca_id = serializers.PrimaryKeyRelatedField(queryset=Marca.objects.all(), source="marca")
    
    class Meta:
        model = Producto
        exclude = ['descripcion','imagen']