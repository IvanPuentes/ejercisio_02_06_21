from django.urls import path
from django.urls import path
from orders.views import OrdersPageView, charge

urlpatterns=[
    path('charge/', charge, name='charge'),
    path('orders/purchase',OrdersPageView.as_view(), name='orders'),
]