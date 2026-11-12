from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class  Usuario(AbstractUser):
          TIPO_USUARIO_CHOICES = [
                    ('CLIENTE', 'Cliente'),
                    ('ADMIN', 'Admin'),
          ]
          tipo_usuario = models.CharField('Tipo de Usuário', max_length=7, choices=TIPO_USUARIO_CHOICES, blank=False, null=False)
          
          def __str__(self):
                  return self.username
class Cliente(models.Model):
        SEXO_CHOICES = [
                ('M', 'Masculino'),
                ('F', 'Feminino'),
        ]
        usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='Cliente')
        cpf = models.CharField('CPF', max_length=11, primary_key=True)
        nome = models.CharField('Nome', max_length=60, null=False, blank=False)
        telefone = models.CharField('Telefone', max_length=13, null=False, blank=False, unique=True)
        email = models.EmailField('E-mail', null=False, blank=False, unique=True)
        logradouro = models.CharField('Logardouro', max_length=60, null=False, blank=False)
        numero = models.IntegerField('Número', null=False, blank=False)
        sexo = models.CharField('Sexo', max_length=1, choices=SEXO_CHOICES, blank=False)
        
        def __str__(self):
                return self.nome

class Venda (models.Model):
        FORMA_PAG_CHOICES = [
                        ('C', 'Cartão de Crédito'),
                        ('P', 'PIX'),
                        ('D', 'Dinheiro'),
                        ('CQ', 'Cheque'),                   
                ] 
        cliente_cpf = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='Venda_cliente')
        data = models.DateField('Data Venda', blank=False, null=False)
        valor_total = models.DecimalField('Valor Total', max_digits=6, decimal_places=2, null=False)
        forma_pagamento = models.CharField('Forma de Pagamento', null=False, blank=False, max_length=2, choices=FORMA_PAG_CHOICES) 
        desconto = models.IntegerField('Desconto')
        
        def __str__(self):
                return self.forma_pagamento
        
class Produto (models.Model):
        CATEGORIA_PRODUTOS = [
                ('CAMISETA', 'Camiseta'),
                ('CALCA', 'Calça'),
                ('VESTIDO', 'Vestido'),
                ('SAIA', 'Saia'),      
        ]
        nome = models.CharField('Nome do Produto', max_length=60, null=False, blank=False)
        valor = models.DecimalField('Valor do Produto', max_digits=6, decimal_places=2, blank=False, null=False)
        quantidade = models.PositiveIntegerField('Quantidade', blank=False, null=False)
        imagem = models.ImageField('Imagem do Produto', blank=False, null=False)
        cat_produto = models.CharField('Categoria de Produtos', max_length=8, blank=False, null=False, choices=CATEGORIA_PRODUTOS)
        
        def __str__(self):
                return self.nome

class Item_Venda(models.Model):
        venda = models.ForeignKey(Venda, on_delete=models.PROTECT, related_name='Item_vendido' )
        produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='Produto_Item_Venda' )
        quantidade_Item = models.PositiveIntegerField('Quantidade', blank=False, null=False)
        preco_unitario = models.DecimalField('Preço Unitário', max_digits=6, decimal_places=2, blank=False, null=False)
        
        def __str__(self):
                return str(self.quantidade_Item)