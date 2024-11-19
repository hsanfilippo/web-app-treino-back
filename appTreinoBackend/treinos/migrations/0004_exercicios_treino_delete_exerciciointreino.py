# Generated by Django 5.1.1 on 2024-09-11 13:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treinos', '0003_alter_exercicios_tecnica_avanc'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercicios',
            name='treino',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='exercicios', to='treinos.treinos'),
        ),
        migrations.DeleteModel(
            name='ExercicioInTreino',
        ),
    ]