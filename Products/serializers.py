from enum import unique
from opcode import stack_effect
from unicodedata import name
from venv import create
from .models import Article
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.validators import UniqueTogetherValidator


class RegisterProductsSerializer(serializers.ModelSerializer):
    permission_classes = [IsAuthenticated]
    

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