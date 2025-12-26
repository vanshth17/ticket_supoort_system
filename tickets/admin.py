from django.contrib import admin

# Register your models here.
from .models import Ticket , Reply

admin.site.register(Ticket)
admin.site.register(Reply)