from rest_framework import serializers

from app.produtor_rural.models import ProdutorRural, CulturaPlantada
from app.produtor_rural.services import validate_cpf, validate_cnpj


class CulturaPlantadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CulturaPlantada
        fields = ['id', 'cultura']


class ProdutorRuralSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    cultura_plantada = CulturaPlantadaSerializer(many=True, read_only=True)
    culturas = serializers.ListField(child=serializers.CharField(), required=False)

    class Meta:
        model = ProdutorRural
        fields = [
            'id',
            'doc_de_registro',
            'nome_produtor',
            'nome_fazenda',
            'cidade',
            'estado',
            'area_total',
            'area_agricultavel',
            'area_vegetacao',
            'culturas',
            'cultura_plantada'

        ]

    def get_culturas(self, obj):
        request = self.context.get('request')
        if request and request.method in ['POST', 'PUT']:
            return obj.culturas

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     request = self.context.get('request')
    #     if request and request.method == 'GET':
    #         data['cultura_plantada'] = CulturaPlantadaSerializer(instance.cultura_plantada).data
    #     return data

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
        produtor_rural = ProdutorRural.objects.create(
            doc_de_registro=validated_data['doc_de_registro'],
            nome_produtor=validated_data['nome_produtor'],
            nome_fazenda=validated_data['nome_fazenda'],
            cidade=validated_data['cidade'],
            estado=validated_data['estado'],
            area_total=validated_data['area_total'],
            area_agricultavel=validated_data['area_agricultavel'],
            area_vegetacao=validated_data['area_vegetacao'],
        )

        for cultura in validated_data.get('culturas', []):
            CulturaPlantada.objects.create(
                produtor=produtor_rural,
                cultura=cultura
            )

        return produtor_rural

    def update(self, instance, validated_data):
        instance.doc_de_registro = validated_data['doc_de_registro']
        instance.nome_produtor = validated_data['nome_produtor']
        instance.cidade = validated_data['cidade']
        instance.estado = validated_data['estado']
        instance.area_total = validated_data['area_total']
        instance.area_agricultavel = validated_data['area_agricultavel']
        instance.area_vegetacao = validated_data['area_vegetacao']
        instance.save()

        # Optei por atualizar dessa forma, devido a praticidade.
        # No frontend no módulo de editar, imaginei que o registro
        # a ser editado estara na tela da seguinte forma:
        # Se houver apenas duas culturas setadas para a fazenda desse produtor,
        # as outras opções de cultura plantada estarão off, caso o usuário, desmarque e/ou
        # marque mais algum opção, o frontend deve atualizar no payload, o campo culturas
        # com apenas as culturas desejadas. Abaixo,faço um filtro, localizo o produtor
        # com todas suas culturas, excluo e gravo o novo list.

        CulturaPlantada.objects.filter(
                produtor=instance
        ).delete()

        for cultura in validated_data.get('culturas', []):
            CulturaPlantada.objects.create(
                    produtor=instance, cultura=cultura
            )

        return instance

