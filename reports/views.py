from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Report
from products.models import Product
from django.contrib.auth.models import User

@login_required
def add_report(request):
    if request.method == 'POST':
        report_type = request.POST.get('report_type')
        reason = request.POST.get('reason')
        reported_id = request.POST.get('reported_id')

        report = Report(
            report_type=report_type,
            reason=reason,
            reporter=request.user
        )

        if report_type == 'user':
            try:
                report.reported_user = User.objects.get(id=reported_id)
            except:
                pass
        elif report_type == 'product':
            try:
                report.reported_product = Product.objects.get(id=reported_id)
            except:
                pass

        report.save()
        return redirect('/reports/')

    users = User.objects.exclude(id=request.user.id)
    products = Product.objects.all()
    return render(request, 'reports/add_report.html', {'users': users, 'products': products})

@login_required
def report_list(request):
    reports = Report.objects.all().order_by('-created_at')
    return render(request, 'reports/report_list.html', {'reports': reports})