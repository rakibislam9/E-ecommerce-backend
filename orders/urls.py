# from django.urls import path
# from .views import AddToCartView, CheckoutView

# urlpatterns = [
#     path("cart/add/", AddToCartView.as_view()),
#     path("checkout/", CheckoutView.as_view()),
# ]

from django.urls import path
from .views import create_payment_intent

urlpatterns = [
    path("create-payment-intent/", create_payment_intent),
]

