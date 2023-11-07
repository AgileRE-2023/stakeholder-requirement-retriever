from django.db import models
from getByQuery.models import Prodi

# Create your models here.
class History(models.Model):
    date_generated = models.DateTimeField(auto_now_add=True)
    exp_date = models.DateTimeField(auto_now_add=True)
    requirements = models.CharField(max_length=200)
    id_history = models.ForeignKey(Prodi, on_delete=models.CASCADE)