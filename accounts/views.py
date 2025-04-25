from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from products.models import Product, PurchaseRequest
from reports.models import Report
from .forms import CustomUserCreationForm
from .models import CustomUser  # ✅ CustomUser import 추가


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_banned:
                form.add_error(None, "이 계정은 정지되었습니다.")
            else:
                login(request, user)
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
def my_page(request):
    user = request.user
    my_products = Product.objects.filter(seller=user).order_by('-created_at')
    my_reports = Report.objects.filter(reporter=user).order_by('-created_at')
    incoming_requests = PurchaseRequest.objects.filter(product__seller=user, is_accepted=False)
    users = CustomUser.objects.exclude(id=user.id)

    context = {
        'user': user,
        'products': my_products,
        'reports': my_reports,
        'incoming_requests': incoming_requests,
        'users': users
    }
    return render(request, 'accounts/my_page.html', context)


@login_required
def update_account(request):
    if request.method == 'POST':
        account_number = request.POST.get('account_number')
        request.user.account_number = account_number
        request.user.save()
        return redirect('my_page')
    return render(request, 'accounts/update_account.html')