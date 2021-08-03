from django.urls import path

#Views

# from .views import PetOwnersListCreateAPIView, PetsListCreateAPIView,PetOwnerRetrieveUpdateDestroyAPIView, PetRetriveUpdateDestroyAPIView
from .views import PetOwnerListAPIView,PetListAPIView,PetOwnerRetrieveAPIView,PetRetrieveAPIView

urlpatterns = [
    # path("owners/", PetOwnersListCreateAPIView.as_view(), name="owners_list-create"),
    # path("owners/<int:pk>", PetOwnerRetrieveUpdateDestroyAPIView.as_view(), name="owner_retrive-update-destroy"),
    # path("pets/", PetsListCreateAPIView.as_view(), name="pets_list-create"),
    # path("pets/<int:pk>", PetRetriveUpdateDestroyAPIView.as_view(), name="pet_retrive-update-destroy")

    path("owners/", PetOwnerListAPIView.as_view(), name="owners_list-create"),
    path("owners/<int:pk>", PetOwnerRetrieveAPIView.as_view(), name="owner_retrive"),
    path("pets/", PetListAPIView.as_view(), name="pets_list-create"),
    path("pets/<int:pk>", PetRetrieveAPIView.as_view(), name="pet_retrive")
]
