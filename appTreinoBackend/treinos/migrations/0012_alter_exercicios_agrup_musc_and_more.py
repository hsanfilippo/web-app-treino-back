# Generated by Django 5.1.1 on 2024-11-12 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treinos', '0011_alter_exercicios_agrup_musc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercicios',
            name='agrup_musc',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='exercicios',
            name='tecnica_avanc',
            field=models.TextField(default='', null=True),
        ),
    ]
