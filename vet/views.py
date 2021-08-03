from django.shortcuts import render
from rest_framework import serializers
from django.shortcuts import get_object_or_404

#VISTAS DE DJANGO
from rest_framework.views import APIView
from rest_framework.response import Response

#SERIALIZERS
from .serializers import PetOwnerListSerializer,PetListSerializer,PetOwnerSerializer, PetSerializer


#MODELS
from .models import PetOwner, Pet
#APIVies es la vista mas basica
class PetOwnersListCreate(APIView):
    """
    View to list all pet Owners in the system
    """
    serializer_class = PetOwnerListSerializer

    def get(self,request):
        # self: Hace referencia a la misma clase u objeto
        #SIEMPRE TIENEN EL CONTEXTO DE LA CLASE Y EL REQUEST
        #.__dict__ traduce una clase a un objeto legible
        # print(request.__dict__)
        # print(PetOwner.objects.all())
        owners_queryset = PetOwner.objects.all()
        # owners = [
        #     {
        #         "id": owner.id , 
        #         "first_name": owner.first_name
        #     } 
        #     for owner in PetOwner.objects.all()
        # ]

        #many= trae varias instancias 
        serializer = self.serializer_class(owners_queryset,many=True)
        #.data es una propiedad de serializer en donde se guarda o almacena la data limpia
        return Response(data=serializer.data)

    def post(self,request):
        serializer = PetOwnerSerializer(data=request.data)
        
        #si todo sale bien yo puedo hacer lo siguiente
        serializer.is_valid(raise_exception=True)
        create_instance = serializer.save()
        print(create_instance.__dict__)

        return Response({})






class PetsList(APIView):
    """
    View to list all pets in the system
    """
    serializer_class = PetListSerializer
    def get(self,request):

        pets_queryset = Pet.objects.all()
        # pets = [
        #     {
        #         "id":pet.id,
        #         "name":pet.name,
        #         "type":pet.type,
        #         "owner":pet.owner.first_name
        #     }
        #     for pet in pets_queryset 
        # ]
        serializer = self.serializer_class(pets_queryset,many=True)
        return Response(data=serializer.data)

    def post(self,request):
        serializer = PetSerializer(data=request.data)
        
        #si todo sale bien yo puedo hacer lo siguiente
        serializer.is_valid(raise_exception=True)
        create_instance = serializer.save()
        print(create_instance.__dict__)

        return Response({})


#VISTAS DE DETALLE
#RENOMBRAR CLASES CON LAS ACCIONES UPDATE Y DESTORY
class PetOwnerRetrieveUpdateDestroyAPIView(APIView):
    '''
    View the datail of one Pet Owner 
    '''

    serializer_class = PetOwnerSerializer

    def get(self,request,pk):
        owner = get_object_or_404(PetOwner, id=pk)
        serializer = self.serializer_class(owner)
        return Response(serializer.data)
        # owner_queryset = PetOwner.objects.get(id=pk)
        # serializer = self.serializer_class(owner_queryset)
        # return Response(data=serializer.data)
    
    #SOBRESCRIBIR PUT(TODOS LOS ELEMENTOS) PATCH(UNO O VARIOS, PARCIALMENTE)

    def patch(self, request,pk):
        owner = get_object_or_404(PetOwner, id=pk)


class PetRetriveUpdateDestroyAPIView(APIView):
    '''
    View the datail of one Pet Owner 
    '''

    serializer_class = PetSerializer

    def get(self, request, pk):

        # pet_queryset = Pet.objects.get(id=pk)
        # serializer = self.serializer_class(pet_queryset)
        # return Response(data=serializer.data)
        pet = get_object_or_404(Pet, id=pk)
        serializer = self.serializer_class(pet)
        return Response(serializer.data)