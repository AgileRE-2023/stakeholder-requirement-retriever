# Generated by Django 4.2.5 on 2023-11-20 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('getByQuery', '0002_scraping_id_prodi'),
        ('getByHistory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='id_prodi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='histories', to='getByQuery.prodi'),
        ),
    ]