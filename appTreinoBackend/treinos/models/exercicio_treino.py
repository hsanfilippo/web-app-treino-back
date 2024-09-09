import uuid
from django.db import models

from appTreinoBackend.treinos.models.exercicios import Exercicios
from appTreinoBackend.treinos.models.treinos import Treinos


class ExercicioInTreino(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    treino = models.ForeignKey(Treinos, related_name='exercicios', on_delete=models.CASCADE)
    exercicio = models.ForeignKey(Exercicios, on_delete=models.CASCADE)
    ordem = models.IntegerField()
    series = models.IntegerField()
    reps = models.IntegerField()
    carga = models.IntegerField()
    intervalo_segs = models.IntegerField()

    class Meta:
        unique_together = ['treino', 'exercicio', 'ordem']
        ordering = ['ordem']

    # def __str__(self):
    #     return f'{self.ordem} - {self.exercicio.exerc_nome} no treino {self.treino.nome}'