from rest_framework import serializers
from ..models.exercicios import Exercicios


class SerializerExercicios(serializers.ModelSerializer):
    class Meta:
        model = Exercicios
        fields = '__all__'