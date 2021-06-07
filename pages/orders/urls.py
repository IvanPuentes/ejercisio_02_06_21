from django.urls import path
from django.urls.resolvers import URLPattern
from orders.views import OrdersPageView, charge

URLPattern = [
    path('charge/', charge, name='charge'),
    path('',OrdersPageView.as_view(), name='orders'),
]