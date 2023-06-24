# Generated by Django 3.2 on 2023-06-17 14:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animaux',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('useridan', models.CharField(max_length=100)),
                ('name', models.CharField(default='', max_length=100)),
                ('bred', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('descri', models.TextField()),
                ('couleur', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('distmarkings', models.CharField(max_length=100)),
                ('daten', models.DateTimeField(default=django.utils.timezone.now)),
                ('addrs', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='animaux_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Animauxfound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userfound', models.CharField(max_length=100)),
                ('bred', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('descri', models.TextField()),
                ('couleur', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('distmarkings', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='animaux_images_found/')),
                ('datefound', models.DateTimeField(default=django.utils.timezone.now)),
                ('addrs', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Animauxlost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userlost', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('bred', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('descri', models.TextField()),
                ('couleur', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('distmarkings', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='animaux_images_lost/')),
                ('datelost', models.DateTimeField(default=django.utils.timezone.now)),
                ('addrs', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=100)),
                ('animid', models.CharField(max_length=100)),
            ],
        ),
    ]
