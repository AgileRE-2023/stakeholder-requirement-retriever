# Generated by Django 4.2.5 on 2023-11-20 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('getByQuery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scraping',
            name='id_prodi',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='scrapings', to='getByQuery.prodi'),
            preserve_default=False,
        ),
    ]
