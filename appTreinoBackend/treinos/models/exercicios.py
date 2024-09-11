import uuid

from django.db import models

class Exercicios(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    agrup_musc = models.TextField()
    nome_exerc = models.CharField(max_length=30)
    series = models.IntegerField()
    reps = models.IntegerField()
    carga = models.IntegerField()
    interv_seg = models.IntegerField()
    tecnica_avanc = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.nome_exerc