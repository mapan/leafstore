from django.db import models
from slugify import slugify, slugify_unicode
from django.urls import reverse


class Collection(models.Model):
  name = models.CharField(max_length=200,
                          unique=True,
                          default='brooch',
                          db_index=True)
  slug = models.SlugField(max_length=200,
                          unique=True, editable=False)

  def save(self, *args, **kwargs):
    self.slug = slugify(self.name)
    super(Collection, self).save(*args, **kwargs)

  class Meta:
    ordering = ('name',)
    verbose_name_plural = '1. Collections'

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('collection', args=[self.slug])


class Product(models.Model):
  collection = models.ForeignKey(Collection,
                                 related_name='products',
                                 on_delete=models.CASCADE)
  name = models.CharField(max_length=200, db_index=True)
  description = models.TextField(blank=True)
  price = models.DecimalField(max_digits=10, decimal_places=2,
                              default=10)
  slug = models.SlugField(max_length=200, db_index=True, editable=False)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def save(self, *args, **kwargs):
    self.slug = slugify(self.name)
    super(Product, self).save(*args, **kwargs)

  class Meta:
    ordering = ('name',)
    index_together = (('id', 'slug'),)
    verbose_name_plural = '2. Products'

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('product', args=[self.id, self.slug])


class ProductColor(models.Model):
  product = models.ForeignKey(Product,
                              related_name='colors',
                              on_delete=models.CASCADE)
  name = models.CharField(max_length=10)
  stock = models.IntegerField(default=1)

  class Meta:
    ordering = ('product__name', 'name',)
    verbose_name_plural = '3. ProductColors'

  def __str__(self):
    return ('Product: {} Color: {}'.format(self.product.name,
                                           self.name))


class Picture(models.Model):
  color = models.ForeignKey(ProductColor,
                            related_name='pictures',
                            on_delete=models.CASCADE)
  image = models.ImageField(upload_to='images/')

  def __str__(self):
    return self.color.name
