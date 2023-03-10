# Generated by Django 4.1.2 on 2023-02-14 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('departamento_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_documento', models.TextField()),
                ('nombre1', models.TextField()),
                ('nombre2', models.TextField(blank=True)),
                ('apellido1', models.TextField()),
                ('apellido2', models.TextField()),
                ('departamento_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.departamento')),
                ('genero_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.genero')),
                ('municipio_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.municipio')),
            ],
        ),
        migrations.CreateModel(
            name='TipoDeDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Tasks',
        ),
        migrations.AddField(
            model_name='paciente',
            name='tipo_documento_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.tipodedocumento'),
        ),
    ]
