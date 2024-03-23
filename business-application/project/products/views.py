from django.shortcuts import render
from django.http import JsonResponse
from .models import Category, Product

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
    categories = Category.objects.all()

    if request.method == 'POST':
        pass
    else:
        return render(request, 'add_product.html', {'categories': categories})

def add_category(request):
    pass

def welcome(request):
    return render(request, 'welcome.html')
