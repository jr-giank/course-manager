# Generated by Django 4.0.1 on 2022-01-12 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creditos', models.IntegerField()),
                ('nombre_asignatura', models.TextField(max_length=45)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
