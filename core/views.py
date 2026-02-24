from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.decorators import group_required
from tickets.models import Ticket

@login_required
def customer_dashboard(request):
    user = request.user

    is_customer = user.groups.filter(name="Customer").exists()
    is_agent = user.groups.filter(name="SupportAgent").exists()

    # Stats
    if is_customer:
        total_tickets = Ticket.objects.filter(created_by=user).count()
        open_tickets = Ticket.objects.filter(created_by=user, status="OPEN").count()
        recent_tickets = Ticket.objects.filter(created_by=user).order_by("-created_at")[:5]

    elif is_agent:
        total_tickets = Ticket.objects.filter(assigned_to=user).count()
        open_tickets = Ticket.objects.filter(assigned_to=user, status="OPEN").count()
        recent_tickets = Ticket.objects.filter(assigned_to=user).order_by("-created_at")[:5]

    else:
        total_tickets = 0
        open_tickets = 0
        recent_tickets = []

    context = {
        "is_customer": is_customer,
        "is_agent": is_agent,
        "total_tickets": total_tickets,
        "open_tickets": open_tickets,
        "recent_tickets": recent_tickets,
    }

    return render(request, "core/home.html", context)

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tickets.models import Ticket

@login_required
def home(request):
    user = request.user

    is_customer = user.groups.filter(name="Customer").exists()
    is_agent = user.groups.filter(name="SupportAgent").exists()

    # Stats + recent tickets
    if is_customer:
        total_tickets = Ticket.objects.filter(created_by=user).count()
        open_tickets = Ticket.objects.filter(created_by=user, status="OPEN").count()
        recent_tickets = Ticket.objects.filter(created_by=user).order_by("-created_at")[:5]

    elif is_agent:
        total_tickets = Ticket.objects.filter(assigned_to=user).count()
        open_tickets = Ticket.objects.filter(assigned_to=user, status="OPEN").count()
        recent_tickets = Ticket.objects.filter(assigned_to=user).order_by("-created_at")[:5]

    else:
        total_tickets = 0
        open_tickets = 0
        recent_tickets = []

    return render(
        request,
        "core/home.html",
        {
            "is_customer": is_customer,
            "is_agent": is_agent,
            "total_tickets": total_tickets,
            "open_tickets": open_tickets,
            "recent_tickets": recent_tickets,
        }
    )