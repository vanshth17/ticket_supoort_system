from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.decorators import group_required

@login_required
@group_required("Customer")
def customer_dashboard(request):
    return render(request,'core/customer_dashboard.html')

@login_required
def home(request):
    user = request.user

    is_customer = user.groups.filter(name="Customer").exists()
    is_agent = user.groups.filter(name="SupportAgent").exists()

    return render(
        request,
        "core/home.html",
        {
            "is_customer": is_customer,
            "is_agent": is_agent,
        }
    )
