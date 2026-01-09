from django import forms
from .models import Ticket

class TicketCreateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title' , 'description']

from django.contrib.auth.models import User

class TicketAssignForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['assigned_to']
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields['assigned_to'].queryset = User.objects.filter(
            groups__name="SupportAgent"
        )

class TicketStatusForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['status']
