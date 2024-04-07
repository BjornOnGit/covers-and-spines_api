from rest_framework import generics, status
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer

class ReviewList(generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        reviews = self.get_queryset()
        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

review_upload = ReviewList.as_view()

# Create your views here.
