from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import group_required
from .forms import TicketCreateForm
from .models import Ticket
from .forms import TicketAssignForm

@login_required
@group_required("Customer")
def create_ticket(request):

    if request.method == 'POST':
        form = TicketCreateForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user
            ticket.save()
            return redirect("customer_tickets")
    else:
        form = TicketCreateForm()
    return render(request,"tickets/create_ticket.html" , {"form":form})

@login_required
@group_required("Customer")
def customer_tickets(request):
    tickets = request.user.created_tickets.all()
    return render(request, "tickets/customer_tickets.html", {"tickets": tickets})

from .forms import TicketAssignForm
from .models import Ticket

@login_required
@group_required("SupportAgent")
def assign_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)

    if request.method == "POST":
        form = TicketAssignForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect("agent_tickets")
    else:
        form = TicketAssignForm(instance=ticket)

    return render(
        request,
        "tickets/assign_ticket.html",
        {"form": form, "ticket": ticket}
    )

@login_required
@group_required("SupportAgent")
def agent_tickets(request):
    tickets = request.user.assigned_tickets.all()
    return render(
        request,
        "tickets/agent_tickets.html",
        {"tickets": tickets}
    )

