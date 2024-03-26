from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('welcome/', views.welcome, name='welcome'),
    path('accounts/complete/google-oauth2/', views.google_login_callback, name="google_login_callback"),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/products/', views.products_by_category, name='products_by_category'),
    path('add_product/', views.add_product, name='add_product'),
    path('product_list/', views.product_view, name="product_list"),
    path('add_category/', views.add_category, name='add_category'),
    path('cart/', views.cart_view, name="cart"),
    path('purchase/<int:product_id>/<int:quantity>/', views.purchase_product, name='purchase_product'),
    path('add-to-cart/<int:product_id>/<int:quantity>/', views.add_to_cart, name="add_to_cart"),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name="remove_from_cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('logout/', views.logout_view, name='logout_view'),
]

