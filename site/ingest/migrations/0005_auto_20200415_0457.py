# Generated by Django 3.0.4 on 2020-04-15 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingest', '0004_remove_paciente_color_de_pero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clasificacionepidemiologica',
            name='nombre_ce',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='nombre_departamento',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='localidad',
            name='nombre_localidad',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nombre_paciente',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='pais',
            name='nombre_pais',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='sintoma',
            name='nombre_sintoma',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='tipoevento',
            name='nombre_tipo_evento',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
