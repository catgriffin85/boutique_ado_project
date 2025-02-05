from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'k_test_51QpEhMAuYHlxCm28Sv8ZnsIPMA9742ih5b497aCQCjf0WezZ2wIw2T7wOPZw4obWEHIusd9XBUbyPWHM0rQopJwC00tdkJQqZ8',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)