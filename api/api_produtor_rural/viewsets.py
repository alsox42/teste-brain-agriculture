from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from app.produtor_rural.models._produtor_rural import ProdutorRural
from api.api_produtor_rural.serializers import ProdutorRuralSerializer


class ProdutorRuralViewSet(viewsets.ModelViewSet):
    queryset = ProdutorRural.objects.all()
    serializer_class = ProdutorRuralSerializer
    permission_classes = [IsAuthenticated,]



