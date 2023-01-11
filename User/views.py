from User.models import Usuarios
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializer import RegisterSerializer, ChangePasswordSerializer, ResetpasswordSerializer
from  rest_framework.generics import CreateAPIView
#import jwt

from User import serializer
class RegisterView(viewsets.ModelViewSet):
    permission_classes=[AllowAny]
    queryset = Usuarios.objects.all()
    serializer_class = RegisterSerializer

class ResetPasswordView(CreateAPIView):
    permission_classes=[AllowAny]
    queryset=Usuarios.objects.all()
    serializer_class= ResetpasswordSerializer
    serializer_class.is_valid
    serializer_class.save
   


class ChangepasswordView(CreateAPIView):

    serializer_class = ChangePasswordSerializer
    permission_classes=[AllowAny]

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['token'] = self.kwargs['token']
        return ctx

  


