from django.db import models

from app.produtor_rural.choices import ESTADOS_CHOICES
"""
Importante: Tendo a oportunidade de conversar com o arquiteto de software
ou com o Stakeholder do projeto, eu proporia que houvesse um cadastro para produtor rural. E
um segundo cadastro para a(s) fazenda(s). Dessa forma não haveria repetição de dados, pois
da forma como a tabela ProdutorRural foi implementada, os produtores rurais que tiverem 
mais de uma fazenda, teram seu nome repetido em cada cadastro. 
"""

class ProdutorRural(models.Model):
    doc_de_registro = models.CharField('CPF ou CNPJ', max_length=100, unique=True)
    nome_produtor = models.CharField('Nome do produtor', max_length=100)
    nome_fazenda = models.CharField('Nome da Fazenda', max_length=100)
    cidade = models.CharField('Cidade', max_length=50)
    estado = models.CharField('Estado', max_length=50, choices=ESTADOS_CHOICES)
    area_total = models.DecimalField('Área total em hectares da fazenda',decimal_places=2, max_digits=6)
    area_agricultavel = models.DecimalField('Área agricultável em hectares',decimal_places=2, max_digits=6)
    area_vegetacao = models.DecimalField('Área de vegetação em hectares', decimal_places=2, max_digits=6)

    def __str__(self):
        return self.nome_produtor

    class Meta:
        db_table = 'produtor_rural'


