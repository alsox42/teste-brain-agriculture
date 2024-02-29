from django.contrib import admin

from app.produtor_rural.models import ProdutorRural, CulturaPlantada


# Register your models here.
class ProdutorRuralAdmin(admin.ModelAdmin):
    list_display = [
        'doc_de_registro',
        'nome_produtor',
        'nome_fazenda',
        'cidade',
        'estado',
        'area_total',
        'area_agricultavel',
        'area_vegetacao'
    ]

class CulturaPlantadaAdmin(admin.ModelAdmin):
    list_display = ['produtor', 'cultura']

admin.site.register(ProdutorRural, ProdutorRuralAdmin)
admin.site.register(CulturaPlantada, CulturaPlantadaAdmin)