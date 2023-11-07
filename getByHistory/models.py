from django.db import models
from getByQuery.models import Prodi

# Create your models here.
class History(models.Model):
    id_history = models.AutoField(primary_key=True)
    id_prodi = models.ForeignKey(Prodi, on_delete=models.CASCADE)
    date_generated = models.DateTimeField(auto_now_add=True)
    exp_date = models.DateTimeField(auto_now_add=True)
    requirements = models.CharField(max_length=200)