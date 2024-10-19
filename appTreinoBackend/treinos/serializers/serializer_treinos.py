from rest_framework import serializers

from ..models import Exercicios
from ..serializers.serializer_exercicios import SerializerExercicios
from ..models.treinos import Treinos


class SerializerTreinos(serializers.ModelSerializer):
    exercicios = SerializerExercicios(many=True)

    class Meta:
        model = Treinos
        fields = '__all__'

    def create(self, validated_data):
        exercicios_data = validated_data.pop('exercicios')

        treino = Treinos.objects.create(**validated_data)

        for exercicio_data in exercicios_data:
            Exercicios.objects.create(treino=treino, **exercicio_data)

        return treino