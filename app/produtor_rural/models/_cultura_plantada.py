from django.db import models

from app.produtor_rural.choices import CULTURAS_CHOICES
from app.produtor_rural.models import ProdutorRural

class CulturaPlantada(models.Model):
    produtor = models.ForeignKey(ProdutorRural, on_delete=models.CASCADE, related_name='cultura_plantada')
    cultura = models.CharField('Cultura plantada', max_length=50, choices=CULTURAS_CHOICES)

    def __str__(self):
        return f'{self.produtor} - {self.cultura}'

    class Meta:
        db_table = 'cultura_plantada'
        verbose_name = 'Culturas Plantada'
        unique_together = ('produtor', 'cultura')

