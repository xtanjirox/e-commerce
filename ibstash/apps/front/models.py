from django.db import models
from datetime import datetime


class Client(models.Model):
    client_name = models.CharField(max_length=30)
    client_email = models.CharField(max_length=100, blank=True, null=True)
    client_phone = models.CharField(max_length=30)
    client_addr = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'client'
        unique_together = (('client_phone', 'client_name'))

    def __str__(self):
        return f'{self.client_name}_{self.client_phone}'


class Variant(models.Model):
    variant_name = models.CharField(max_length=20)

    class Meta:
        db_table = 'variant'

    def __str__(self):
        return self.variant_name


class Category(models.Model):
    category_name = models.CharField(max_length=30)
    variant = models.ManyToManyField(Variant)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_code = models.IntegerField()
    product_name = models.CharField(max_length=50)
    product_price = models.FloatField(default=0)
    product_img = models.CharField(max_length=300, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.product_name


class Payment(models.Model):
    payment_status = models.CharField(max_length=20)

    class Meta:
        db_table = 'payment'

    def __str__(self):
        return self.payment_status


class Discount(models.Model):
    discount_name = models.CharField(max_length=20)

    class Meta:
        db_table = 'discount'

    def __str__(self):
        return self.discount_name


class Delivery(models.Model):
    delivery_status = models.CharField(max_length=20)

    class Meta:
        db_table = 'delivery'

    def __str__(self):
        return self.delivery_status


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, blank=True, null=True)
    discount = models.ManyToManyField(Discount, blank=True, null=True)
    order_total_base = models.FloatField(default=0)
    order_total_discount = models.FloatField(default=0)
    create_date = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = 'order'


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_quantity = models.IntegerField(default=0)
    product_desc = models.CharField(max_length=300, null=True, blank=True)

    class Meta:
        db_table = 'cart'


class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        db_table = 'inventory'
        unique_together = (('product', 'variant'), )
