from django.contrib import admin
from inventory.models import NomenclatureModel, RecordModel, Department, AssignItemModel


# Register your models here.
@admin.register(RecordModel)
class RecordAdmin(admin.ModelAdmin):
    """
    record for admin panel.
    """

    list_display = ["id", "price", "quantity", "buy_date"]


@admin.register(NomenclatureModel)
class NomenclatureAdmin(admin.ModelAdmin):
    """
    Nomenclature for admin panel.
    """

    list_display = ["name"]


@admin.register(AssignItemModel)
class AssignItemAdmin(admin.ModelAdmin):
    """
    Commodity for admin panel.
    """

    list_display = [
        "id",
        "assign_to",
        "department",
        "nomenclature",
        "status",
        "functionality",
    ]


admin.site.register(Department)
