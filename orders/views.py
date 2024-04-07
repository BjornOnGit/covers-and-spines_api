from rest_framework import generics, status
from rest_framework.response import Response
from pypaystack import Transaction
from django.conf import settings
from rest_framework.permissions import IsAuthenticated

class BookOrder(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        amount = int(request.data.get('amount'))
        email = request.data.get('email')
        auth_code = request.data.get('auth_code')

        transaction = Transaction(authorization_key=settings.PAYSTACK_TEST_API_KEY)
        response = transaction.charge(auth_code=auth_code, email=email, amount=amount, reference='123456789')

        if response[0]:
            return Response({'message': 'Payment successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Payment failed'}, status=status.HTTP_400_BAD_REQUEST)

book_order = BookOrder.as_view()
 
# Create your views here.
