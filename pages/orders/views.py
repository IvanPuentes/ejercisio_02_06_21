from django.views.generic.list import ListView
import stripe
from django.views.generic.base import TemplateView
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.models import Permission

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key']=settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context

def charge(request):
    
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount = 1500,
            currency='usd',
            description='pago de servicio',
            source=request.POST['stripeToken']
        )
    return render(request, 'orders/charge.html')
        
