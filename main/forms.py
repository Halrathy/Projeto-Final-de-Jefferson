from django import forms
from .models import *

class ProdutosForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','categoria','descricao','imagem','valor']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder':'Nome do Produto', 'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-select'}),
            'descricao': forms.Textarea(attrs={'placeholder':'Descrição', 'class': 'form-control','style':'height:100px'}),
            'valor': forms.TextInput(attrs={'placeholder':'Valor', 'class': 'form-control'}),
            'imagem': forms.FileInput(attrs={'class':'form-control', 'id':'formFileSm'}),
        }

class PublicacaoForm(forms.ModelForm):
    class Meta:
        model = Publicacao
        fields = ['titulo','descricao','corpo_do_texto','tempo_da_publicacao', 'imagem', 'autor','categoria']
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder':'Adicione um título', 'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'placeholder':'Descrição da publicação', 'class': 'form-control','style':'height:100px'}),
            'corpo_do_texto': forms.Textarea(attrs={'placeholder':'', 'class': 'form-control','style':'height:100px'}),
            'tempo_da_publicacao': forms.TextInput(attrs={'placeholder':'Data da Publicação', 'class': 'form-control'}),
            'autor': forms.Textarea(attrs={'placeholder':'Autor', 'class': 'form-control','style':'height:100px'}),
            'imagem': forms.FileInput(attrs={'class':'form-control', 'id':'formFileSm'}),
            'categoria': forms.Select(attrs={'class':'form-select'}),
            
        }