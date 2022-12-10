from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    Telefone = models.IntegerField()
    cep = models.IntegerField()

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
   
class Publicacao(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    corpo_do_texto = RichTextUploadingField()
    tempo_da_publicacao = models.DateField()
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True, max_length=250)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Categoria)

    def __str__(self):
        return self.id
    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    Telefone = models.IntegerField()
    cep = models.IntegerField()

class Categoria_Produto(models.Model):
    nome = models.CharField(max_length=100)

    
    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=8,decimal_places=2)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria_Produto, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True, max_length=250)

    
    def __str__(self):
        return self.nome
