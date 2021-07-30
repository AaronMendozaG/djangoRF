from django.shortcuts import render

#VISTAS DE DJANGO
from rest_framework.views import APIView
from rest_framework.response import Response

#SERIALIZERS
from .serializers import PetOwnerListSerializer,PetListSerializer


#MODELS
from .models import PetOwner, Pet
#APIVies es la vista mas basica
class PetOwnersList(APIView):
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