"""
URL configuration for invnetory project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import itemsListCreateView, categoryListCreateView, ItemDetailsUpdateDestroyView, CategoryDetailsUpdateDestroyView, inventory_levels, inventory_report, reorder_suggestions, get_item_by_barcode, StoresListCreateView, StoreDetailsUpdateDestroyView

router = DefaultRouter()
router.register(r'items', itemsListCreateView)
router.register(r'category', categoryListCreateView)
router.register(r'stores', StoresListCreateView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/item/', itemsListCreateView.as_view(), name='item-list-create'),  # List and Create
    path('api/item/<int:pk>/', ItemDetailsUpdateDestroyView.as_view(), name='item-detail'),  # Retrieve, Update, Delete

    # Category CRUD operations
    path('api/category/', categoryListCreateView.as_view(), name='category-list-create'),  # List and Create
    path('api/category/<int:pk>/', CategoryDetailsUpdateDestroyView.as_view(), name='category-detail'),  # Retrieve, Update, Delete

    path('api/item/level/' , inventory_levels, name='quantity-list'), 
    path('api/item/report/', inventory_report, name='inventory-report'),

    path('api/stores/', StoresListCreateView.as_view() , name='Stores'),
    path('api/stores/<int:pk>/', StoreDetailsUpdateDestroyView.as_view(), name='store-detail'),  # Retrieve, Update, Delete

    
]