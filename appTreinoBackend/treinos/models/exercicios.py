import uuid

from django.db import models

from ..models.treinos import Treinos


class Exercicios(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    agrup_musc = models.TextField()
    nome_exerc = models.CharField(max_length=30)
    series = models.IntegerField()
    reps = models.IntegerField()
    carga = models.IntegerField()
    interv_seg = models.IntegerField()
    tecnica_avanc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    treino = models.ForeignKey(Treinos, related_name='exercicios', null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.nome_exerc
