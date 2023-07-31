from django import forms
from .models import SolicitacaoReserva, Pagamento,\
    DuvidasSugestoesReclamacoes, SolicitacaoCancelamento

class SolicitacaoReserva(forms.ModelForm):
    class Meta:
        model = SolicitacaoReserva
        fields = ['nome', 'plano', 'telefone','email','modelo_veiculo','placa']


class PagamentosForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ('mes_ano_referencia','arquivo')


class DuvidasSugestoesReclamacoesForm(forms.ModelForm):
    class Meta:
        model = DuvidasSugestoesReclamacoes
        fields = ['nome_completo', 'mensagem']


class SolicitacaoCancelamentoForm(forms.ModelForm):
    data_saida = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = SolicitacaoCancelamento
        fields = ['data_saida', 'motivo']
