from .models import Pedidos, logs
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from User.models import Usuarios
from rest_framework.permissions import DjangoModelPermissions




class CreateLogs(serializers.ModelSerializer):
    

    class Meta:
        model=logs
        fields= ['pedido_asociado','log', 'user_encargado']

    def to_representation(self,instance):
        return {
            'log': instance.log,
            'user_encargado': instance.user_encargado,
            'pedido_asociado': instance.pedido_asociado,            
        }    
    

class CreateOrdersSerializer(serializers.ModelSerializer):
   


    class Meta:
        model = Pedidos
        fields = ['numero','mensajero','fecha_creado','estado_pedido','direccion_pedido']

        estado_pedido=serializers.CharField(read_only=True)
   
   

    def create(self, validated_data):
        pedido = Pedidos.objects.create(
            mensajero= validated_data['mensajero'],
            estado_pedido= validated_data['estado_pedido'],
            direccion_pedido= validated_data['direccion_pedido']
        )

        return pedido
 


    def to_representation(self,instance):
        return {
            'numero': instance.numero,
            'mensajero': "Pendiente por asignar",
            'fecha_pedido' : instance.fecha_creado.strftime("%Y-%m-%d %H:%M:%S"),
            'estado_pedido': "Pendiente",            
            'direccion': instance.direccion_pedido,  
        }    

    
class ListPedidosSerializer(serializers.ModelSerializer):

    


    class Meta:
        model= Pedidos  
        exclude= ['fecha_actualizado']
    
 


class UpdateOrderSerializer(serializers.ModelSerializer):

    
  

    class Meta:
        model= Pedidos  
        exclude= ['fecha_creado','direccion_pedido']

    def validate_estado_pedido(self,request,pk,*args, **kwargs):

        
        estados_antiguos=request.data(numero=pk)
        estado_original=Pedidos.objects.filter(estado_pedido=estados_antiguos)

    def validate_mensajero(self, value):
        if value == '' or value == None:
            raise serializers.ValidationError({"Mensajero": "Debe asignar un mensajero para enviar pedido"})

        
    def update(self, instance, validated_data):
    # Actualizar datos de orden
        instance.mensajero = validated_data.get('mensajero', instance.mensajero)
        instance.estado_pedido = validated_data.get('estado_pedido', instance.estado_pedido)
        instance.save()
    
    def to_representation(self,instance):
        return {
            'numero': instance.numero,
            'mensajero': instance.mensajero,
            'fecha_actualizado' : instance.fecha_creado.strftime("%Y-%m-%d %H:%M:%S"),
            'estado_pedido': instance.estado_pedido,          
            'direccion': instance.direccion_pedido,  
        }    

    def save(self,instance):
        usuario= self.context['user']
        created_log=logs.objects.create(
            usuario_encargado= usuario,
            pedido_asociado=instance.numero

                )

        

