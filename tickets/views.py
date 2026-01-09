from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import group_required
from .forms import TicketCreateForm
from .models import Ticket
from .forms import TicketAssignForm
from .forms import TicketStatusForm
from .models import TicketStatus
from .models import Reply
from .forms import ReplyForm

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

@login_required
@group_required("SupportAgent")
def update_ticket_status(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    # Prevent changes if ticket is closed
    if ticket.status == TicketStatus.CLOSED:
        return redirect("agent_tickets")

    if request.method == "POST":
        form = TicketStatusForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect("agent_tickets")
    else:
        form = TicketStatusForm(instance=ticket)

    return render(
        request,
        "tickets/update_status.html",
        {"form": form, "ticket": ticket}
    )

@login_required
def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    replies = ticket.replies.order_by("created_at")

    # Permission checks
    user = request.user
    is_customer = user.groups.filter(name="Customer").exists()
    is_agent = user.groups.filter(name="SupportAgent").exists()

    # Block unauthorized access
    if is_customer and ticket.created_by != user:
        return redirect("customer_tickets")

    if is_agent and ticket.assigned_to != user:
        return redirect("agent_tickets")

    # Block replies if closed
    can_reply = ticket.status != TicketStatus.CLOSED

    if request.method == "POST" and can_reply:
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.ticket = ticket
            reply.author = user
            reply.save()
            return redirect("ticket_detail", ticket_id=ticket.id)
    else:
        form = ReplyForm()

    return render(
        request,
        "tickets/ticket_detail.html",
        {
            "ticket": ticket,
            "replies": replies,
            "form": form,
            "can_reply": can_reply,
        }
    )
