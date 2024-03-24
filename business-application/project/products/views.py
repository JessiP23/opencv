from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Category, Product, CartItem
from .forms import ProductForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def add_product(request):
    if not request.user.is_superuser:
        return redirect('product_list')
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def purchase_product(request, product_id, quantity):
    product = Product.objects.get(pk=product_id)
    if product.reduce_inventory(quantity):
        messages.success(request, 'Purchased successfully')
    else:
        messages.error(request, 'This item has run out of inventory')
    return redirect('product_list')

def category_list(request):
    categories = Category.objects.all()
    data = [{'id': category.id, 'name': category.name} for category in categories]
    return JsonResponse(data, safe=False)

def products_by_category(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    data = [{'name': product.name, 'price': str(product.price)} for product in products]
    return JsonResponse(data, safe=False)

def product_view(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def add_category(request):
    pass

def welcome(request):
    return render(request, 'welcome.html')

def add_to_cart(request, product_id, quantity):
    product = get_object_or_404(Product, pk=product_id)

    if request.user.is_authenticated:
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return redirect('product_list')

    else:
        return redirect('login')

def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})