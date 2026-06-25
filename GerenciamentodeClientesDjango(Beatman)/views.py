from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Cliente

# 1. Página Inicial: Lista os clientes
def paginaInicial(request):
    listaDeClientes = Cliente.objects.all()
    context = {"listaDeClientes": listaDeClientes}
    return render(request, "base.html", context)

# 2. NOVO: Recebe o envio dos dados e cadastra um novo cliente no banco
def cadastrarcliente(request):
    if request.method == "POST":
        novo_cliente = Cliente() # Cria um cliente em branco
        novo_cliente.nome = request.POST["nome"]   # Preenche o nome
        novo_cliente.email = request.POST["email"] # Preenche o e-mail
        novo_cliente.save() # Salva no banco de dados
        return redirect("/") # Atualiza a página inicial
    else:
        return HttpResponse("Nenhum dado foi enviado")


def cadastrarcliente(request):
    if request.method == "POST":
        novo_cliente = Cliente()  # 1. Cria um registro vazio na memória
        novo_cliente.nome = request.POST["nome"]  # 2. Pega o 'nome' do HTML e bota nele
        novo_cliente.email = request.POST["email"]  # 3. Pega o 'email' do HTML e bota nele
        novo_cliente.save()  # 4. Grava de verdade no Banco de Dados

        return redirect("/")  # 5. Recarrega a página para o cliente aparecer na lista

# 3. Nova Página: Abre o formulário de edição
def editar(request, cliid):
    cliente = Cliente.objects.get(pk=cliid)
    context = {"cliente": cliente}
    return render(request, "editarcliente.html", context)

# 4. Processa a edição do formulário
def editarcliente(request):
    if request.method == "POST":
        cliente = Cliente.objects.get(pk=request.POST["id"])
        cliente.nome = request.POST["nome"]
        cliente.email = request.POST["email"]
        cliente.save()
        return redirect("/")
    else:
        return HttpResponse("Nenhum dado foi passado na requisição")

# 5. Remove o cliente
def remover(request, cliid):
    clienteDeletar = Cliente.objects.get(pk=cliid)
    clienteDeletar.delete()
    return redirect("/")