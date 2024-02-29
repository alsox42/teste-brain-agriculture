from django.db import models
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from app.produtor_rural.models import ProdutorRural, CulturaPlantada


class DashboardViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def fazendas_totais(self, request):
        total_fazendas = ProdutorRural.objects.count()
        soma_area_total = ProdutorRural.objects.aggregate(total_area=models.Sum('area_total'))['total_area'] or 0

        data = {
            "total de fazendas em quantidade": total_fazendas,
            "total de fazendas em hectares": soma_area_total
        }
        return Response(data)

    @action(detail=False, methods=['get'])
    def chart_fazendas_por_estado(self, request):
        fazendas_por_estado = ProdutorRural.objects.values('estado').annotate(total=models.Count('estado'))

        data = []
        for fazenda in fazendas_por_estado:
            data.append({
                "estado": fazenda['estado'],
                "total": fazenda['total']
            })

        return Response(data)

    @action(detail=False, methods=['get'])
    def chart_fazendas_por_cultura(self, request):
        fazendas_por_cultura = CulturaPlantada.objects.values('cultura').annotate(total=models.Count('cultura'))

        data = []
        for fazenda in fazendas_por_cultura:
            data.append({
                "cultura": fazenda['cultura'],
                "total": fazenda['total']
            })

        return Response(data)

    @action(detail=False, methods=['get'])
    def chart_area_agricultavel_e_vegetacao(self, request):
        total_agricultavel = ProdutorRural.objects.aggregate(total_agricultavel=models.Sum('area_agricultavel'))[
                                 'total_agricultavel'] or 0
        total_vegetacao = ProdutorRural.objects.aggregate(total_vegetacao=models.Sum('area_vegetacao'))[
                              'total_vegetacao'] or 0

        data = {
            "agricultavel": total_agricultavel,
            "vegetação": total_vegetacao
        }
        return Response(data)