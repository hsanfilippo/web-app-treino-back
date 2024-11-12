from rest_framework import serializers
from ..models.exercicios import Exercicios


class SerializerExercicios(serializers.ModelSerializer):
    agrup_musc = serializers.CharField(allow_blank=True, required=False)
    tecnica_avanc = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = Exercicios
        fields = '__all__'