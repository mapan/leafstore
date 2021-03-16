from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'store/index.html')

def story(request):
    return render(request, 'store/story.html')

def collection(request):
    return render(request, 'store/collection.html')

def contact(request):
    return render(request, 'store/contact.html')