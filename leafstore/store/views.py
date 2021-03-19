from django.shortcuts import render
from django.http import HttpResponse

from .models import Product


def index(request):
  return render(request, 'store/index.html')


def story(request):
  return render(request, 'store/story.html')


def collection(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/collection.html', context)

def contact(request):
  return render(request, 'store/contact.html')
