from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from products.models import Product
from reports.models import Report

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
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

    context = {
        'user': user,
        'products': my_products,
        'reports': my_reports,
    }
    return render(request, 'accounts/my_page.html', context)