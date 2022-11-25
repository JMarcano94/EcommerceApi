from itertools import product
from xml.dom import ValidationErr

from User import serializer
from .serializers import RegisterProductsSerializer
from  rest_framework.generics import CreateAPIView
from Products.models import Article



class RegisterProductsView(CreateAPIView):
    queryset= Article.objects.all()
    serializer_class=RegisterProductsSerializer

        
  