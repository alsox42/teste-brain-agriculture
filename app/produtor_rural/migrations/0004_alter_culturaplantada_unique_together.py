# Generated by Django 5.0.2 on 2024-02-29 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtor_rural', '0003_alter_produtorrural_estado_culturaplantada'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='culturaplantada',
            unique_together={('produtor', 'cultura')},
        ),
    ]
