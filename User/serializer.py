import datetime



from User.models import Usuarios 
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.translation import gettext as _
import jwt



class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=Usuarios.objects.all())]
            )
    
    password = serializers.CharField(max_length=20, write_only=True, required=True)
    password2 = serializers.CharField(max_length=20, write_only=True, required=True)
    

    class Meta:
        model = Usuarios
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'username': {'required': True,},
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "La contraseña no coincide"})

        return attrs

    def create(self, validated_data):
        user = Usuarios.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user



class ResetpasswordSerializer(serializers.ModelSerializer):
      email=serializers.EmailField(max_length=50)


      class Meta:

            model= Usuarios
            fields= ('email',)
            extra_kwargs = {'email': {'required': True,} }

      def validate_email(self, data):

        try:

          email=Usuarios.objects.get(email=data)

          return data

        except Usuarios.DoesNotExist:
          raise serializers.ValidationError("El correo no es correcto")

    
       
      def create(self, validate_data): 
        email=validate_data.get('email')

        
        key= "lgsus"
        token = jwt.encode({ 'email': email }, "lgsus", algorithm="HS256")
        

        c= {
					
					'domain':'127.0.0.1:8000',
					'site_name': 'LgsusTest',
					"user": Usuarios,
					'token': token,
					'protocol': 'http',
					}

        send_mail(
          
          subject= 'Reseto de contraseña',
          message= '',
          html_message= render_to_string('reset_password.html', c),
          from_email=  'moreyalejandro1@gmail.com',
          recipient_list= [email],
          
        )
       
        return validate_data

class ChangePasswordSerializer(serializers.ModelSerializer):

    new_password1 = serializers.CharField(max_length=28, write_only=True, required=True)
    new_password2 = serializers.CharField(max_length=28, write_only=True, required=True)
    user=None
    class Meta:
        model = Usuarios
        fields = ('new_password1', 'new_password2')

    def validate(self, data):
        token = self.context['token']  
        payload=jwt.decode(token, "lgsus", algorithms=["HS256"])
        self.user = Usuarios.objects.get(email=payload['email'])

        if self.user.DoesNotExist:
            raise serializers.ValidationError({'El usuario no existe': _("El usuario solicitado no existe")})


        if data['new_password1'] != data['new_password2']:
            raise serializers.ValidationError({'new_password2': _("Las Contraseñas no coinciden")})
        validate_password(data['new_password1'], self.user)
        return data  
       
    def create(self, validated_data, **kwargs):
        password = validated_data['new_password1']
        self.user.set_password(password)
        self.user.save()
        return self.user
