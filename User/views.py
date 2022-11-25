


from User.models import Usuarios
from rest_framework import viewsets

from .serializer import RegisterSerializer, ChangePasswordSerializer, ResetpasswordSerializer
from  rest_framework.generics import CreateAPIView
#import jwt

from User import serializer
class RegisterView(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = RegisterSerializer

class ResetPasswordView(CreateAPIView):
    queryset=Usuarios.objects.all()
    serializer_class= ResetpasswordSerializer
   


class ChangepasswordView(CreateAPIView):

    serializer_class = ChangePasswordSerializer

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['token'] = self.kwargs['token']
        return ctx

  


