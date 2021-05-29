from rest_framework import status, generics
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.generics import (
    ListCreateAPIView,
    ListAPIView, get_object_or_404
)
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Pet
from .serializers import PetSerializer


class PetsView(APIView):
    def get(self, request):
        pets = Pet.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = PetSerializer(pets, many=True)
        return Response({"count": len(pets), "items": serializer.data})


class PetList(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def perform_create(self, serializer):
        serializer.save()


class PetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
