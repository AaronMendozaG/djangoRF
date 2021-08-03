from rest_framework import serializers
from .models import PetOwner,Pet

#VALIDACIONES DE DATOS DE ENTRADA Y SALIDA, NORMALIZACION DE DATOS
#PERMITE DEFINIR KEYS Y CONSTRAINTS
class PetOwnerSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    address = serializers.CharField()
    email = serializers.EmailField()
    phone =  serializers.CharField()

    #se sobrescribe el metodo a ocupar en este caso se quiere crear una nueva instancia
    def create(self, validate_date):
        return PetOwner.objects.create(**validate_date)


class PetSerializer(serializers.Serializer):
    name = serializers.CharField()
    type = serializers.CharField()
    owner = serializers.PrimaryKeyRelatedField(queryset=PetOwner.objects.all())

    def create(self, validate_date):
        return Pet.objects.create(**validate_date)


class PetOwnerListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)

class PetOwnerContactSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.EmailField()

class PetListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    type = serializers.CharField(max_length=255)
    owner = PetOwnerContactSerializer()

#SERIALIZERS PARA UPDATE 

class PetOwnerUpdateSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    phone =  serializers.CharField(required=False)