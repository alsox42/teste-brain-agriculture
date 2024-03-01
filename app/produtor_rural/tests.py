from django.test import TestCase
from .models import ProdutorRural

class ProdutorRuralTestCase(TestCase):
    def setUp(self):
        # Criando um produtor rural válido para ser usado em vários testes
        self.produtor_rural_valido = ProdutorRural.objects.create(
            doc_de_registro='12345678901',
            nome_produtor='João da Silva',
            nome_fazenda='Fazenda Feliz',
            cidade='Cidade A',
            estado='Estado A',
            area_total=100.50,
            area_agricultavel=50.25,
            area_vegetacao=30.75
        )


    def test_atualizar_produtor_rural_com_valores_validos(self):
        # Testar atualizar um produtor rural com valores válidos
        self.produtor_rural_valido.nome_produtor = 'José Pereira'
        self.produtor_rural_valido.save()
        self.assertEqual(ProdutorRural.objects.get(nome_produtor='José Pereira').nome_produtor, 'José Pereira')

    def test_excluir_produtor_rural(self):
        # Testar excluir um produtor rural
        produtor_rural_para_excluir = ProdutorRural.objects.create(
            doc_de_registro='11111111111',
            nome_produtor='Excluir Teste',
            nome_fazenda='Fazenda Teste',
            cidade='Cidade C',
            estado='Estado C',
            area_total=50.50,
            area_agricultavel=25.25,
            area_vegetacao=15.75
        )
        produtor_rural_para_excluir.delete()
        self.assertIsNone(ProdutorRural.objects.filter(nome_produtor='Excluir Teste').first())

    def test_consultar_produtor_rural_por_cpf_cnpj(self):
        # Testar consultar um produtor rural por CPF/CNPJ
        self.assertEqual(ProdutorRural.objects.get(doc_de_registro='12345678901').nome_produtor, 'João da Silva')

    def test_consultar_todos_os_produtores_rurais_cadastrados(self):
        # Testar consultar todos os produtores rurais cadastrados
        self.assertEqual(ProdutorRural.objects.count(), 1)

    def test_consultar_produtores_rurais_por_cidade(self):
        # Testar consultar produtores rurais por cidade
        produtores_por_cidade = ProdutorRural.objects.filter(cidade='Cidade A')
        self.assertEqual(produtores_por_cidade.count(), 1)

    def test_consultar_produtores_rurais_por_estado(self):
        # Testar consultar produtores rurais por estado
        produtores_por_estado = ProdutorRural.objects.filter(estado='Estado A')
        self.assertEqual(produtores_por_estado.count(), 1)
