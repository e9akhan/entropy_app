from django.urls import path
from inventory.views import (ListInventories, CreateInventory, CreateItem, CreateCommodity,
    UpdateCommodity, UpdateItem, ListCommodity, UpdateInventory, ListItem, ListInventoryCommodity,
    DeleteInventory, DeleteItem, DeleteCommodity, NonFunctionalCommodity, FunctionalCommodity,
    Alerts, CommoditySearch, ItemSearch, InventorySearch, ListDepartment, CreateDepartment,
    UpdateDepartment, DeleteDepartment, DepartmentSearch)
from inventory.api.views import (inventories_api, inventories_api_with_pk, items_api, items_api_with_name,
                       department_api, department_api_with_name, commodity_api, commodity_api_with_id)


urlpatterns = [
    path('api/items/', items_api),
    path('api/items/<str:name>/', items_api_with_name),

    path('api/inventories/', inventories_api),
    path('api/inventories/<int:pk>/', inventories_api_with_pk),

    path('api/departments/', department_api),
    path('api/departments/<str:name>', department_api_with_name),

    path('api/commodity/', commodity_api),
    path('api/commodity/<str:id>/', commodity_api_with_id),

    path('items/', ListItem.as_view(), name='items'),
    path('inventories/', ListInventories.as_view(), name='inventories'),
    path('departments/', ListDepartment.as_view(), name='departments'),
    path('<str:item>/commodity/', ListCommodity.as_view(), name='commodity'),
    path('inventories/<int:id>/commodity/', ListInventoryCommodity.as_view(), name='commodity'),

    path('add-item/', CreateItem.as_view(), name='add-item'),
    path('add-inventory/', CreateInventory.as_view(), name='add-inventory'),
    path('add-department/', CreateDepartment.as_view(), name='add-department'),
    path('add-commodity/', CreateCommodity.as_view(), name='add-commodity'),

    path('update-item/<str:item>/', UpdateItem.as_view(), name='update-item'),
    path('update-inventory/<int:pk>/', UpdateInventory.as_view(), name='update-inventory'),
    path('update-department/<str:name>/', UpdateDepartment.as_view(), name='update-department'),
    path('update-commodity/<str:id>/', UpdateCommodity.as_view(), name='update-commodity'),

    path('delete-item/<str:item>/', DeleteItem.as_view(), name='delete-item'),
    path('delete-inventory/<int:pk>/', DeleteInventory.as_view(), name='delete-inventory'),
    path('delete-department/<str:name>/', DeleteDepartment.as_view(), name='delete-department'),
    path('delete-commodity/<str:id>/', DeleteCommodity.as_view(), name='delete-commodity'),

    path('non-functional-items/', NonFunctionalCommodity.as_view(), name='non-functional-items'),
    path('functional-items/', FunctionalCommodity.as_view(), name='functional-items'),
    path('alert/', Alerts.as_view(), name='alerts'),

    path('search/commodity', CommoditySearch.as_view(), name='commodity_search'),
    path('search/item', ItemSearch.as_view(), name='item_search'),
    path('search/inventory', InventorySearch.as_view(), name='inventory_search'),
    path('search/department', DepartmentSearch.as_view(), name='department_search'),
]