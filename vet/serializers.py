from rest_framework import serializers

#VALIDACIONES DE DATOS DE ENTRADA Y SALIDA, NORMALIZACION DE DATOS
#PERMITE DEFINIR KEYS Y CONSTRAINTS
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