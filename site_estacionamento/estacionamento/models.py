from django.db import models
from datetime import date
import uuid


def get_meses_opcoes():
    MES_ANO_FORMAT = []
    today = date.today()

    # Dicionário de meses em português
    meses_pt_br = {
        1: 'Janeiro',
        2: 'Fevereiro',
        3: 'Março',
        4: 'Abril',
        5: 'Maio',
        6: 'Junho',
        7: 'Julho',
        8: 'Agosto',
        9: 'Setembro',
        10: 'Outubro',
        11: 'Novembro',
        12: 'Dezembro',
    }

    for i in range(3, -2, -1):
        month = (today.month - i) % 12 or 12
        year = today.year - (1 if today.month <= i else 0)
        opcao = f"{month:02d}/{year}"
        label = f"{meses_pt_br[month]}/{year}"
        MES_ANO_FORMAT.append((opcao, label))
    return MES_ANO_FORMAT


def get_opcoes_from_model(ModelA, campo):
    valores_distintos = ModelA.objects.values_list(campo, flat=True).distinct()
    opcoesA = []
    for valor in valores_distintos:
        if 'Mensal' in valor:
            opcoesA.append((valor, valor))

    return opcoesA

 

class Vaga(models.Model):
    vaga_id = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('Vazio','Vazio'), ('Reservado','Reservado')], default='Vazio')
    nome_cliente = models.CharField(max_length=100, default='Vazio')
    
    def __str__(self) -> str:
        if self.status == 'Vazio':
            return f"{self.vaga_id}"
        
        else:
            return ""

class Plano(models.Model):
    plano_id = models.IntegerField()
    tipo_automovel = models.CharField(max_length=50, default='Automóvel')
    frequencia = models.CharField(max_length=50, default='Frequência')
    preço = models.FloatField(default=0.0)
    name = models.CharField(max_length=50, default='')

    def __str__(self) -> str:
        return f"{self.tipo_automovel} {self.frequencia}"


class SolicitacaoReserva(models.Model):
    nome = models.CharField(max_length=50)
    plano = models.CharField(max_length=50, choices=get_opcoes_from_model(Plano,'name'))
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    modelo_veiculo = models.CharField(max_length=20)
    placa = models.CharField(max_length=20)
    data = models.DateTimeField(auto_now_add=True)

class Pagamento(models.Model):
    STATUS_CHOICES = [
        ('nao_confirmado', 'Não Confirmado'),
        ('Confirmado', 'Confirmado'),
    ]
    mes_ano_referencia = models.CharField(max_length=20, choices=get_meses_opcoes())
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Não Verificado')
    datetime_upload = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50)
    arquivo = models.FileField(upload_to='', null=True, blank=True)

    @property
    def get_filename(self):
        return self.arquivo.name.split('/')[-1]
    
    def save(self, *args, **kwargs):
        random_uuid = str(uuid.uuid4())[:6]
        self.arquivo.name = f'{random_uuid}-{self.arquivo.name}'
        super(Pagamento, self).save(*args, **kwargs)
    

class ReservaRotativa(models.Model):
    vaga_id = models.ForeignKey(Vaga, on_delete=models.PROTECT)
    placa_veiculo = models.CharField(max_length=20)
    tipo_automovel = models.ForeignKey(Plano, on_delete=models.PROTECT)
    horario_entrada = models.DateTimeField()
    horario_saida = models.DateTimeField()
    valor_hora = models.FloatField()

    @property
    def tempo_percorrido(self):
        return self.horario_saida - self.horario_entrada
    
    @property
    def valor_total(self):
        return round((self.tempo_percorrido.total_seconds()/3600)*self.valor_hora,2)


    def save(self, *args, **kwargs):
        outro_objeto = self.vaga_id
        outro_objeto.status = "Reservado"
        outro_objeto.save()

        super(ReservaRotativa, self).save(*args, **kwargs)   

    def delete(self, *args, **kwargs):
        outro_objeto = self.vaga_id
        print(self.vaga_id)
        outro_objeto.status = 'Vazio'
        outro_objeto.save()

        super(ReservaRotativa, self).delete(*args, **kwargs)



class ClienteMensalista(models.Model):
    nome_completo = models.CharField(max_length=200)
    email = models.EmailField()
    modelo_veiculo = models.CharField(max_length=20)
    placa = models.CharField(max_length=20)
    vaga_id = models.ForeignKey(Vaga, on_delete=models.PROTECT, null=True, unique=False)
    tipo_automovel = models.CharField(max_length=20)
    plano_id = models.ForeignKey(Plano, on_delete=models.PROTECT)
    data_entrada = models.DateTimeField(auto_now_add=True)
    telefone = models.CharField(max_length=20)



class DuvidasSugestoesReclamacoes(models.Model):
    nome_completo = models.CharField(max_length=200)
    mensagem = models.TextField()
    data_entrada = models.DateTimeField(auto_now_add=True)


class SolicitacaoCancelamento(models.Model):
    data_saida = models.DateField()
    motivo = models.TextField()
    username = models.CharField(max_length=200)








        
        