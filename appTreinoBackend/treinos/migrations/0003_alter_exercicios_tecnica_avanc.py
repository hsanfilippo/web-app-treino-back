# Generated by Django 5.1.1 on 2024-09-11 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treinos', '0002_rename_exercicio_id_exercicios_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercicios',
            name='tecnica_avanc',
            field=models.TextField(null=True),
        ),
    ]