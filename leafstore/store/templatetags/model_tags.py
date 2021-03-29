from django import template
from ..models import Collection, ProductColor, Picture

register = template.Library()


@register.simple_tag
def get_all_collections():
  return Collection.objects.all()


@register.simple_tag
def get_product_colors(product):
  return ProductColor.objects.filter(
      product__id=product.id).filter(stock__gt=0)


@register.simple_tag
def get_product_pictures(product):
  colors = get_product_colors(product)
  return Picture.objects.filter(color__in=colors)


@register.simple_tag
def get_color_quantity(product):
  colors = get_product_colors(product)
  color_id_to_quantity = {}
  for color in colors:
    color_id_to_quantity[color.id] = int(color.stock)
  return color_id_to_quantity


@register.simple_tag
def get_color_pictures(product):
  colors = get_product_colors(product)
  color_id_to_pictures = {}
  for color in colors:
    color_id_to_pictures[color.id] = (
      [p.image.url for p in color.pictures.all()])
  return color_id_to_pictures
