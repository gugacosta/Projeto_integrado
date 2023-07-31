from django.contrib import admin
from .models import Vaga,Plano,SolicitacaoReserva, Pagamento, ReservaRotativa,\
ClienteMensalista, DuvidasSugestoesReclamacoes, SolicitacaoCancelamento


@admin.register(ReservaRotativa)
class ReservaRotativaAdmin(admin.ModelAdmin):
    list_display = ('placa_veiculo', 'tipo_automovel', 'horario_entrada', 'horario_saida',
                    'valor_hora', 'tempo_percorrido','valor_total')
    
    search_fields = ('placa_veiculo',) 
    list_editable = ('horario_saida',)
    search_help_text = "PESQUISE A PLACA"

@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ('vaga_id', 'status', 'nome_cliente')

@admin.register(Plano)
class PlanoAdmin(admin.ModelAdmin):
    list_display = ('plano_id', 'tipo_automovel', 'frequencia', 'preço')

@admin.register(SolicitacaoReserva)
class SolicitacaoReservaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome','plano','telefone','data')

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('mes_ano_referencia', 'status', 'datetime_upload', 'username', 'arquivo')

@admin.register(ClienteMensalista)
class ClienteMensalistaAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'placa', 'vaga_id', 'plano_id', 'telefone')

@admin.register(DuvidasSugestoesReclamacoes)
class DuvidasSugestoesReclamacoesAdmin(admin.ModelAdmin):
    list_display = ('nome_completo','mensagem','data_entrada')

@admin.register(SolicitacaoCancelamento)
class SolicitacaoCancelamentoAdmin(admin.ModelAdmin):
    list_display = ('username','data_saida','motivo')


admin.site.site_header = "Administração do Estacionamento"
