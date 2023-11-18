# Generated by Django 4.2.5 on 2023-11-09 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('getByQuery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id_history', models.AutoField(primary_key=True, serialize=False)),
                ('date_generated', models.DateTimeField(auto_now_add=True)),
                ('exp_date', models.DateTimeField(auto_now_add=True)),
                ('requirements', models.CharField(max_length=200)),
                ('id_prodi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='getByQuery.prodi')),
            ],
        ),
    ]
