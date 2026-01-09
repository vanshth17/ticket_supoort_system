from django.urls import path
from . import views

urlpatterns = [
    path("", views.customer_tickets, name="customer_tickets"),
    path("create/", views.create_ticket, name="create_ticket"),
    path("agent/", views.agent_tickets, name="agent_tickets"),
    path("<int:ticket_id>/assign/", views.assign_ticket, name="assign_ticket"),
    path("<int:ticket_id>/status/", views.update_ticket_status, name="update_ticket_status"),
    path("<int:ticket_id>/", views.ticket_detail, name="ticket_detail"),
]