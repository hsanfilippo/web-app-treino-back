# Generated by Django 5.1.1 on 2024-09-11 14:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treinos', '0005_rename_id_exercicios_exercicio_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercicios',
            name='treino',
            field=models.ForeignKey(default='1a4ab4ce-7a3b-4d8f-bd83-fae9f9ac3c8e', on_delete=django.db.models.deletion.CASCADE, related_name='exercicios', to='treinos.treinos'),
        ),
    ]