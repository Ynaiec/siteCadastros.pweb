from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from venda.models import * 

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
          list_display = ('usuario', 'cpf', 'nome', 'telefone', 'email', 'logradouro', 'numero', 'sexo')
          
@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
          list_display = ('cliente_cpf', 'data', 'valor_total', 'forma_pagamento', 'desconto')

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
          list_display = ('nome', 'valor', 'quantidade', 'imagem', 'cat_produto')
          
@admin.register(Item_Venda)
class Item_VendaAdmin(admin.ModelAdmin):
          list_display = ('venda', 'produto', 'quantidade_Item', 'preco_unitario')


