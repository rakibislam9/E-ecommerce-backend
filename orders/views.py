# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from .models import Cart, CartItem, Order
# from .serializers import CartItemSerializer, OrderSerializer
# from products.models import Product
# from decimal import Decimal

# class AddToCartView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         product_id = request.data.get("product_id")
#         qty = int(request.data.get("quantity", 1))

#         cart, _ = Cart.objects.get_or_create(user=request.user)
#         product = Product.objects.get(id=product_id)

#         item, created = CartItem.objects.get_or_create(
#             cart=cart, product=product
#         )
#         if not created:
#             item.quantity += qty
#         item.save()

#         return Response({"message": "Added to cart"})


# class CheckoutView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         cart = Cart.objects.get(user=request.user)
#         total = Decimal("0.00")

#         for item in cart.items.all():
#             total += item.product.price * item.quantity

#         order = Order.objects.create(
#             user=request.user,
#             total=total,
#             status="pending"
#         )

#         cart.items.all().delete()
#         return Response(OrderSerializer(order).data)


import stripe
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

stripe.api_key = settings.STRIPE_SECRET_KEY


@api_view(['POST'])
def create_payment_intent(request):
    amount = request.data.get("amount")  # cents

    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency="usd",
        payment_method_types=["card"],
    )

    return Response({
        "clientSecret": intent.client_secret
    })
