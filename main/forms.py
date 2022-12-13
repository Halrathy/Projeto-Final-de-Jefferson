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
            'categoria': forms.Select(attrs={'class':'form-select'}),
        }