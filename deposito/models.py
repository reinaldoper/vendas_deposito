from django.db import models


class itens(models.Model):
    produto = models.CharField(max_length=100, null=True)
    preco = models.CharField(max_length=10, null=True)
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField(null=True)

    def __str__(self):
        return self.produto


# Create your models here.
