from rest_framework.response import Response
from rest_framework import status
from Pedidos.models import Pedidos, logs
from .serializers import CreateOrdersSerializer, UpdateOrderSerializer, ListPedidosSerializer, CreateLogs
from rest_framework import generics
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import CustomDjangoModelPermissions
from django.shortcuts import get_object_or_404


class CreateOrdersViews(generics.ListCreateAPIView):

    queryset= Pedidos.objects.all()
    serializer_class=CreateOrdersSerializer
    permission_classes= [CustomDjangoModelPermissions]
   
    def post(self, request, pk=None, format=None):

        serializer = CreateOrdersSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
 
    """def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request.user})
        print(context)
        return context"""
              

class ListPedidosView(generics.ListAPIView):

        queryset = Pedidos.objects.all()
        serializer_class= ListPedidosSerializer
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['estado_pedido', 'fecha_creado']
        permission_classes= [CustomDjangoModelPermissions]
       

             

class UpdateOrderView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Pedidos.objects.all()
    serializer_class=UpdateOrderSerializer
    permission_classes= [CustomDjangoModelPermissions]
    
    
  
   
    def get(self, request, pk, *args, **kwargs):

        try:
          
            queryset = Pedidos.objects.get(numero=pk)
            serializer = UpdateOrderSerializer(queryset)
            current_user=request.user

            return Response(serializer.data)

        except Pedidos.DoesNotExist:

                return Response(status=status.HTTP_404_NOT_FOUND)
    

    
    def patch(self,instance, request, pk=None, format=None, *args, **kwargs):

        pk = self.kwargs.get('pk')
        serializer = UpdateOrderSerializer(data=request.POST)
        save_allowance = get_object_or_404(Pedidos.objects.all(), pk=pk)
        data = request.data.get('allowance')
        serializer = UpdateOrderSerializer(instance=save_allowance,data=data,partial=True)
        if serializer.is_valid(raise_exception=True):
            allowance_saved=serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk, format=None, *args, **kwargs):
        
       
        pedido= Pedidos.objects.filter(pk=pk).first()
        if pedido:
            pedido.delete()
            serializer=UpdateOrderSerializer(pedido)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
      
    """def get_serializer_context(self):
        user=self.request.user
        ctx = super().get_serializer_context()
        ctx['user'] = self.kwargs['user']
        return ctx"""

    def cxt(self,request,*args, **kwargs):

        serializer = UpdateOrderSerializer(logs, context={'user': request.user})
        serializer.data
        
        return serializer.data
