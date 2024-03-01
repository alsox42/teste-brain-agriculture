from rest_framework import viewsets
from app.produtor_rural.models import ProdutorRural
from api.api_produtor_rural.serializers import ProdutorRuralSerializer


class ProdutorRuralViewSet(viewsets.ModelViewSet):
    queryset = ProdutorRural.objects.all()
    serializer_class = ProdutorRuralSerializer
