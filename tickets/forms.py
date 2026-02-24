from django import forms
from .models import Ticket
from .models import Reply

class TicketCreateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description"]

        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Short summary of your issue"
            }),
            "description": forms.Textarea(attrs={
                "placeholder": "Explain the problem in detail..."
            }),
        }
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
        fields = ["status"]

        widgets = {
            "status": forms.Select(attrs={
                "class": "status-select"
            })
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['message']