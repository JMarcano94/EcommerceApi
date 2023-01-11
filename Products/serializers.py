
from .models import Article
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.validators import UniqueTogetherValidator


class RegisterProductsSerializer(serializers.ModelSerializer):
   
   

    class Meta:
        model = Article
        fields = ('name', 'section', 'description', 'unit_price')

        extra_kwargs = {
            'name': {'required': True},
            'section': {'required': True},
            'unit_price': {'required': True},
        }
        validators = [
            UniqueTogetherValidator(
                queryset=Article.objects.all(),
                fields=['name']
            )
        ]

    

    def create(self, validated_data):
        product = Article.objects.create(
            name= validated_data['name'],
            section= validated_data['section'],
            description= validated_data['description'],
            unit_price= validated_data['unit_price']
        )

        return product


  
    def to_representation(self,instance):
        return {
            'id': instance.id,
            'name': instance.name,            
            'description': instance.description,
            
        }    


"""class OrdenDetalleSerializer(serializers.ModelSerializer):
producto = ProductosSerializer(read_only=True, many=False)
producto_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Productos.objects.all(), source='producto')

class Meta:
    model = Orden_Detalles
    fields = ('id','producto','producto_id','costo',)


   Orden Detalle Update

class OrdenDetalleUpdateSerializer(serializers.ModelSerializer):
producto = ProductosSerializer(read_only=True, many=False)
producto_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Productos.objects.all(), source='producto')

class Meta:
    model = Orden_Detalles
    fields = ('id','producto','producto_id','costo',)
    extra_kwargs = {'id': {'read_only':False}}

   Ordenes Create

class OrdenesCreateSerializer(serializers.ModelSerializer):
orden_details = Orden_DetailSerializer(many=True)   

class Meta:
    model = Orden
    fields = '__all__'

def create(self, validated_data):
    #Obtener el contenido de orden_details
    orden_details_data = validated_data.pop('orden_details')
    
    #Creamos el nuevo registro de la orden
    nueva_orden = Orden.objects.create(**validated_data)
    
    #En un ciclo, recorremos el orden_detail y creamos el nuevo registro
    for orden_detail in orden_details_data:
        Orden_Details.objects.create(**orden_detail, orden=nueva_orden)       
    return nueva_orden



    Orden Editar, cree un nuevo serializer para actualizar la info de Orden Detalle,
    para poder acceder al id de la orden_detalle

class OrdenesUpdateSerializer(serializers.ModelSerializer):
orden_details = OrdenDetalleUpdateSerializer(many=True)

class Meta:
    model = Ordenes
    fields = ('id','status','total',
             'tipo_pago','usuario','orden_details',)

def update(self, instance, validated_data):
    # Actualizar datos de orden
    instance.total = validated_data.get('total', instance.total)
    instance.status = validated_data.get('status', instance.status)
    instance.tipo_pago = validated_data.get('tipo_pago', instance.tipo_pago)
    instance.usuario = validated_data.get('usuario', instance.usuario)
    instance.save()
    orden_details_data = validated_data.pop('orden_details')
    
    # Datos de Orden Detalles
    if orden_details_data:
        for orden_detail in orden_details_data:
            orden_detail_id = Orden_Detalles.get('id',None)
            if orden_detail_id:
                update_order_detail = Orden_Detalles.objects.get(id=orden_detail_id)
                update_order_detail.producto = orden_detail.get('aplicacion_nutricion_id',update_order_detail.aplicacion_nutricion)
                update_order_detail.costo = orden_detail.get('costo',update_order_detail.costo)
                update_order_detail.save()
            else:
                #En caso de no existir el id, crear un nuevo registro
                Orden_Detalles.objects.create(**orden_detail, orden=instance)
    else:
        # posiblemente se eliminarian en caso de existir
        pass
    
   return instance"""