from django.urls import path
from .views import (ClientView, OrderView, ClientCreateView, OrderCreateView, ClientDeleteView, OrderDeleteView)

urlpatterns = [
    # Clients views
    path('client/', ClientView.as_view()),
    path('create_client/', ClientCreateView.as_view()),
    path('client/<pk>/delete/', ClientDeleteView.as_view()),

    # Products views
    path('product/', OrderView.as_view()),
    path('create_product/', OrderCreateView.as_view()),
    path('product/<pk>/delete/', OrderDeleteView.as_view()),

    # Orders views
    path('order/', OrderView.as_view()),
    path('create_order/', OrderCreateView.as_view()),
    path('order/<pk>/delete/', OrderDeleteView.as_view()),
]
