# Generated by Django 2.1 on 2018-10-06 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alerta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_reporte', models.DateField(blank=True, null=True)),
                ('coordenadas_alerta', models.CharField(max_length=200)),
                ('descripcion_alerta', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='cai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cai', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('coordenadas_cai', models.CharField(max_length=200)),
                ('descripcion_cai', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=200)),
                ('cedula', models.CharField(max_length=200)),
                ('nickname', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='alerta',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplication.usuario'),
        ),
    ]