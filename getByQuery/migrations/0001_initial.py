# Generated by Django 4.2.5 on 2023-11-09 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prodi',
            fields=[
                ('id_prodi', models.AutoField(primary_key=True, serialize=False)),
                ('nama_prodi', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scraping',
            fields=[
                ('id_scrap', models.AutoField(primary_key=True, serialize=False)),
                ('tgl_scrap', models.DateTimeField(auto_now_add=True)),
                ('teks', models.TextField(max_length=599999)),
            ],
        ),
    ]