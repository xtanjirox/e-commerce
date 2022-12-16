from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Client, Order, Product


# Clients Views

class ClientView(ListView):
    model = Client
    template_name = 'front/clients.html'
    context_object_name = 'clients'


class ClientCreateView(CreateView):
    model = Client
    template_name = 'front/clients_form.html'
    success_url = '/client'
    fields = ['client_name', 'client_email', 'client_phone', 'client_addr']


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'front/delete_confirm.html'
    success_url = '/client'


# Products Views

class ProductView(ListView):
    model = Product
    template_name = 'front/products.html'
    context_object_name = 'products'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'front/products_form.html'
    success_url = '/product'
    fields = ['product_code', 'product_name', 'product_price', 'product_img']


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'front/delete_confirm.html'
    success_url = '/product'


# Orders Views

class OrderView(ListView):
    model = Order
    template_name = 'front/orders.html'
    context_object_name = 'orders'


class OrderCreateView(CreateView):
    model = Order
    template_name = 'front/orders_form.html'
    success_url = '/order'
    fields = ['client', 'payment', 'delivery', 'discount', 'order_total_base', 'order_total_discount']


class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'front/delete_confirm.html'
    success_url = '/order'
