from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import Collection, Product, ProductColor, Picture


class ProductInline(admin.TabularInline):
  model = Product
  formfield_overrides = {
      models.CharField: {'widget': TextInput(attrs={'size': '40'})},
      models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 40})},
  }


class ProductColorInline(admin.TabularInline):
  model = ProductColor


class PictureInline(admin.TabularInline):
  model = Picture


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
  inlines = [
      ProductInline,
  ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  inlines = [
      ProductColorInline,
  ]


@admin.register(ProductColor)
class ProductColorAdmin(admin.ModelAdmin):
  inlines = [
      PictureInline,
  ]
