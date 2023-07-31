from django.shortcuts import render, redirect
from .models import Vaga, Plano, Pagamento

from .forms import SolicitacaoReserva, PagamentosForm,\
    DuvidasSugestoesReclamacoesForm, SolicitacaoCancelamentoForm
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, "estacionamento/home.html")



def vagaseplanos(request):
    vagas_info = Vaga.objects.all()
    planos_info = Plano.objects.all()
    return render(request, "estacionamento/vagaseplanos.html",
                {"vagas_info": vagas_info, "planos_info": planos_info})


def solicitacaoreserva(request):
    if request.method == 'POST':
        form = SolicitacaoReserva(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estacionamento:solicitacaoreserva_confirmacao')
            
    else:
        form = SolicitacaoReserva()
    
    return render(request, "estacionamento/solicitacaoreserva.html", context={"form":form})



def solicitacaoreserva_confirmacao(request):
    return render(request, "estacionamento/solicitacaoreserva_confirmacao.html")



@login_required()
def userpage(request):
    # Recupera o cliente logado, por exemplo, através do objeto 'request.user'
    username_logado = request.user.username
    if 'admin' in username_logado:
        return redirect('/admin/')

    # Recupera os comprovantes do cliente logado
    comprovantes = Pagamento.objects.filter(username=username_logado)

    # Lida com o envio do formulário de upload
    if request.method == 'POST':       
        a=list(request.FILES.keys())
        print(a)
        if a != []:
            form = PagamentosForm(request.POST, request.FILES)
            if form.is_valid():
                adduser = form.save(commit=False)
                adduser.username = request.user.username
                adduser.save()            
                return redirect('estacionamento:userpage') 
            else:
                cancelform = SolicitacaoCancelamentoForm()
            
        else:
            cancelform = SolicitacaoCancelamentoForm(request.POST, request.FILES)
            if cancelform.is_valid():               
                adduser = cancelform.save(commit=False)
                adduser.username = request.user.username
                adduser.save()  
                return redirect('estacionamento:userpage')
            else:
                form = PagamentosForm()
            
    else:
        form = PagamentosForm()
        cancelform = SolicitacaoCancelamentoForm()
    
    return render(request, "estacionamento/userpage.html",
                {'comprovantes': comprovantes, 'form': form, 'cancelform':cancelform})


def duvidassugestoesreclamacoes(request):
    if request.method == 'POST':
        form = DuvidasSugestoesReclamacoesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estacionamento:duvidassugestoesreclamacoes_confirmacao')
            
    else:
        form = DuvidasSugestoesReclamacoesForm()
    
    return render(request, "estacionamento/duvidassugestoesreclamacoes.html", context={"form":form})

def duvidassugestoesreclamacoes_confirmacao(request):
    return render(request, "estacionamento/duvidassugestoesreclamacoes_confirmacao.html")


