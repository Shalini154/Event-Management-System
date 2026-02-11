from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Membership, Transaction, Maintenance
from .forms import MembershipForm

# --------------------------------------------------
# CHECK ADMIN USER
# --------------------------------------------------
def is_admin(user):
    return user.is_superuser

# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------
def home(request):
    return render(request, 'home.html')

# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

# --------------------------------------------------
# MAINTENANCE MODULE (MANDATORY PART)
# --------------------------------------------------
@user_passes_test(is_admin)
def maintenance(request):
    if request.method == 'POST':
        Maintenance.objects.create(title="Base Data Initialized")

    data = Maintenance.objects.all()
    return render(request, 'maintenance.html', {'data': data})

# --------------------------------------------------
# ADD MEMBERSHIP
# --------------------------------------------------
@login_required
def add_membership(request):
    if not Maintenance.objects.exists():
        return render(request, 'blocked.html')

    form = MembershipForm(request.POST or None)
    if form.is_valid():
        membership = form.save(commit=False)
        membership.maintenance = Maintenance.objects.first()
        membership.save()

        Transaction.objects.create(
            membership=membership,
            action='Created'
        )
        return redirect('reports')

    return render(request, 'add_membership.html', {'form': form})

# --------------------------------------------------
# SEARCH MEMBERSHIP FOR UPDATE
# --------------------------------------------------
@login_required
def search_update(request):
    if request.method == 'POST':
        mid = request.POST.get('mid')
        if mid:
            return redirect('update_membership', pk=mid)
    return render(request, 'search_update.html')

# --------------------------------------------------
# UPDATE MEMBERSHIP
# --------------------------------------------------
@login_required
def update_membership(request, pk):
    membership = get_object_or_404(Membership, pk=pk)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'extend':
            membership.duration = '6M'
            membership.save()
            Transaction.objects.create(membership=membership, action='Extended')

        elif action == 'cancel':
            membership.active = False
            membership.save()
            Transaction.objects.create(membership=membership, action='Cancelled')

        return redirect('reports')

    return render(request, 'update_membership.html', {'m': membership})

# --------------------------------------------------
# REPORTS MODULE
# --------------------------------------------------
@login_required
def reports(request):
    data = Membership.objects.all()
    return render(request, 'reports.html', {'data': data})

# --------------------------------------------------
# TRANSACTIONS MODULE
# --------------------------------------------------
@login_required
def transactions(request):
    data = Transaction.objects.all()
    return render(request, 'transactions.html', {'data': data})

