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

    def update(self, instance, validated_data):
        exercicios_data = validated_data.pop('exercicios', None)

        instance.nome = validated_data.get('nome', instance.nome)
        instance.descricao = validated_data.get('descricao', instance.descricao)
        instance.save()

        if exercicios_data:
            ids_exercicios = [ex_data.get('id') for ex_data in exercicios_data if ex_data.get('id')]

            Exercicios.objects.filter(treino=instance).exclude(id__in=ids_exercicios).delete()

            for exercicio_data in exercicios_data:
                exercicio_id = exercicio_data.get('id')
                if exercicio_id:
                    exercicio = Exercicios.objects.get(id=exercicio_id, treino=instance)
                    for attr, value in exercicio_data.items():
                        setattr(exercicio, attr, value)
                    exercicio.save()
                else:
                    Exercicios.objects.create(**exercicio_data)

        return instance