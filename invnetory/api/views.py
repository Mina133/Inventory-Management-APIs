from django.shortcuts import render
from .serializers import itemsSerializer, categorySerializer
from rest_framework import viewsets
from .models import Items, Categories
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import decorators
from django.db import models
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.dispatch import receiver
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

class itemsListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Items.objects.all()
    serializer_class = itemsSerializer


class categoryListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Categories.objects.all()
    serializer_class = categorySerializer

class ItemDetailsUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Items.objects.all()
    serializer_class = itemsSerializer

class CategoryDetailsUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Categories.objects.all()
    serializer_class = categorySerializer


# Custom Endpoints
@api_view(['GET'])
def inventory_report(request):
    items = Items.objects.all()
    total_value = sum(item.Quantity * item.Price for item in items)
    low_stock_items = items.filter(Quantity=models.F('low_stock_threshold')).count()
    response = {
        "total_value": total_value,
        "low_stock_items": low_stock_items,
    }
    return Response(response)

@api_view(['GET'])
def get_item_by_barcode(request, barcode):
    try:
        item = Items.objects.get(barcode=barcode)
        serializer = itemsSerializer(item)
        return Response(serializer.data)
    except Items.DoesNotExist:
        return Response({"error": "Item not found"}, status=404)

@api_view(['GET'])
def reorder_suggestions(request):
    low_stock_items = Items.objects.filter(quantity__lt=models.F('low_stock_threshold'))
    serializer = itemsSerializer(low_stock_items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def inventory_levels(request):
    category = request.query_params.get('category', None)
    price_min = request.query_params.get('price_min', None)
    price_max = request.query_params.get('price_max', None)
    low_stock = request.query_params.get('low_stock', None)

    queryset = Items.objects.all()

    if category:
        queryset = queryset.filter(category__name=category)
    if price_min:
        queryset = queryset.filter(price__gte=price_min)
    if price_max:
        queryset = queryset.filter(price__lte=price_max)
    if low_stock:
        queryset = queryset.filter(quantity__lt=models.F('low_stock_threshold'))

    data = queryset.values('Name', 'Quantity', 'Price', 'Category')
    return Response(data)

# Signal for Low Stock Alerts
@receiver(post_save, sender=Items)
def check_low_stock(sender, instance, **kwargs):
    if instance.Quantity < instance.low_stock_threshold:
        send_mail(
            subject="Low Stock Alert",
            message=f"Item {instance.name} is low on stock. Only {instance.quantity} left!",
            from_email="admin@inventory.com",
            recipient_list=[instance.user.email],
        )
