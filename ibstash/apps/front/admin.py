from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Discount)
admin.site.register(Delivery)
admin.site.register(Variant)
admin.site.register(Category)
admin.site.register(Inventory)
