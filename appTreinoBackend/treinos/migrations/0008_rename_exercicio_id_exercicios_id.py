# Generated by Django 5.1.1 on 2024-09-11 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treinos', '0007_alter_exercicios_treino'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercicios',
            old_name='exercicio_id',
            new_name='id',
        ),
    ]
