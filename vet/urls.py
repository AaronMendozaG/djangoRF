from django.urls import path

#Views

from .views import PetOwnersListCreate, PetsList,PetOwnerRetrieveUpdateDestroyAPIView, PetRetriveUpdateDestroyAPIView


urlpatterns = [
    path("owners/", PetOwnersListCreate.as_view(), name="owners_list-create"),
    path("owners/<int:pk>", PetOwnerRetrieveUpdateDestroyAPIView.as_view(), name="owner_retrive-update-destroy"),
    path("pets/", PetsList.as_view(), name="pets_list-create"),
    path("pets/<int:pk>", PetRetriveUpdateDestroyAPIView.as_view(), name="pet_detail")
]
