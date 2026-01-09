from django.contrib import admin

# Register your models here.
from .models import Ticket , Reply

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "status",
        "created_by",
        "assigned_to",
        "created_at",
    )

    list_filter = ("status", "created_at")

    search_fields = ("title", "description", "created_by__username")

    list_editable = ("status", "assigned_to")

    ordering = ("-created_at",)
    
@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ("id", "ticket", "author", "created_at")
    list_filter = ("created_at",)
    search_fields = ("message", "author__username")
    ordering = ("-created_at",)