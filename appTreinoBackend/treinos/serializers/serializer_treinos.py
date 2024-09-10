from rest_framework import serializers
from ..models.treinos import Treinos


class SerializerTreinos(serializers.ModelSerializer):
    class Meta:
        model = Treinos
        fields = ['id', 'nome', 'descricao', 'created_on']