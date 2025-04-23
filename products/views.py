from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.decorators import login_required

def product_list(request):
    products = Product.objects.order_by('-created_at')
    return render(request, 'products/product_list.html', {'products': products})

@login_required
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        if name and price:
            Product.objects.create(
                name=name,
                description=description,
                price=price,
                image=image,
                seller=request.user
            )
            return redirect('/products/')
    return render(request, 'products/add_product.html')