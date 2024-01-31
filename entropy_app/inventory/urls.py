"""
    Module name :- urls
"""

from django.urls import path
from inventory.views import (
    ListNomeclature,
    ListRecords,
    ListDepartment,
    CreateNomenclature,
    CreateRecord,
    CreateDepartment,
    CreateAssignedItem,
    UpdateNomenclature,
    UpdateRecord,
    UpdateDepartment,
    UpdateAssignedItem,
    DeleteNomenclature,
    DeleteRecord,
    DeleteDepartment,
    DeleteAssignItem,
    NomenclatureSearch,
    RecordSearch,
    DepartmentSearch,
    ItemSearch,
    ListItems,
    get_id_for_nomenclature,
    Alerts,
)


app_name = "inventory"

urlpatterns = [
    path("", ListNomeclature.as_view(), name="nomenclatures"),
    path("records/", ListRecords.as_view(), name="records"),
    path("departments/", ListDepartment.as_view(), name="departments"),
    path("all_items/", ListItems.as_view(), name="list-items"),
    path("add-nomenclature/", CreateNomenclature.as_view(), name="add-nomenclature"),
    path("add-record/", CreateRecord.as_view(), name="add-record"),
    path("add-department/", CreateDepartment.as_view(), name="add-department"),
    path("add-assign-item/", CreateAssignedItem.as_view(), name="add-assign-item"),
    path(
        "update-nomenclature/<str:nomenclature>/",
        UpdateNomenclature.as_view(),
        name="update-nomenclature",
    ),
    path("update-record/<int:pk>/", UpdateRecord.as_view(), name="update-record"),
    path(
        "update-department/<str:name>/",
        UpdateDepartment.as_view(),
        name="update-department",
    ),
    path(
        "update-assign-item/<int:pk>/",
        UpdateAssignedItem.as_view(),
        name="update-assign-item",
    ),
    path(
        "delete-nomenclature/<str:nomenclature>/",
        DeleteNomenclature.as_view(),
        name="delete-nomenclature",
    ),
    path("delete-record/<int:pk>/", DeleteRecord.as_view(), name="delete-record"),
    path(
        "delete-department/<str:name>/",
        DeleteDepartment.as_view(),
        name="delete-department",
    ),
    path(
        "delete-assign-item/<int:pk>/",
        DeleteAssignItem.as_view(),
        name="delete-assign-item",
    ),
    path("alert/", Alerts.as_view(), name="alerts"),
    path("search/item", ItemSearch.as_view(), name="item_search"),
    path(
        "search/nomenclature", NomenclatureSearch.as_view(), name="nomenclature_search"
    ),
    path("search/record", RecordSearch.as_view(), name="record_search"),
    path("search/department", DepartmentSearch.as_view(), name="department_search"),
    path("get_ids/", get_id_for_nomenclature, name="get_ids"),
]
