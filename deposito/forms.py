from django import forms
from .models import itens


class mercadoForm(forms.ModelForm):
    class Meta:
        model = itens
        fields = ('produto','preco', 'descricao')
        