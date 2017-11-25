from django.db import models

# Create your models here.
class Product(models.Model):
    Name = models.TextField()
    Description = models.TextField()
    Code = models.TextField()

class Order(models.Model):
    Code = models.TextField()
    ProductCode = models.TextField()