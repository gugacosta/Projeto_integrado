# Generated by Django 4.2.2 on 2023-07-29 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamento', '0006_duvidassugestoesreclamacoes_data_entrada_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitacaoCancelamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_saida', models.DateField()),
                ('motivo', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='mes_ano_referencia',
            field=models.CharField(choices=[('04/2023', 'Abril/2023'), ('05/2023', 'Maio/2023'), ('06/2023', 'Junho/2023'), ('07/2023', 'Julho/2023'), ('08/2023', 'Agosto/2023')], max_length=20),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='status',
            field=models.CharField(choices=[('anexado_nao_verificado', 'Não Confirmado'), ('anexado_verificado', 'Confirmado')], default='Não Verificado', max_length=30),
        ),
    ]
