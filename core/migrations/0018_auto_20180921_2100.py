# Generated by Django 2.0.2 on 2018-09-21 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20180921_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projetointeressados',
            name='entidade_proponente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proponente', to='core.Entidade'),
        ),
    ]