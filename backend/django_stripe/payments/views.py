from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import stripe

from .models import Items


def create_checkout_session(request, pk):
    item = Items.objects.get(pk=pk)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    domain = 'http://127.0.0.1:8000'
    session = stripe.checkout.Session.create(
        mode='payment',
        payment_method_types=['card'],
        success_url=domain +'/success/',
        cancel_url=domain + '/cancel/',
        line_items=[{
            'price_data': {
                'currency': 'eur',
                'product_data': {
                    'name': item.name
                },
                'unit_amount': item.price,
            },
            'quantity': 1,
        }]
    )
    return JsonResponse({'id': session['id']})
