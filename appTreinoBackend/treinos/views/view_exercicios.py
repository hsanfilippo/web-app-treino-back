from rest_framework import generics

from ..models import Exercicios
from ..serializers import SerializerExercicios


class ListarExercicios(generics.ListCreateAPIView):
    queryset = Exercicios.objects.all()
    serializer_class = SerializerExercicios


class EditarExercicios(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercicios.objects.all()
    serializer_class = SerializerExercicios

