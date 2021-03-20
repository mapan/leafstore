from django import template
from ..models import Collection

register = template.Library()


@register.simple_tag
def get_all_collections():
  return Collection.objects.all()
