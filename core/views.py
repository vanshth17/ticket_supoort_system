from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.decorators import group_required

@login_required
@group_required("Customer")
def customer_dashboard(request):
    return render(request,'core/customer_dashboard.html')