from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import cookie
from django.contrib import messages
from .models import *
from .forms import ProdutosForm, PublicacaoForm
# Create your views here.

def index(request):
    lista = Publicacao.objects.all()
    lista_produto = Produto.objects.all()

    busca = request.GET.get('search')
    if busca:
        lista = Publicacao.objects.filter(titulo__icontains = busca)
        lista_produto = Produto.objects.filter(nome__icontains = busca)
        context = {'buscas' : lista, 'busca_produto' : lista_produto}
        return render(request, "busca.html", context)
    else:
        context={'publicacoes' : lista, 'produtos' : lista_produto}
        return render(request,"index.html", context)

def detalhe (request,id):
    busca = request.GET.get('search')
    if busca:
        lista = Publicacao.objects.filter(titulo__icontains = busca)
        lista_produto = Produto.objects.filter(nome__icontains = busca)
        context = {'buscas' : lista, 'busca_produto' : lista_produto}
        return render(request, "busca.html", context)
    else:
        publicacao = Publicacao.objects.get(id=id)
        context = {'publicacao' : publicacao }
        return render(request,"detalhe.html", context)

def noticias (request):
    busca = request.GET.get('search')
    if busca:
        lista = Publicacao.objects.filter(titulo__icontains = busca)
        lista_produto = Produto.objects.filter(nome__icontains = busca)
        context = {'buscas' : lista, 'busca_produto' : lista_produto}
        return render(request, "busca.html", context)
    else:
        lista = Publicacao.objects.all()
        context ={'publicacoes' : lista}
        return render(request, 'noticia.html', context)

def mercado(request):
    busca = request.GET.get('search')
    if busca:
        lista = Publicacao.objects.filter(titulo__icontains = busca)
        lista_produto = Produto.objects.filter(nome__icontains = busca)
        context = {'buscas' : lista, 'busca_produto' : lista_produto}
        return render(request, "busca.html", context)
    else:
        lista = Produto.objects.all()
        context ={'produtos' : lista}
        return render(request, 'mercado.html', context)

def detalhe_produto(request, id):
    busca = request.GET.get('search')
    if busca:
        lista = Publicacao.objects.filter(titulo__icontains = busca)
        lista_produto = Produto.objects.filter(nome__icontains = busca)
        context = {'buscas' : lista, 'busca_produto' : lista_produto}
        return render(request, "busca.html", context)
    else:
        lista = Produto.objects.get(id=id)
        context = {'produto' : lista}
        return render(request, "detalhe_produto.html", context)


@login_required
def produto(request):
    form = ProdutosForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            task_list = form.save(commit=False)
            task_list.user = request.user
            task_list.save()
            form = ProdutosForm
            return render(request, 'produto.html', {'form': form})
    return render(request, 'produto.html', {'form': form})

def cadastro(request):
# Aqui o request está pegando os dados enviados pelo metodo POST.
    if request.method == "GET":
        return render(request,'cadastro.html')
    else:
# Aqui a informação do forms(POST) estão sendo atribuidas a variaveis.
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

# Aqui está sendo feita uma filtragem com o nome do usuário, para saber se ja tem uma conta cadastrada com esse nome.        
        user = User.objects.filter(username=username).first()

        if user:
            messages.info(request, 'Já existe um usuário com esse nome')
            return redirect('cadastro')
# Aqui está sendo feita o cadastrado dos informações.            
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return redirect('index')


def login(request):
# Aqui o request está pegando os dados enviados pelo metodo POST.
    if request.method == "GET":
        return render(request, 'login.html')
    else:
# Aqui a informação do forms(POST) estão sendo atribuidas a variaveis.
        username = request.POST.get('username')
        senha = request.POST.get('senha')
# Aqui está sendo guardado o usuário autenticado.
        user = authenticate(username=username, password=senha)

        if user:
# Aqui está sendo feita a verificação, para saber se o usuário estava cadastrado no banco.
            login_django(request, user)
            return redirect('index')
        else:
            messages.warning(request, 'Usuário ou Senha inválidos')
            return redirect('login')

def resetarsenha(request):
    if request.method == "GET":
        return render(request, 'resetarsenha.html')
    else:
        username = request.POST.get('username')
        novasenha = request.POST.get('novasenha')
        try:
            user = User.objects.get(username=username)
            user.set_password(request.POST['novasenha'])
            user.save()
            messages.success(request, 'Senha modificada com sucesso')
            return redirect('login')
        except User.DoesNotExist:
            return render(request,'resetarsenha.html')

@login_required(login_url="/login/")
def plataforma(request):
    form = PublicacaoForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            task_list = form.save(commit=False)
            task_list.user = request.user
            task_list.save()
            form = PublicacaoForm
            return render(request, 'plataforma.html', {'form_p': form})
            
    return render(request, 'plataforma.html',  {'form_p': form})

# Todas as páginas que tiver @login_requireds, so vai ser possivel acessar ela quando o usuário estiver logado.

@login_required(login_url="/login/")
def perfil(request):
    lista = Publicacao.objects.filter(user=request.user)
    lista_produto = Produto.objects.filter(user=request.user)
    context = {'publicacoes' : lista, 'produtos' : lista_produto}
    return render(request,'Perfil.html', context)

@login_required(login_url="/login/")
def loja(request,id):
    try:
        produto = Produto.objects.get(pk = id)
        pedido_aux = Pedido.objects.get(nome_produto= produto.nome, id_cliente = request.user.id)

        if pedido_aux:
            messages.error(request,'Esse produto ja está no seu carrinho')
            return redirect('detalhe_produto', produto.pk)

    except Pedido.DoesNotExist:
        produto = Produto.objects.get(pk = id)
        print(produto)
        new_pedido = Pedido( id_cliente = request.user.id, nome_produto = produto.nome, valor_produto = produto.valor, quantidade = 5)
        print(new_pedido)
        new_pedido.save()
        print(produto)
        return redirect('detalhe_produto',produto.pk)

@login_required
def Carrinho(request):
    pedidos = Pedido.objects.filter(id_cliente = request.user.id )
    return render(request, 'carrinho.html', {'pedidos':pedidos})

@login_required(login_url="/login/")
def delete(request, id):
    pedido = get_object_or_404(Pedido, pk = id)
    pedido.delete()
    return redirect('carrinho')


def sobrenos(request):
    return render(request, 'sobrenos.html')
def usuario_cadastrado(request):
    return render(request, 'usuariocadastrado.html') 