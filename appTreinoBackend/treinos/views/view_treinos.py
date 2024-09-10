from rest_framework import generics

from ..models import Treinos
from ..serializers import SerializerTreinos


class ListarTreinos(generics.ListCreateAPIView):
    queryset = Treinos.objects.all()
    serializer_class = SerializerTreinos


class EditarTreinos(generics.RetrieveUpdateDestroyAPIView):
    queryset = Treinos.objects.all()
