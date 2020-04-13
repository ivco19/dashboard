# Generated by Django 3.0.4 on 2020-04-13 05:33

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ingest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClasificacionEpidemiologica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Clasificaciones Epidemiologicas',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id_departamento', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DeterminacionResultado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nombre', models.CharField(max_length=255)),
                ('notas', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Determinaciones de Resultados',
            },
        ),
        migrations.CreateModel(
            name='Financiamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id_localidad', models.IntegerField(unique=True)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingest.Departamento')),
            ],
            options={
                'verbose_name_plural': 'Localidades',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id_pais', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Paises',
            },
        ),
        migrations.CreateModel(
            name='Sintoma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nombre', models.CharField(max_length=255)),
                ('notas', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoEvento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nombre', models.CharField(max_length=255)),
                ('notas', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id_provincia', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=255)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provincias', to='ingest.Pais')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nombre', models.CharField(max_length=255)),
                ('sexo', models.CharField(choices=[('M', 'M'), ('F', 'F'), ('O', 'O')], max_length=2)),
                ('sepi_apertura', models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('edad_actual', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(200)])),
                ('causa_fallecimiento_vinculada', models.BooleanField()),
                ('causa_fallecimiento', models.CharField(max_length=255)),
                ('fis', models.DateField()),
                ('antecedente_epidemiologico', models.CharField(max_length=255)),
                ('fallecido', models.BooleanField()),
                ('fecha_fallecimiento', models.DateField()),
                ('fecha_apertura', models.DateField()),
                ('ocupacion', models.CharField(max_length=255)),
                ('grupo_etario', models.CharField(choices=[('0-10', '0-10'), ('10-20', '10-20'), ('20-30', '20-30'), ('30-40', '30-40'), ('40-50', '40-50'), ('50-60', '50-60'), ('60-70', '60-70'), ('70-80', '70-80'), ('80-90', '80-90'), ('90-100', '90-100'), ('> 100', '> 100')], max_length=50)),
                ('grupo_etario_decada', models.IntegerField(choices=[(10, 10), (20, 20), (30, 30), (40, 40), (50, 50), (60, 60), (70, 70), (80, 80), (90, 90), (100, 100), (110, 110), (120, 120), (200, 200)])),
                ('asma', models.BooleanField(default=False)),
                ('bajo_peso', models.BooleanField(default=False)),
                ('bronquio_previa', models.BooleanField(default=False)),
                ('dbt', models.BooleanField(default=False)),
                ('embarazo', models.BooleanField(default=False)),
                ('enf_neuro_previa', models.BooleanField(default=False)),
                ('enf_onco_previa', models.BooleanField(default=False)),
                ('epoc', models.BooleanField(default=False)),
                ('hepato_cronica', models.BooleanField(default=False)),
                ('hta', models.BooleanField(default=False)),
                ('inmunos_congenita', models.BooleanField(default=False)),
                ('insf_cardiaca', models.BooleanField(default=False)),
                ('insf_renal', models.BooleanField(default=False)),
                ('nac_previa', models.BooleanField(default=False)),
                ('obesidad', models.BooleanField(default=False)),
                ('prematuro', models.BooleanField(default=False)),
                ('sin_comorb', models.BooleanField(default=False)),
                ('tbc', models.BooleanField(default=False)),
                ('notas', models.TextField()),
                ('financiamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingest.Financiamiento')),
                ('localidad_residencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingest.Localidad')),
                ('provincia_carga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingest.Provincia')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id_snvs_grupo_evento', models.IntegerField()),
                ('fecha_mod_diag', models.DateField()),
                ('fecha_cui_intensivos', models.DateField()),
                ('min_ftm', models.DateField()),
                ('id_eventocaso', models.IntegerField(unique=True)),
                ('muestra_ftm', models.CharField(max_length=255)),
                ('asist_resp_mecanica', models.BooleanField()),
                ('internado', models.BooleanField()),
                ('curado', models.BooleanField()),
                ('curado_mejorado', models.BooleanField()),
                ('fecha_alta_medica', models.DateField()),
                ('clasif_resumen', models.TextField()),
                ('clasificacion_manual', models.TextField()),
                ('notas', models.TextField()),
                ('clasificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingest.ClasificacionEpidemiologica')),
                ('creado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventos', to=settings.AUTH_USER_MODEL)),
                ('determinacion_resultado', models.ManyToManyField(to='ingest.DeterminacionResultado')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingest.Paciente')),
                ('signo_sintoma', models.ManyToManyField(to='ingest.Sintoma')),
                ('tipo_evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingest.TipoEvento')),
                ('user_mod_diag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventos_modificados', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='departamento',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingest.Provincia'),
        ),
    ]
