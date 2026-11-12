from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages

# Create your views here.

def index(request):
          return render (request, 'index.html')

def CadastraCliente(request):
        if request.method == 'POST':
                form = ClienteForms(request.POST, request.FILES)
                if form.is_valid():
                            form.save()
                            messages.success(request, 'Cliente Cadastrado com sucesso')
                            form = ClienteForms()
                else:
                            messages.error(request, 'Erro ao cadastrar o cliente')
        else: 
            form = ClienteForms()
        context = {'form':form}
        return render (request, 'cadastroCliente.html', context)
        
                
                
          


