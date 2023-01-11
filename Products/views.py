from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterProductsSerializer
from  rest_framework.generics import CreateAPIView
from Products.models import Article
from Pedidos.permissions import CustomDjangoModelPermissions



class RegisterProductsView(CreateAPIView):
    queryset= Article.objects.all()
    serializer_class=RegisterProductsSerializer
    permission_classes= [CustomDjangoModelPermissions]

        
    def put(self, request, pk=None, format=None):

        serializer = RegisterProductsSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
       
        producto = Article.objects.filter(pk=pk).first()
        if producto:
            producto.delete()
            serializer=RegisterProductsSerializer(producto)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

"""
    Ordenes List y Post
"""
"""class OrdenesList(APIView):


def post(self, request):
    serializer = OrdenesCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrdenesDetail(APIView):
permission_classes = (IsAuthenticated, )
        
def get_object(self, pk):
    try:
        return Orden.objects.get(pk=pk)  
    except Orden.DoesNotExist:
        raise Http404
    
def put(self, request, pk, format=None):
    orden = self.get_object(pk)     
    serializer = OrdenesUpdateSerializer(orden, data=request.data)
    if serializer.is_valid():
           return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


def delete(self, request, pk, format=None):
    orden = self.get_object(pk)
    orden.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)"""