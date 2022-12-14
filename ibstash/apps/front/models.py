from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=30)
    client_email = models.CharField(max_length=100, blank=True, null=True)
    client_phone = models.CharField(max_length=30)
    client_addr = models.CharField(max_length=100, blank=True, null=True)


class Product(models.Model):
    product_code = models.IntegerField()
    product_name = models.CharField(max_length=50)
    product_img = models.CharField(max_length=300, null=True, blank=True)


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_quantity = models.IntegerField(default=0)
    product_desc = models.CharField(max_length=300, null=True, blank=True)


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
