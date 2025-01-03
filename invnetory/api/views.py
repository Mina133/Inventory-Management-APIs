from django.shortcuts import render
from .serializers import itemsSerializer, categorySerializer
from rest_framework import viewsets
from .models import Items, Categories
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
class itemsListCreateView(ListCreateAPIView):
    queryset = Items.objects.all()
    serializer_class = itemsSerializer

class categoryListCreateView(ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = categorySerializer

class ItemDetailsUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Items.objects.all()
    serializer_class = itemsSerializer

class CategoryDetailsUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = categorySerializer