from django.db import models

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    Telefone = models.IntegerField()
    cep = models.IntegerField()

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
   
class Publicacao(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    corpo_do_texto = models.TextField()
    tempo_da_publicacao = models.DateField()
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True, max_length=250)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Categoria)

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    Telefone = models.IntegerField()
    cep = models.IntegerField()

class Categoria_Produto(models.Model):
    nome = models.CharField(max_length=100)

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=8,decimal_places=2)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria_Produto, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True, max_length=250)