from rest_framework import serializers

from app.produtor_rural.models import ProdutorRural, CulturaPlantada
from app.produtor_rural.services import validate_cpf, validate_cnpj


class CulturaPlantadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CulturaPlantada
        fields = '__all__'


class ProdutorRuralSerializer(serializers.ModelSerializer):
    cultura_plantada = CulturaPlantadaSerializer()

    class Meta:
        model = ProdutorRural
        fields = [
            'doc_de_registro',
            'nome_produtor',
            'nome_fazenda',
            'cidade',
            'estado',
            'area_total',
            'area_agricultavel',
            'area_vegetacao',
            'cultura_plantada'
        ]

    def validate_doc_de_registro(self, value):
        if len(value) == 11:
            if not validate_cpf(value):
                raise serializers.ValidationError("CPF inválido")
        elif len(value) == 14:
            if not validate_cnpj(value):
                raise serializers.ValidationError("CNPJ inválido")
        else:
            raise serializers.ValidationError("Documento de registro deve ter 11 ou 14 caracteres")

        return value

    def validate(self, data):
        area_agricultavel = data.get('area_agricultavel', 0)
        area_vegetacao = data.get('area_vegetacao', 0)
        area_total = data.get('area_total', 0)

        if area_agricultavel + area_vegetacao > area_total:
            raise serializers.ValidationError(
                "A soma da área agricultável e da área de vegetação não pode ser maior que a área total.")

        return data

    def create(self, validated_data):
        pass




