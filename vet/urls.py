from django.urls import path

#Views

# from .views import PetOwnersListCreateAPIView, PetsListCreateAPIView,PetOwnerRetrieveUpdateDestroyAPIView, PetRetriveUpdateDestroyAPIView
from .views import (PetOwnerListCreateAPIView,
                    PetListCreateAPIView,
                    PetOwnersRetrieveUpdateDestroyAPIView, 
                    PetRetrieveUpdateDestroyAPIView,
                    PetsDatesListCreateAPIView,
                    PetsDatesRetrieveUpdateDestroyAPIView,
                    )

urlpatterns = [
    # path("owners/", PetOwnersListCreateAPIView.as_view(), name="owners_list-create"),
    # path("owners/<int:pk>", PetOwnerRetrieveUpdateDestroyAPIView.as_view(), name="owner_retrive-update-destroy"),
    # path("pets/", PetsListCreateAPIView.as_view(), name="pets_list-create"),
    # path("pets/<int:pk>", PetRetriveUpdateDestroyAPIView.as_view(), name="pet_retrive-update-destroy")

    path("owners/", PetOwnerListCreateAPIView.as_view(), name="owners_list-create"),
    path("owners/<int:pk>", PetOwnersRetrieveUpdateDestroyAPIView.as_view(), name="owner_retrive-update-destroy"),
    path("pets/", PetListCreateAPIView.as_view(), name="pets_list-create"),
    path("pets/<int:pk>", PetRetrieveUpdateDestroyAPIView.as_view(), name="pet_retrive"),
    path("dates/", PetsDatesListCreateAPIView.as_view(), name="petDate_list-create"),
    path("dates/<int:pk>", PetsDatesRetrieveUpdateDestroyAPIView.as_view(), name="petDate_retrive-update-destroy")
]
