from django.urls import path
from .views import (ClientView, OrderView, ClientCreateView, OrderCreateView, ClientDeleteView, OrderDeleteView,
                    CategoryView, CategoryCreateView, CategoryDeleteView, ProductCreateView,
                    ProductDeleteView, ProductDetailView, InventoryView, InventoryCreateView, InventoryDeleteView)

urlpatterns = [
    # Clients views
    path('client/', ClientView.as_view()),
    path('create_client/', ClientCreateView.as_view()),
    path('client/<pk>/delete/', ClientDeleteView.as_view()),

    # Products views
    path('product/', ProductCreateView.as_view()),
    path('product/<pk>', ProductDetailView.as_view(), name='article-detail'),
    path('product/<pk>/delete/', ProductDeleteView.as_view()),

    # Orders views
    path('order/', OrderView.as_view()),
    path('create_order/', OrderCreateView.as_view()),
    path('order/<pk>/delete/', OrderDeleteView.as_view()),

    # categories views
    path('category/', CategoryView.as_view()),
    path('create_category/', CategoryCreateView.as_view()),
    path('category/<pk>/delete/', CategoryDeleteView.as_view()),

    # inventories views
    path('inventory/', InventoryView.as_view()),
    path('create_inventory/', InventoryCreateView.as_view()),
    path('inventory/<pk>/delete/', InventoryDeleteView.as_view()),
]
