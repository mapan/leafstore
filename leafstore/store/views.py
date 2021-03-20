from django.shortcuts import render
from django.http import HttpResponse

from .models import Collection, Product, ProductColor, Picture


def index(request):
  return render(request, 'store/index.html')


def story(request):
  return render(request, 'store/story.html')


def collection(request, slug):
  collection = Collection.objects.get(slug=slug)
  products = collection.products.all()
  context = {'products': products}
  return render(request, 'store/collection.html', context)


def contact(request):
  return render(request, 'store/contact.html')
