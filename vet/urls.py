from django.urls import path

#Views

# from .views import PetOwnersListCreateAPIView, PetsListCreateAPIView,PetOwnerRetrieveUpdateDestroyAPIView, PetRetriveUpdateDestroyAPIView
from rest_framework.authtoken import views as authtoken_views
from .views import (PetOwnerListCreateAPIView,
                    PetListCreateAPIView,
                    PetOwnersRetrieveUpdateDestroyAPIView, 
                    PetRetrieveUpdateDestroyAPIView,
                    PetsDatesListCreateAPIView,
                    PetsDatesRetrieveUpdateDestroyAPIView,
                    PetOwnersDatesListCreateAPIView,
                    )

urlpatterns = [
    # path("owners/", PetOwnersListCreateAPIView.as_view(), name="owners_list-create"),
    # path("owners/<int:pk>", PetOwnerRetrieveUpdateDestroyAPIView.as_view(), name="owner_retrive-update-destroy"),
    # path("pets/", PetsListCreateAPIView.as_view(), name="pets_list-create"),
    # path("pets/<int:pk>", PetRetriveUpdateDestroyAPIView.as_view(), name="pet_retrive-update-destroy")
    path("auth-token", authtoken_views.obtain_auth_token, name="token-auth" ),
    path("owners/", PetOwnerListCreateAPIView.as_view(), name="owners_list-create"),
    path("owners/<int:pk>", PetOwnersRetrieveUpdateDestroyAPIView.as_view(), name="owner_retrive-update-destroy"),
    path(
        "owners/<int:pk>/dates",
        PetOwnersDatesListCreateAPIView.as_view(),
        name="owners_dates_list",
    ),
    path("pets/", PetListCreateAPIView.as_view(), name="pets_list-create"),
    path("pets/<int:pk>", PetRetrieveUpdateDestroyAPIView.as_view(), name="pet_retrive"),
    path("dates/", PetsDatesListCreateAPIView.as_view(), name="petDate_list-create"),
    path("dates/<int:pk>", PetsDatesRetrieveUpdateDestroyAPIView.as_view(), name="petDate_retrive-update-destroy")
]
