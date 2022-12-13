from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=30)
    client_email = models.CharField(max_length=100, blank=True, null=True)
    client_phone = models.CharField(max_length=30)
    client_addr = models.CharField(max_length=100, blank=True, null=True)


class Product(models.Model):
    pass


class Cart(models.Model):
    product = models.ManyToManyField(Product)
    product_quantity = models.IntegerField(default=0)


class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
