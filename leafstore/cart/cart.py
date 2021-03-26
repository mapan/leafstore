from decimal import Decimal
from django.conf import settings
from store.models import Product, ProductColor
from ast import literal_eval


def _get_cart_key(product, color):
  return str((product.id, color.id))


class Cart(object):

  def __init__(self, request):
    self.session = request.session
    cart_key = settings.CART_SESSION_ID
    if cart_key not in self.session:
      self.session[cart_key] = {}
    self.cart = self.session.get(cart_key)

  def add(self, product, color, quantity=1, override_quantity=False):
    key = _get_cart_key(product, color)
    if key not in self.cart:
      self.cart[key] = {
          'price': str(product.price),
          'quantity': 0,
      }
    if override_quantity:
      self.cart[key]['quantity'] = quantity
    else:
      self.cart[key]['quantity'] += quantity

    self.save()

  def remove(self, product, color):
    self.cart.pop(_get_cart_key(product, color), None)
    self.save()

  def save(self):
    self.session.modified = True

  def __iter__(self):
    cart = self.cart.copy()
    for key in self.cart.keys():
      product_id, color_id = literal_eval(key)
      cart[key]['product'] = Product.objects.get(id=product_id)
      cart[key]['color'] = ProductColor.objects.get(id=color_id)
    for item in cart.values():
      item['price'] = Decimal(item['price'])
      item['total_price'] = item['price'] * item['quantity']
      yield item

  def __len__(self):
    """Returns the total number of items in the cart."""
    return sum(item['quantity'] for item in self.cart.values())

  def get_total_price(self):
    return sum(
        Decimal(item['price']) * item['quantity'] for item
        in self.cart.values()
    )

  def clear(self):
    # Remove cart from session.
    del self.session[settings.CART_SESSION_ID]
    self.save()
