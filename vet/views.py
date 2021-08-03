from django.shortcuts import render
from rest_framework import serializers, status, generics
from django.shortcuts import get_object_or_404
#VISTAS DE DJANGO
from rest_framework.views import APIView
from rest_framework.response import Response
#SERIALIZERS
from .serializers import PetOwnerListSerializer,PetListSerializer,PetOwnerSerializer, PetSerializer, PetOwnerUpdateSerializer,PetUpdateSerializer
#MODELS
from .models import PetOwner, Pet



#APIViews es la vista mas basica
# class PetOwnersListCreateAPIView(APIView):
#     """
#     View to list all pet Owners in the system
#     """
#     serializer_class = PetOwnerListSerializer

#     def get(self,request):
#         # self: Hace referencia a la misma clase u objeto
#         #SIEMPRE TIENEN EL CONTEXTO DE LA CLASE Y EL REQUEST
#         #.__dict__ traduce una clase a un objeto legible
#         # print(request.__dict__)
#         # print(PetOwner.objects.all())
#         owners_queryset = PetOwner.objects.all()
#         # owners = [
#         #     {
#         #         "id": owner.id , 
#         #         "first_name": owner.first_name
#         #     } 
#         #     for owner in PetOwner.objects.all()
#         # ]

#         #many= trae varias instancias 
#         serializer = self.serializer_class(owners_queryset,many=True)
#         #.data es una propiedad de serializer en donde se guarda o almacena la data limpia
#         return Response(data=serializer.data)

#     def post(self,request):
#         serializer = PetOwnerSerializer(data=request.data)
        
#         #si todo sale bien yo puedo hacer lo siguiente
#         serializer.is_valid(raise_exception=True)
#         create_instance = serializer.save()
#         serialized_instance = PetOwnerSerializer(create_instance)

#         return Response(serialized_instance.data, status=status.HTTP_201_CREATED)

###LISTA DE PETS

# class PetsListCreateAPIView(APIView):
#     """
#     View to list all pets in the system
#     """
#     serializer_class = PetListSerializer
#     def get(self,request):

#         pets_queryset = Pet.objects.all()
#         # pets = [
#         #     {
#         #         "id":pet.id,
#         #         "name":pet.name,
#         #         "type":pet.type,
#         #         "owner":pet.owner.first_name
#         #     }
#         #     for pet in pets_queryset 
#         # ]
#         serializer = self.serializer_class(pets_queryset,many=True)
#         return Response(data=serializer.data)

#     def post(self,request):
#         serializer = PetSerializer(data=request.data)
        
#         #si todo sale bien yo puedo hacer lo siguiente
#         serializer.is_valid(raise_exception=True)
#         create_instance = serializer.save()
#         serialized_instance = PetSerializer(create_instance)

#         return Response(serialized_instance.data, status=status.HTTP_201_CREATED)


# #VISTAS DE DETALLE
# #RENOMBRAR CLASES CON LAS ACCIONES UPDATE Y DESTORY
# class PetOwnerRetrieveUpdateDestroyAPIView(APIView):
#     '''
#     View the datail of one Pet Owner 
#     '''

#     serializer_class = PetOwnerSerializer

#     def get(self,request,pk):
#         owner = get_object_or_404(PetOwner, id=pk)
#         serializer = self.serializer_class(owner)
#         return Response(serializer.data)
#         # owner_queryset = PetOwner.objects.get(id=pk)
#         # serializer = self.serializer_class(owner_queryset)
#         # return Response(data=serializer.data)
    
#     #SOBRESCRIBIR PUT(TODOS LOS ELEMENTOS) PATCH(UNO O VARIOS, PARCIALMENTE)

#     def patch(self, request,pk):
#         owner = get_object_or_404(PetOwner, id=pk)
#         serializer = PetOwnerUpdateSerializer(instance=owner, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         updated_instante = serializer.save()
#         serialized_instace = self.serializer_class(updated_instante)
#         return Response(serialized_instace.data)
    
#     def delete(self, request, pk):
#         owner = get_object_or_404(PetOwner, id=pk)
#         owner.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class PetRetriveUpdateDestroyAPIView(APIView):
#     '''
#     View the datail of one Pet Owner 
#     '''

#     serializer_class = PetSerializer

#     def get(self, request, pk):

#         # pet_queryset = Pet.objects.get(id=pk)
#         # serializer = self.serializer_class(pet_queryset)
#         # return Response(data=serializer.data)
#         pet = get_object_or_404(Pet, id=pk)
#         serializer = self.serializer_class(pet)
#         return Response(serializer.data)
    
#     def patch(self, request,pk):
#         pet = get_object_or_404(Pet, id=pk)
#         serializer = PetUpdateSerializer(instance=pet, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         updated_instante = serializer.save()
#         serialized_instace = self.serializer_class(updated_instante)
#         return Response(serialized_instace.data)
    
#     def delete(self, request, pk):
#         pet = get_object_or_404(Pet, id=pk)
#         pet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#MIXIN -> CLASE QUE NO FUNCIONA POR SI SOLA, NECESITA SER HEREDADA
##VISTAS GENERICAS BASADAS EN CLASE from rest_framework import generics


#LISTADO
class PetOwnerListAPIView(generics.ListAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = PetOwnerListSerializer

class PetListAPIView(generics.ListAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetListSerializer
    

