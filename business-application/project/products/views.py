import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Category, Product, CartItem
from .forms import ProductForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from allauth.socialaccount.models import SocialAccount

stripe.api_key = settings.STRIPE_SECRET_KEY

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

@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, pk=item_id)
    if cart_item.user == request.user:
        cart_item.delete()
    return redirect('cart')

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        try:
            payment_method = request.POST['payment_method']

            intent = stripe.PaymentIntent.create(
                amount=int(total_price * 100),
                currency='usd',
                payment_method=payment_method,
                confirm=True,
                description='Online Purchase',
            )
            messages.success(request, 'Payment successful')
            return redirect('payment_success')
        except stripe.error.CartError as e:
            messages.error(request, f"Card Error: {e.error.message}")
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
    return render(request, 'checkout.html', {'total_price': total_price})

def landing_page(request):
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect("landing_page")

def google_login_callback(request):
    print("Google callback GET data:", request.GET)
    code = request.GET.get('code')

    user = SocialAccount.objects.get(provider='google', uid=request.GET.get('code')).user
    print("Authenticated user:", user)

    if user is not None:
        login(request, user)
        return redirect('welcome')
    else:
        return redirect('login_page')
    