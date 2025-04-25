from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from accounts.models import CustomUser
from reports.models import Report
from products.models import Product
from chat.models import Message

def index(request):
    return render(request, 'index.html')

# 관리자 전용 접근
def admin_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)

@admin_required
def admin_dashboard(request):
    users = CustomUser.objects.all()
    products = Product.objects.all()
    reports = Report.objects.all()
    messages = Message.objects.all()
    return render(request, 'core/admin_dashboard.html', {
        'users': users,
        'products': products,
        'reports': reports,
        'messages': messages
    })

@admin_required
def ban_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.is_banned = True
    user.save()
    return redirect('admin_dashboard')

@admin_required
def unban_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.is_banned = False
    user.save()
    return redirect('admin_dashboard')

@admin_required
def delete_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.delete()
    return redirect('admin_dashboard')