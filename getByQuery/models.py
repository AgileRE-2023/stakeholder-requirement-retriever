from django.db import models

class Prodi(models.Model):
    id_prodi = models.AutoField(primary_key=True)
    nama_prodi = models.CharField(max_length=50,unique=True,null=False)

class Scraping(models.Model):
    id_scrap = models.AutoField(primary_key=True)
    tgl_scrap = models.DateTimeField(auto_now_add=True)
    teks = models.TextField(max_length=599999,null=False)
