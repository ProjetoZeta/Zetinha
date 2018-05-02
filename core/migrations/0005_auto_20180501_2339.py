# Generated by Django 2.0.2 on 2018-05-01 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180501_2310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimoequipamento',
            name='no_equipamento',
        ),
        migrations.AlterField(
            model_name='emprestimoequipamento',
            name='nu_patrimonio',
            field=models.CharField(max_length=64, verbose_name='Número de Patrimônio'),
        ),
        migrations.AlterField(
            model_name='emprestimoequipamento',
            name='tipo_equipamento',
            field=models.CharField(choices=[('1', 'Computador'), ('2', 'Projetor'), ('2', 'Microcontrolador'), ('4', 'Equipamento de Rede')], default='1', max_length=1, verbose_name='Tipo de Equipamento'),
        ),
    ]
