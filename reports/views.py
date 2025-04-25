from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Report
from .forms import ReportForm
from products.models import Product
from accounts.models import CustomUser

# 상품 신고
@login_required
def report_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.report_type = 'product'
            report.reporter = request.user
            report.reported_product = product
            report.save()
            return redirect('/')
    else:
        form = ReportForm()

    return render(request, 'reports/report_form.html', {
        'form': form,
        'target_type': '상품',
        'target_name': product.name
    })

# 사용자 신고
@login_required
def report_user(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)

    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.report_type = 'user'
            report.reporter = request.user
            report.reported_user = target_user
            report.save()
            return redirect('/')
    else:
        form = ReportForm()

    return render(request, 'reports/report_form.html', {
        'form': form,
        'target_type': '사용자',
        'target_name': target_user.username
    })

# 관리자용 신고 목록 조회
@login_required
def report_list(request):
    reports = Report.objects.all().order_by('-created_at')
    return render(request, 'reports/report_list.html', {'reports': reports})