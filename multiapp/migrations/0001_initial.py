# Generated by Django 2.0.5 on 2018-12-13 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_comentario', models.DateTimeField(auto_now_add=True)),
                ('comentario', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Comentarios',
                'db_table': 'multimedia"."comentario',
                'ordering': ['-id'],
                'verbose_name': 'Comentario',
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_curso', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Cursos',
                'db_table': 'multimedia"."curso',
                'ordering': ['-id'],
                'verbose_name': 'Curso',
            },
        ),
        migrations.CreateModel(
            name='TipoCurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_curso', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Tipo de Cursos',
                'db_table': 'multimedia"."tipo_curso',
                'ordering': ['-id'],
                'verbose_name': 'Tipo de Curso',
            },
        ),
        migrations.AddField(
            model_name='curso',
            name='tipo_curso',
            field=models.ForeignKey(db_column='tipo_curso_id', on_delete=django.db.models.deletion.PROTECT, to='multiapp.TipoCurso'),
        ),
        migrations.AddField(
            model_name='curso',
            name='usuario',
            field=models.ForeignKey(db_column='usuario_id', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comentario',
            name='curso',
            field=models.ForeignKey(db_column='curso_id', on_delete=django.db.models.deletion.PROTECT, to='multiapp.Curso'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(db_column='usuario_id', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
