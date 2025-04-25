from django.shortcuts import render, redirect,  get_object_or_404
from .models import Product, PurchaseRequest
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def product_list(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        ).order_by('-created_at')
    else:
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

@login_required
def request_purchase(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # 자기 물건은 못 삼
    if request.user == product.seller:
        return redirect('product_list')

    # 이미 요청한 경우 중복 방지
    existing = PurchaseRequest.objects.filter(buyer=request.user, product=product).first()
    if not existing:
        PurchaseRequest.objects.create(buyer=request.user, product=product)

    return render(request, 'products/purchase_info.html', {
        'seller_account': product.seller.account_number,
        'price': product.price,
        'product': product
    })

@login_required
def accept_purchase(request, purchase_id):
    purchase = get_object_or_404(PurchaseRequest, id=purchase_id, product__seller=request.user)
    if request.method == 'POST':
        purchase.is_accepted = True
        purchase.save()
    return redirect('my_page')