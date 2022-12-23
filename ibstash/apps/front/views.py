from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView
from .models import (Client, Order, Product, Category, Inventory)
from datetime import datetime
from .forms import InventoryForm
from django.db.models import Count, F


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

class ProductDetailView(DetailView):
    model = Product
    template_name = 'front/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = kwargs.get('object')
        product_id = product.pk
        context['inventories'] = Inventory.objects.filter(product_id=product_id).annotate(
            variant_name=F('variant__variant_name'))
        context['inventory_form'] = InventoryForm(None,
                                                  initial={'product': product})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        context['inventories'] = Inventory.objects.filter(product_id=self.object.pk)
        context['inventory_form'] = InventoryForm(None, initial={'product': self.object})
        form = InventoryForm(request.POST or None, initial={'product': self.object})
        if form.is_valid():
            form.save()
            return self.render_to_response(context=context)
        elif 'already exists.' in str(form.errors):
            form_data = form.cleaned_data
            Inventory.objects.filter(product=form_data.get('product'), variant=form_data.get('variant')).update(
                quantity=form_data.get('quantity'))
            return self.render_to_response(context=context)
        else:
            return self.render_to_response(context=context)


class ProductCreateView(CreateView):
    model = Product
    template_name = 'front/products.html'
    success_url = '/product'
    fields = ['product_name', 'product_price', 'product_img', 'category']

    def get_context_data(self, **kwargs):
        kwargs['products'] = Product.objects.all().annotate(category_name=F('category__category_name'))
        return super(ProductCreateView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.product_code = abs(hash(str(datetime.now()) + form.instance.product_name))
        form.save()
        return super().form_valid(form)


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


# Category Views

class CategoryView(ListView):
    model = Category
    template_name = 'front/categories.html'
    context_object_name = 'categories'


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'front/categories_form.html'
    success_url = '/category'
    fields = ['category_name', 'variant']


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'front/delete_confirm.html'
    success_url = '/category'


# Inventory Views

class InventoryView(ListView):
    model = Inventory
    template_name = 'front/inventories.html'
    context_object_name = 'inventories'


class InventoryCreateView(CreateView):
    model = Inventory
    template_name = 'front/inventories_form.html'
    success_url = '/inventory'
    fields = ['product', 'variant', 'quantity']


class InventoryDeleteView(DeleteView):
    model = Inventory
    template_name = 'front/delete_confirm.html'
    success_url = '/inventory'
