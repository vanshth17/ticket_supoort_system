from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_ticket, name="create_ticket"),
    path("", views.customer_tickets, name="customer_tickets"),
    path("<int:ticket_id>/assign/", views.assign_ticket, name="assign_ticket"),
    path("agent/", views.agent_tickets, name="agent_tickets"),

]
