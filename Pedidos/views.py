from rest_framework.response import Response
from rest_framework import status
from Pedidos.models import Pedidos
from .serializers import CreateOrdersSerializer, UpdateOrderSerializer
from rest_framework import generics
import django_filters.rest_framework
from rest_framework.views import APIView


class CreateOrdersViews(generics.ListCreateAPIView):

    Model= Pedidos
    serializer_class= CreateOrdersSerializer
    queryset= Pedidos.objects.all()
    
    def post(self, request):
        serializer = CreateOrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class ListPedidosView(generics.ListAPIView):

        queryset = Pedidos.objects.all()
        serializer_class=UpdateOrderSerializer
        filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
        filterset_fields = ['estado_pedido']

        def list(self, request):

            try:
       
                queryset = self.get_queryset()
                serializer = UpdateOrderSerializer(queryset, many=True)
                return Response(serializer.data)
            except Pedidos.DoesNotExist:

                return Response(status=status.HTTP_404_NOT_FOUND)


class UpdateOrderView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Pedidos.objects.all()
    serializer_class=UpdateOrderSerializer

   
    def get(self, request):

        try:
       
            queryset = self.get_queryset()
            serializer = UpdateOrderSerializer(queryset, many=True)
            return Response(serializer.data)
        except Pedidos.DoesNotExist:

                return Response(status=status.HTTP_404_NOT_FOUND)
    


    def put(self, request, pk=None, format=None):
        serializer = UpdateOrderSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk, format=None):
        pedido= Pedidos.objects.filter(pk=pk).first()
        if pedido:
            pedido.delete()
            serializer=UpdateOrderSerializer(pedido)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
      
