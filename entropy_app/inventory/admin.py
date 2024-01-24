from django.contrib import admin
from inventory.models import InventoryModel, ItemModel, Department, CommodityModel

# Register your models here.
@admin.register(InventoryModel)
class InventoryAdmin(admin.ModelAdmin):
    """
        Inventory for admin panel.
    """
    list_display = ['id', 'price', 'current_price', 'quantity', 'buy_date']


@admin.register(ItemModel)
class ItemAdmin(admin.ModelAdmin):
    """
        Item for admin panel.
    """
    list_display = ['name', 'depreciation_percent']


@admin.register(CommodityModel)
class CommodityAdmin(admin.ModelAdmin):
    """
        Commodity for admin panel.
    """
    list_display = ['id', 'assign_to', 'department', 'inventory', 'status']


admin.site.register(Department)
