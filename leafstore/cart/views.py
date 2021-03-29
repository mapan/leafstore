from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Product, ProductColor
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id, color_id=None):
  cart = Cart(request)
  product = get_object_or_404(Product, id=product_id)
  color_id = color_id or request.POST.get('color')
  color = get_object_or_404(ProductColor, id=color_id)
  cart.add(product=product,
           color=color,
           quantity=int(request.POST.get('quantity')),
           override_quantity=False)
  return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, product_id, color_id):
  cart = Cart(request)
  product = get_object_or_404(Product, id=product_id)
  color = get_object_or_404(ProductColor, id=color_id)
  cart.remove(product, color)
  return redirect('cart:cart_detail')


def cart_detail(request):
  cart = Cart(request)
  return render(request, 'cart/detail.html', {'cart': cart})
