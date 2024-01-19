from django.urls import path
from inventory.views import (ListInventory, CreateInventory, CreateCommodities, CreateCommodity,
    UpdateCommodity, UpdateCommodities, ListCommodities, ListCommodity, UpdateInventory, ListAllCommodities,
    DeleteInventory, DeleteCommodities, DeleteCommodity, NonFunctionalCommodity, FunctionalCommodity,
    DetailCommodities, DetailCommodity)


urlpatterns = [
    path('inventories/', ListInventory.as_view(), name='inventories'),
    path('all-commodities/', ListAllCommodities.as_view(), name='all-commodities'),

    path('<str:inventory_name>/commodities/', ListCommodities.as_view(), name='commodities'),
    path('<int:commodities_id>/commodity/', ListCommodity.as_view(), name='commodity'),

    path('add-inventory/', CreateInventory.as_view(), name='add-inventory'),
    path('add-commodities/', CreateCommodities.as_view(), name='add-commodities'),
    path('add-commodity/', CreateCommodity.as_view(), name='add-commodity'),

    path('update-inventory/<str:name>/', UpdateInventory.as_view(), name='update-inventory'),
    path('update-commodities/<int:pk>/', UpdateCommodities.as_view(), name='update-commodities'),
    path('update-commodity/<str:id>/', UpdateCommodity.as_view(), name='update-commodity'),

    path('detail-commodities/<int:pk>/', DetailCommodities.as_view(), name='detail-commodities'),
    path('detail-commodity/<str:id>/', DetailCommodity.as_view(), name='detail-commodity'),

    path('delete-inventory/<str:name>/', DeleteInventory.as_view(), name='delete-inventory'),
    path('delete-commodities/<int:pk>/', DeleteCommodities.as_view(), name='delete-commodities'),
    path('delete-commodity/<str:id>/', DeleteCommodity.as_view(), name='delete-commodity'),

    path('non-functional-items/', NonFunctionalCommodity.as_view(), name='non-functional-items'),
    path('functional-items/', FunctionalCommodity.as_view(), name='functional-items')
]