from django.shortcuts import render
from django.http import HttpResponse

from .models import Product


def index(request):
    products = list(Product.objects.all())
    context = {'products': products}
    return render(request, 'store/index.html', context)

def story(request):
    return render(request, 'store/story.html')

def collection(request):
    return render(request, 'store/collection.html')

def contact(request):
    return render(request, 'store/contact.html')