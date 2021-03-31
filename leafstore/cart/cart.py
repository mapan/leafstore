from decimal import Decimal
from django.conf import settings
from store.models import ProductColor


class Cart(object):

  def __init__(self, request):
    self.session = request.session
    cart_key = settings.CART_SESSION_ID
    if cart_key not in self.session:
      self.session[cart_key] = {}
    self.cart = self.session.get(cart_key)

  def add(self, color, quantity=1, override_quantity=False):
    key = str(color.id)
    if key not in self.cart:
      self.cart[key] = {
          'price': str(color.product.price),
          'quantity': 0,
      }
    if override_quantity:
      self.cart[key]['quantity'] = quantity
    else:
      new_quantity = self.cart[key]['quantity'] + quantity
      if new_quantity > color.stock:
        return
      self.cart[key]['quantity'] = new_quantity

    self.save()

  def remove(self, color):
    self.cart.pop(str(color.id), None)
    self.save()

  def save(self):
    self.session.modified = True

  def __iter__(self):
    cart = self.cart.copy()
    for key in self.cart.keys():
      cart[key]['color'] = ProductColor.objects.get(id=int(key))
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
