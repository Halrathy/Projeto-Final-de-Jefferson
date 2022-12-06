from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    lista = Publicacao.objects.all()
    context={'publicacoes' : lista}
    return render(request,"index.html", context)
