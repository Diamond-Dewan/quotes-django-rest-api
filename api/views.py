# from django.shortcuts import render
from rest_framework import generics 

from quote.models import Quote, Category

from .serializers import QuoteSerializer
from .serializers import CategorySerializer

# Create your views here.
class QuoteApiView(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

class CategoryApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer