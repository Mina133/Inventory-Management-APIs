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
from user.views import CustomUserListCreateView, CustomUserCreateUpdateView, RoleListCreateView, RoleCreateUpdateView

router = DefaultRouter()
router.register(r'items', itemsListCreateView)
router.register(r'category', categoryListCreateView)
router.register(r'stores', StoresListCreateView)
router.register(r'users', CustomUserListCreateView)
router.register(r'roles', RoleListCreateView)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/item/', itemsListCreateView.as_view(), name='item-list-create'),  # List and Create
    path('api/item/<int:pk>/', ItemDetailsUpdateDestroyView.as_view(), name='item-detail'),  # Retrieve, Update, Delete
    path('api/item/level/' , inventory_levels, name='quantity-list'), 
    path('api/item/report/', inventory_report, name='inventory-report'),
    path('api/item/barcode/<str:barcode>/', get_item_by_barcode, name='item-barcode'),  # Retrieve by barcode
    path('api/item/reorder/', reorder_suggestions, name='reorder-suggestions'),  # Retrieve reorder suggestions

    # Category CRUD operations
    path('api/category/', categoryListCreateView.as_view(), name='category-list-create'),  # List and Create
    path('api/category/<int:pk>/', CategoryDetailsUpdateDestroyView.as_view(), name='category-detail'),  # Retrieve, Update, Delete

    path('api/stores/', StoresListCreateView.as_view() , name='Stores'),
    path('api/stores/<int:pk>/', StoreDetailsUpdateDestroyView.as_view(), name='store-detail'),  # Retrieve, Update, Delete

    path('api/users/', CustomUserListCreateView.as_view(), name='user-list-create'),  # List and Create
    path('api/users/<int:pk>/', CustomUserCreateUpdateView.as_view(), name='user-detail'),  # Retrieve, Update, Delete

    path('api/roles/', RoleListCreateView.as_view(), name='role-list-create'),  # List and Create
    path('api/roles/<int:pk>/', RoleCreateUpdateView.as_view(), name='role-detail'),  # Retrieve, Update, Delete

    
]