from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Category, Product
from .forms import ProductForm
from django.contrib import messages

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

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def add_category(request):
    pass

def welcome(request):
    return render(request, 'welcome.html')

def purchase_product(request, product_id, quantity):
    product = Product.objects.get(pk=product_id)
    if product.reduce_inventory(quantity):
        messages.sucess(request, 'Purchased successfully')
    else:
        messages.error(request, 'This item has run out of inventory')
    return redirect('product_list')