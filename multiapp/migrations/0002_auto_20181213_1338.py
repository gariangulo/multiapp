# Generated by Django 2.0.5 on 2018-12-13 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='comentario',
            field=models.TextField(max_length=500),
        ),
    ]
