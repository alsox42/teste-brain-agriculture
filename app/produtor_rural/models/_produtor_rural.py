from django.db import models

from app.produtor_rural.choices import ESTADOS_CHOICES


class ProdutorRural(models.Model):
    doc_de_registro = models.CharField('CPF ou CNPJ', max_length=100, unique=True)
    nome_produtor = models.CharField('Nome do produtor', max_length=100)
    nome_fazenda = models.CharField('Nome da Fazenda', max_length=100)
    cidade = models.CharField('Cidade', max_length=50)
    estado = models.CharField('Estado', max_length=50, choices=ESTADOS_CHOICES)
    area_total = models.FloatField('Área total em hectares da fazenda')
    area_agricultavel = models.FloatField('Área agricultável em hectares')
    area_vegetacao = models.FloatField('Área de vegetação em hectares')

    def __str__(self):
        return self.nome_produtor

    class Meta:
        db_table = 'produtor_rural'


