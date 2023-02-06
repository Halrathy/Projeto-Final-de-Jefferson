from django import forms
import django.forms.utils
import django.forms.widgets
from ckeditor.fields import RichTextFormField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingFormField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
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

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['nome_Completo','rua','bairro','numero', 'cidade', 'complemento', 'descricao']
        widgets = {
            'nome_Completo': forms.TextInput(attrs={'placeholder':'Nome Completo', 'class': 'form-control'}),
            'rua': forms.TextInput(attrs={'placeholder':'Rua', 'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'placeholder':'Bairro', 'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'placeholder':'Número', 'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'placeholder':'Cidade', 'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'placeholder':'complemento', 'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'placeholder':'Descrição', 'class': 'form-control','style':'height:100px'}),
        }

class DateInput(forms.DateInput):
    input_type = 'date'

class PublicacaoForm(forms.ModelForm):
    class Meta:
        model = Publicacao
        fields = ['titulo','descricao','corpo_do_texto','tempo_da_publicacao', 'imagem', 'autor','categoria']
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder':'Adicione um título', 'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'placeholder':'Descrição da publicação', 'class': 'form-control','style':'height:100px'}),
            'corpo_do_texto': forms.Textarea(),
            'tempo_da_publicacao': forms.SelectDateWidget(attrs={'class':'form-control','style':'width:100px;display:inline'}),
            'autor': forms.Select(attrs={'class':'form-select'}),
            'imagem': forms.FileInput(attrs={'class':'form-control', 'id':'formFileSm'}),
            'categoria': forms.SelectMultiple(attrs={'class':'form-select'}),
        }