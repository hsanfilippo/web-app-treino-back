from rest_framework import serializers

from ..serializers.serializer_exercicios import SerializerExercicios
from ..models.treinos import Treinos


class SerializerTreinos(serializers.ModelSerializer):
    exercicios = SerializerExercicios(many=True, read_only=True)

    class Meta:
        model = Treinos
        fields = '__all__'
