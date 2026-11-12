from django import forms 
from .models import *

class ClienteForms (forms.ModelForm):
          class Meta:
                    model = Cliente
                    fields = '__all__'