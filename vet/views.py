from django.shortcuts import render
from rest_framework import serializers, status, generics, filters
from django.shortcuts import get_object_or_404
#VISTAS DE DJANGO
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
#SERIALIZERS
#from .serializers import PetOwnerSerializer, PetSerializer, PetOwnerUpdateSerializer,PetUpdateSerializer
from .serializers import (PetOwnerListModelSerializer,
                            PetListModelSerializer,
                            PetOwnerModelSerializer,
                            PetModelSerializer,
                            PetDateListModelSerializer,
                            PetDateModelSerializer,
                            PetDateUpdateModelSerializer,
                            PetDateRetrieveModelSerializer,
                        )
#MODELS
from .models import PetOwner, Pet, PetDate



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
# class PetOwnerListAPIView(generics.ListAPIView):
#     queryset = PetOwner.objects.all()
#     serializer_class = PetOwnerListSerializer

#     def get_queryset(self):
#         #EL FILTRO SE HACE OPCIONAL
#         first_name_filter = self.request.GET.get("first_name")
#         filters = {}
#         if first_name_filter:
#             filters["first_name__icontains"] = first_name_filter
#         return self.queryset.filter(**filters)

# class PetListAPIView(generics.ListAPIView):
#     queryset = Pet.objects.all()
#     serializer_class = PetListSerializer

#RETRIEVE

# class PetOwnerRetrieveAPIView(generics.RetrieveAPIView):
#     queryset = PetOwner.objects.all()
#     serializer_class = PetOwnerModelSerializer

# class PetRetrieveAPIView(generics.RetrieveAPIView):
#     queryset = Pet.objects.all()
#     serializer_class = PetListModelSerializer


#LIST-CREATE

class PetOwnerListCreateAPIView(generics.ListCreateAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = PetOwnerListModelSerializer
    #BUSQUEDA ESPECIFICA
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["first_name"]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["first_name"]
    ordering_fields = ["email"]

    # def get_queryset(self):
    #     #EL FILTRO SE HACE OPCIONAL
    #     first_name_filter = self.request.GET.get("first_name")
    #     filters = {}
    #     if first_name_filter:
    #         filters["first_name__icontains"] = first_name_filter
    #     return self.queryset.filter(**filters)
    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = PetOwnerModelSerializer
        return serializer_class

class PetOwnersDatesListCreateAPIView(generics.ListCreateAPIView):

    queryset = PetDate.objects.all()
    serializer_class = PetDateListModelSerializer

    def get_queryset(self):
        owner_id = self.kwargs["pk"]
        filters = {}
        if owner_id:
            filters["pet__owner_id"] = owner_id

        return self.queryset.filter(**filters)

class PetListCreateAPIView(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetListModelSerializer

    def get_queryset(self):
        #EL FILTRO SE HACE OPCIONAL
        name_filter = self.request.GET.get("name")
        filters = {}
        if name_filter:
            filters["name__icontains"] = name_filter
        return self.queryset.filter(**filters)
    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = PetModelSerializer
        return serializer_class

#CLASES SISMPLES (ListAPIView,Create,Retieve,Update,Destoy)
#RETRIEVE-UPDATE-DESTROY

class PetOwnersRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = PetOwner.objects.all()
    serializer_class = PetOwnerModelSerializer

class PetRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Pet.objects.all()
    serializer_class = PetModelSerializer


#PETS DATES

#LIST-CREATE

class PetsDatesListCreateAPIView(generics.ListCreateAPIView):
    queryset = PetDate.objects.all()
    serializer_class = PetDateListModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["pet__owner__first_name","pet__owner__last_name"]
    depth = 2

    # def get_queryset(self):
    #     #EL FILTRO SE HACE OPCIONAL
    #     name_filter = self.request.GET.get("name")
    #     owner_filter = self.request.GET.get("owner")
    #     filters = {}
    #     if name_filter:
    #         filters["pet__name"] = name_filter
    #     elif owner_filter:
    #         filters["pet__owner"] = owner_filter
    #     return self.queryset.filter(**filters)

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = PetDateModelSerializer
        return serializer_class

class PetsDatesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = PetDate.objects.all()
    serializer_class = PetDateRetrieveModelSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "PUT" and "PATCH":
            serializer_class = PetDateListModelSerializer
        return serializer_class