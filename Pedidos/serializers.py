
from User.models import Usuarios
from .models import Pedidos
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from User.models import Usuarios




class CreateOrdersSerializer(serializers.ModelSerializer):

    permission_classes = [IsAuthenticated]

    class Meta:
        model = Pedidos
        fields = ['numero','mensajero','fecha_creado','estado_pedido','direccion_pedido']

        estado_pedido=serializers.CharField(read_only=True)
   
    def create_pedido(self, validated_data):
            pedido = Pedidos.objects.create(**validated_data)
            return pedido

    def to_representation(self,instance):
        return {
            'numero': instance.numero,
            'mensajero': "Pendiente por asignar",
            'fecha_pedido' : instance.fecha_creado.strftime("%Y-%m-%d %H:%M:%S"),
            'estado_pedido': "Pendiente",            
            'direccion': instance.direccion_pedido,
            
        }    

class ListPedidos(serializers.ModelSerializer):

    class Meta:
        model= Pedidos  
        exclude= ['fecha_actualizado']


class UpdateOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model= Pedidos  
        exclude= ['fecha_creado','direccion_pedido']

    def validate_estado_pedido(self,value):
        estado_original=Pedidos.objects.filter

    def validate_mensajero(self, value):
        if value == '' or value == None:
            raise serializers.ValidationError({"Mensajero": "Debe asignar un mensajero para enviar pedido"})

        
    def update(self, instance, validated_data):
        print (instance)
        return super().update(instance, validated_data)

