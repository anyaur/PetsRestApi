from django.conf.urls import url
from django.urls import path, re_path
from .views import (
    PetsView,
    # PetsListCreateApiView,
    # ImageList,
    PetDetail,
    PetList,
)

app_name = "pets"
urlpatterns = [
    path('pets/', PetsView.as_view()),
    # path('post/pets/', PetsListCreateApiView.as_view(), name='pets_list'),
    # path('pets/<uuid:pk>', PetsView.as_view()),
    path('post/pets/', PetList.as_view()),
    path('post/pets/<uuid:pk>/', PetDetail.as_view()),
    # re_path(r'Pet/(?:id-(?P<id>\d+)/)?$', ImageList.as_view())
]

