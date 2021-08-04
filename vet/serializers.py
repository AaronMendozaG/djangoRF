from django.db.models import fields
from rest_framework import serializers
from .models import PetOwner,Pet, PetDate

#VALIDACIONES DE DATOS DE ENTRADA Y SALIDA, NORMALIZACION DE DATOS
#PERMITE DEFINIR KEYS Y CONSTRAINTS
# class PetOwnerSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     address = serializers.CharField()
#     email = serializers.EmailField()
#     phone =  serializers.CharField()

#     #se sobrescribe el metodo a ocupar en este caso se quiere crear una nueva instancia
#     def create(self, validate_date):
#         return PetOwner.objects.create(**validate_date)


# class PetSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     name = serializers.CharField()
#     type = serializers.ChoiceField(choices=Pet.PET_TYPES)
#     owner = serializers.PrimaryKeyRelatedField(queryset=PetOwner.objects.all())

#     def create(self, validate_date):
#         return Pet.objects.create(**validate_date)




# class PetOwnerListSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     first_name = serializers.CharField(max_length=255)
#     last_name = serializers.CharField(max_length=255)


# class PetOwnerContactSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     first_name = serializers.CharField(max_length=255)
#     last_name = serializers.CharField(max_length=255)
#     email = serializers.EmailField()

# class PetListSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField(max_length=255)
#     type = serializers.CharField(max_length=255)
#     owner = PetOwnerContactSerializer()

#SERIALIZERS PARA UPDATE 

# class PetOwnerUpdateSerializer(serializers.Serializer):
#     first_name = serializers.CharField(required=False)
#     last_name = serializers.CharField(required=False)
#     address = serializers.CharField(required=False)
#     phone =  serializers.CharField(required=False)

#     #SE SOBRESCRIBE EL METODO UPDATE DEL SERIALIZER
#     def update(self, instance, validate_data):
#                                                 #SI NO HAY CAMBIO SE DEJA LA INSTANCIA
#         instance.first_name = validate_data.get("first_name", instance.first_name)
#         instance.last_name = validate_data.get("last_name", instance.last_name)
#         instance.address = validate_data.get("address", instance.address)
#         instance.phone = validate_data.get("phone",instance.phone)
#         instance.save()
#         return instance

# class PetUpdateSerializer(serializers.Serializer):
#     name = serializers.CharField(required=False)
#     type = serializers.CharField(required=False)
#     owner_id = serializers.IntegerField(required=False) 
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.type = validated_data.get("type",instance.type)
#         instance.owner_id = validated_data.get("owner_id",instance.owner_id)
#         instance.save()
#         return instance






#MODEL SERIALIZERS

class PetOwnerListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = ["id","first_name", "last_name"]
class PetOwnerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = ["id","first_name", "last_name", "address", "email","phone"]

class PetListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ["id","name","type"]
class PetModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ["id","name","type",'owner']

#PET DATES

class PetDateListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetDate
        fields = ["id","datetime","type"]

class PetDateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetDate
        fields = ["id","datetime","type","pet"]

class PetDateRetrieveModelSerializer(serializers.ModelSerializer):
    pet = PetModelSerializer()
    class Meta:
        model = PetDate
        fields = ["id","datetime","type","pet"]

class PetDateUpdateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetDate
        fields = ["id","datetime","type"]