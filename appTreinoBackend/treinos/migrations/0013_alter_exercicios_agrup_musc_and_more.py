# Generated by Django 5.1.1 on 2024-11-12 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treinos', '0012_alter_exercicios_agrup_musc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercicios',
            name='agrup_musc',
            field=models.TextField(default=' ', null=True),
        ),
        migrations.AlterField(
            model_name='exercicios',
            name='tecnica_avanc',
            field=models.TextField(default=' ', null=True),
        ),
    ]
