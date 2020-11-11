# Generated by Django 3.1.2 on 2020-10-15 16:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20201014_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Almacenamieto',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Codigo unido del producto', primary_key=True, serialize=False)),
                ('marca', models.CharField(choices=[('se', 'Seleccione'), ('we', 'Western Digital'), ('sa', 'Samsung'), ('Ki', 'Kingston')], default='se', help_text='Marca del producto', max_length=2)),
                ('modelo', models.CharField(max_length=50)),
                ('capacidad', models.CharField(max_length=50)),
                ('formato', models.CharField(choices=[('s', 'Seleccione'), ('h', 'HDD'), ('m', 'M.2'), ('2', '2.5"')], default='s', help_text='Formato del producto', max_length=1)),
                ('bus', models.CharField(max_length=50)),
                ('precio', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FuentePoder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Codigo unico del producto', primary_key=True, serialize=False)),
                ('marca', models.CharField(choices=[('s', 'Seleccione'), ('a', 'ASUS'), ('e', 'EVGA'), ('g', 'GAMEMAX')], default='s', help_text='Marca del producto', max_length=1)),
                ('potencia', models.CharField(max_length=50)),
                ('certificacion', models.CharField(choices=[('sele', 'Seleccione'), ('gold', '80PLUS Gold'), ('Bron', '80PLUS Bronze'), ('sinc', 'Sin Certificacion')], default='sele', help_text='Certificacion del producto', max_length=4)),
                ('modular', models.CharField(choices=[('se', 'Seleccione'), ('si', 'SI'), ('no', 'NO')], default='se', max_length=2)),
                ('precio', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Gpu',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Codigo unico del producto', primary_key=True, serialize=False)),
                ('marca', models.CharField(choices=[('s', 'Seleccione'), ('a', 'AMD radeon'), ('m', 'MSI'), ('s', 'ASUS'), ('n', 'Nvidia')], default='s', help_text='Mara del producto', max_length=1)),
                ('modelo', models.CharField(max_length=100)),
                ('plataforma', models.CharField(choices=[('s', 'Seleccione'), ('a', 'AMD'), ('n', 'Nvidia')], default='s', help_text='Plataforma del producto', max_length=1)),
                ('memoria', models.CharField(max_length=100)),
                ('frecuencia', models.CharField(max_length=100)),
                ('precio', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Ram',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Codigo unico del producto', primary_key=True, serialize=False)),
                ('marca', models.CharField(choices=[('s', 'Seleccione'), ('a', 'A-DATA'), ('c', 'Crucial'), ('g', 'G.Skill'), ('h', 'HyperX')], default='s', help_text='Marca del producto', max_length=1)),
                ('capacidad', models.CharField(max_length=100)),
                ('tipo', models.CharField(choices=[('se', 'Seleccione'), ('d3', 'DDR3'), ('d4', 'DDR4')], default='se', help_text='Tipo de ram', max_length=2)),
                ('frecuencia', models.CharField(max_length=50)),
                ('formato', models.CharField(choices=[('s', 'Seleccione'), ('d', 'DIMM'), ('s', 'SO-DIMM')], default='s', help_text='Formato de la Ram', max_length=1)),
                ('precio', models.IntegerField(default=0)),
            ],
        ),
    ]
