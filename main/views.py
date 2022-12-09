from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *
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



    
    if busca:
        lista = Publicacao.objects.filter(titulo__icontains= busca)
        context = {'buscas' : lista}
        return render(request, "busca.html", context)
    else:
        return render(request, "index.html")

def detalhe (request,id):
    publicacao = Publicacao.objects.get(id=id)
    context = {'publicacao' : publicacao }
    return render(request,"detalhe.html", context)


def mercado(request):
    lista = Produto.objects.all()
    context ={'produtos' : lista}
    return render(request, 'mercado.html', context)

def detalhe_produto(request, id):
    lista = Produto.objects.get(id=id)
    context = {'produtos' : lista}
    return render(request, "detalhe_produto.html", context)

def produto(request):
    lista = Categoria_Produto.objects.all()
    context = {'categoria_produtos' : lista}
    return render(request, 'produto.html', context)

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
            return HttpResponse('ja existe um usuário com esse username')
# Aqui está sendo feita o cadastrado dos informações.            
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return render(request, 'usuariocadastrado.html')


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
            return render(request, 'index.html')
        else:
            return HttpResponse("Usuário ou senha invalidos")

@login_required(login_url="/login/")
def plataforma(request):
# Aqui será a pagina que somente o usuário autenticado terá acesso, ou seja, a página de cadastro de publicações será aqui.   
    return render(request, 'plataforma.html')

# Todas as páginas que tiver @login_required, so vai ser possivel acessar ela quando o usuário estiver logado.
@login_required(login_url="/login/")
def perfil(request):
    return render(request,'Perfil.html')

def sobrenos(request):
    return render(request, 'sobrenos.html')
def usuario_cadastrado(request):
    return render(request, 'usuariocadastrado.html')