from django.urls import path
from . import views


app_name = "estacionamento"
urlpatterns = [
    # my home page
    path("", views.home, name="home"),
    # exibe vagas e planos
    path("vagaseplanos/", views.vagaseplanos, name="vagaseplanos"),
    # solicitação de reserva
    path("solicitacao/", views.solicitacaoreserva, name="solicitacaoreserva"),
    # solicitação de reserva envio
    path("solicitacao/confirmacao", views.solicitacaoreserva_confirmacao, name="solicitacaoreserva_confirmacao"),
    # página do usuário
    path("userpage/", views.userpage, name="userpage"),
    # Dúvidas/Sugestões/Reclamações
    path("duvidassugestoesreclamacoes/", views.duvidassugestoesreclamacoes, name="duvidassugestoesreclamacoes"),
    # Dúvidas/Sugestões/Reclamações Confirma
    path("duvidassugestoesreclamacoes/confirmacao", views.duvidassugestoesreclamacoes_confirmacao,
        name="duvidassugestoesreclamacoes_confirmacao"
        ),


]