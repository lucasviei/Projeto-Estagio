from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Acervo(models.Model):
    tipoObra = models.CharField(max_length=11)
    tituloObra = models.CharField(max_length=20)
    description = models.TextField()
    begin_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'acervo'

