from django import forms
from .models import Produto

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