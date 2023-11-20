from django.db import models

class Prodi(models.Model):
    id_prodi = models.AutoField(primary_key=True)
    nama_prodi = models.CharField(max_length=50,unique=True,null=False)
    subject = models.CharField(max_length=1, null=False, default=0) #0 for Arts & Humanities; 1 for Engineering and Technology; 2 for Life Sciences and Medicine; 3 for Natural Sciences; 4 for Social Sciences and Management

class Scraping(models.Model):
    id_scrap = models.AutoField(primary_key=True)
    id_prodi = models.ForeignKey(Prodi, on_delete=models.CASCADE, related_name='scrapings', default=1)
    tgl_scrap = models.DateTimeField(auto_now_add=True)
    teks = models.TextField(max_length=599999,null=False)
