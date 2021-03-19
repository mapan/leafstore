from django.db import models
from slugify import slugify, slugify_unicode


class Collection(models.Model):
  name = models.CharField(max_length=200,
                          default='brooch',
                          db_index=True)
  # slug = models.SlugField(max_length=200,
  #                         unique=True, editable=False)

  class Meta:
    ordering = ('name',)

  def __str__(self):
    return self.name


class Product(models.Model):
  collection = models.ForeignKey(Collection,
                                 related_name='products',
                                 on_delete=models.CASCADE)
  name = models.CharField(max_length=200, db_index=True)
  slug = models.SlugField(max_length=200, db_index=True, editable=False)
  description = models.TextField(blank=True)
  price = models.DecimalField(max_digits=10, decimal_places=2,
                              default=10)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def save(self, *args, **kwargs):
    self.slug = slugify(self.name)
    super(Collection, self).save(*args, **kwargs)

  class Meta:
    ordering = ('name',)
    index_together = (('id', 'slug'),)

  def __str__(self):
    return self.name


class ProductColor(models.Model):
  product = models.ForeignKey(Product,
                              related_name='colors',
                              on_delete=models.CASCADE)
  color = models.CharField(max_length=10, default='red')
  stock = models.DecimalField(max_digits=10, decimal_places=0,
                              default=1)

  class Meta:
    ordering = ('color',)

  def __str__(self):
    return self.color


class Picture(models.Model):
  color = models.ForeignKey(ProductColor,
                            related_name='pictures',
                            on_delete=models.CASCADE)
  image = models.ImageField(upload_to='images/')

  def __str__(self):
    return 'Picture'
