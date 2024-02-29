import random
from django.core.management.base import BaseCommand
from faker import Faker
from app.produtor_rural.models import ProdutorRural, CulturaPlantada
from pycpfcnpj import gen


class Command(BaseCommand):
    help = 'Populate tables with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker('pt_BR')

        for _ in range(1000):
            produtor = ProdutorRural.objects.create(
                doc_de_registro=random.choice([gen.cpf_with_punctuation(), gen.cnpj_with_punctuation()]),
                nome_produtor=fake.name(),
                nome_fazenda=fake.company(),
                cidade=fake.city(),
                estado=fake.state_abbr().lower(),

                area_total=random.uniform(700, 1000),
                area_agricultavel=random.uniform(150, 400),
                area_vegetacao=random.uniform(150, 290)
            )

            for _ in range(random.randint(1, 4)):
                cultura = random.choice(['soja', 'milho', 'algodao', 'cafe', 'cana_de_acucar'])
                try:
                    CulturaPlantada.objects.create(
                        produtor=produtor,
                        cultura=cultura
                    )
                except:
                    pass

        self.stdout.write(self.style.SUCCESS('Dados populados com sucesso.'))
