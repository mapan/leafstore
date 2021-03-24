from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Collection, Product, ProductColor, Picture


def index(request):
  return render(request, 'store/index.html')


def story(request):
  return render(request, 'store/story.html')


def collection(request, slug=None):
  collection = None
  collections = Collection.objects.all()
  products = Product.objects.filter(colors__stock__gt=0)
  if slug:
    collection = get_object_or_404(Collection, slug=slug)
    collections = [collection]
    products = products.filter(collection=collection)

  context = {'collection': collection,
             'collections': collections,
             'products': products}

  return render(request, 'store/collection.html', context)


def product(request, id, slug):
  product = get_object_or_404(Product,
                              id=id,
                              slug=slug)
  return render(request,
                'store/product.html',
                {'product': product})


def contact(request):
  return render(request, 'store/contact.html')
