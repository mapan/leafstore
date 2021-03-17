from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=200)
  details = models.TextField(default='d')
  price = models.FloatField(default=10)
  
class Picture(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='images/')

