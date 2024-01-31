"""
    Module name :- views
"""

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from inventory.forms import RecordForm, NomenclatureForm, DepartmentForm, AssignItemForm
from inventory.models import NomenclatureModel, RecordModel, Department, AssignItemModel


# Create your views here.
@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class ListNomeclature(ListView):
    """
    List Item.
    """

    model = NomenclatureModel
    template_name = "inventory/list_nomenclatures.html"
    paginate_by = 8
    context_object_name = "nomenclatures"


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class ListRecords(ListView):
    """
    List inventories.
    """

    template_name = "inventory/list_records.html"
    paginate_by = 8
    context_object_name = "records"

    def get_queryset(self):
        return RecordModel.objects.all()[::-1]


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class ListItems(ListView):
    """
    List Commodities.
    """

    template_name = "inventory/list_items.html"
    paginate_by = 8
    context_object_name = "items"

    def get_queryset(self):
        return AssignItemModel.objects.all()[::-1]



@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class ListDepartment(ListView):
    """
        List Department.
    """
    template_name = "inventory/list_department.html"
    paginate_by = 8
    context_object_name = "departments"

    def get_queryset(self):
        return Department.objects.all()[::-1]


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class CreateNomenclature(SuccessMessageMixin, CreateView):
    """
    Create Nomenclature.
    """

    template_name = "inventory/add_nomenclature.html"
    success_url = reverse_lazy("inventory:nomenclatures")
    form_class = NomenclatureForm
    success_message = "Nomenclature Added."


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class CreateRecord(SuccessMessageMixin, CreateView):
    """
    Create record.
    """

    template_name = "inventory/add_record.html"
    form_class = RecordForm
    success_message = "Added record."

    def get_success_url(self) -> str:
        return reverse_lazy("inventory:records")


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class CreateAssignedItem(SuccessMessageMixin, CreateView):
    """
    Create Assigned Item.
    """

    model = AssignItemModel
    template_name = "inventory/add_assign_item.html"
    form_class = AssignItemForm
    success_message = "Item assigned."
    success_url = reverse_lazy("inventory:list-items")

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["departments"] = Department.objects.all()
        context["nomenclatures"] = NomenclatureModel.objects.all()
        return context


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class CreateDepartment(SuccessMessageMixin, CreateView):
    """
        Create department.
    """
    model = Department
    template_name = "inventory/add_department.html"
    form_class = DepartmentForm
    success_url = reverse_lazy("inventory:departments")
    success_message = "Department Created."


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class UpdateNomenclature(SuccessMessageMixin, UpdateView):
    """
    Update Nomenclature.
    """

    model = NomenclatureModel
    template_name = "inventory/update_nomenclature.html"
    form_class = NomenclatureForm
    success_url = reverse_lazy("inventory:nomencaltures")
    success_message = "Nomenclature Updated"

    def get(self, request, *args, **kwargs):
        try:
            self.get_object()
        except NomenclatureModel.DoesNotExist:
            messages.info(request, "Nomenclature does not exists.")
            return redirect("inventory:nomenclatures")
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return NomenclatureModel.objects.get(name=self.kwargs["nomenclature"])


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class UpdateAssignedItem(SuccessMessageMixin, UpdateView):
    """
    Update Assigned Item.
    """

    model = AssignItemModel
    template_name = "inventory/update_assign_item.html"
    success_message = "Assign Item Updated"
    form_class = AssignItemForm
    success_url = reverse_lazy("inventory:list-items")
    context_object_name = "item"

    def get(self, request, *args, **kwargs):
        try:
            self.get_object()
        except AssignItemModel.DoesNotExist:
            messages.info(request, "Assign item does not exists.")
            return redirect("inventory:list-items")
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["departments"] = Department.objects.all()
        context["nomenclatures"] = NomenclatureModel.objects.all()
        return context


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class UpdateRecord(SuccessMessageMixin, UpdateView):
    """
    Update Record.
    """

    model = RecordModel
    template_name = "inventory/update_record.html"
    form_class = RecordForm
    success_message = "Record Updated"

    def get(self, request, *args, **kwargs):
        try:
            self.get_object()
        except RecordModel.DoesNotExist:
            messages.info(request, "Record does not exists.")
            return redirect("inventory:records")
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy("inventory:records")


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class UpdateDepartment(SuccessMessageMixin, UpdateView):
    """
    Update Department.
    """

    model = Department
    template_name = "inventory/update_department.html"
    form_class = DepartmentForm
    success_url = reverse_lazy("inventory:departments")
    success_message = "Department updated."

    def get(self, request, *args, **kwargs):
        try:
            self.get_object()
        except Department.DoesNotExist:
            messages.info(request, "Department does not exists.")
            return redirect("inventory:departments")

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return Department.objects.get(name=self.kwargs["name"])


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class DeleteNomenclature(SuccessMessageMixin, DeleteView):
    """
    Delete Item.
    """

    template_name = "inventory/delete_nomenclature.html"
    model = NomenclatureModel
    context_object_name = "item"
    success_message = "Nomenclature Deleted."
    success_url = reverse_lazy("inventory:nomenclatures")

    def get(self, request, *args, **kwargs):
        try:
            self.get_object()
        except NomenclatureModel.DoesNotExist:
            messages.info(request, "Nomenclature does not exists.")
            return redirect("inventory:nomenclatures")
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return NomenclatureModel.objects.get(name=self.kwargs["nomenclature"])


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class DeleteRecord(SuccessMessageMixin, DeleteView):
    """
    Delete Record.
    """

    template_name = "inventory/delete_record.html"
    model = RecordModel
    context_object_name = "item"
    success_message = "Record Deleted."

    def get(self, request, *args, **kwargs):
        try:
            self.get_object()
        except RecordModel.DoesNotExist:
            messages.info(request, "Record does not exists.")
            return redirect("inventory:records")
        return super().get(request, *args, **kwargs)

    def get_success_url(self) -> str:
        return reverse_lazy("inventory:records")


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class DeleteAssignItem(SuccessMessageMixin, DeleteView):
    """
    Delete assign item.
    """

    template_name = "inventory/delete_assign_item.html"
    model = AssignItemModel
    context_object_name = "item"
    success_message = "Assigned Item Deleted."
    success_url = reverse_lazy("inventory:list-items")

    def get(self, request, *args, **kwargs):
        try:
            self.get_object()
        except AssignItemModel.DoesNotExist:
            messages.info(request, "Assigned Item does not exists.")
            return redirect("inventory:list-items")

        return super().get(request, *args, **kwargs)


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class DeleteDepartment(SuccessMessageMixin, DeleteView):
    """
    Delete Department.
    """

    template_name = "inventory/delete_department.html"
    context_object_name = "item"
    success_url = reverse_lazy("inventory:departments")
    success_message = "Department Deleted."

    def get(self, request, *args, **kwargs):
        try:
            self.get_object()
        except:
            messages.info(request, "Department does not exist.")
            return redirect("inventory:departments")

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return Department.objects.get(name=self.kwargs["name"])


class Alerts(ListView):
    """
    Alert system.
    """

    template_name = "inventory/alerts.html"
    paginate_by = 8
    context_object_name = "alerts"

    def get_queryset(self):
        return [
            item
            for item in NomenclatureModel.objects.all()
            if item.get_remaining_items <= 5
        ]


class ItemSearch(ListView):
    """
    Search Commodity.
    """

    template_name = "inventory/list_items.html"
    paginate_by = 8
    context_object_name = "items"

    def get_queryset(self):
        search = self.request.GET["search"]

        return AssignItemModel.objects.filter(
            Q(item_id__icontains=search)
            | Q(assign_to__icontains=search)
            | Q(department__name__icontains=search)
            | Q(status__icontains=search)
            | Q(functionality__icontains=search)
            | Q(nomenclature__name__icontains=search)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search"] = self.request.GET["search"]
        return context


class NomenclatureSearch(ListView):
    """
    Nomenclature search.
    """

    template_name = "inventory/list_nomenclatures.html"
    paginate_by = 8
    context_object_name = "nomenclatures"

    def get_queryset(self):
        search = self.request.GET["search"]

        return NomenclatureModel.objects.filter(Q(name__icontains=search))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search"] = self.request.GET["search"]
        return context


class RecordSearch(ListView):
    """
    Search record.
    """

    template_name = "inventory/list_records.html"
    paginate_by = 8
    context_object_name = "records"

    def get_queryset(self):
        search = self.request.GET["search"]

        return RecordModel.objects.filter(
            Q(quantity__icontains=search)
            | Q(price__icontains=search)
            | Q(buy_date__icontains=search)
            | Q(nomenclature__name__icontains=search)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search"] = self.request.GET["search"]
        return context


class DepartmentSearch(ListView):
    """
    Search Department.
    """

    template_name = "inventory/list_department.html"
    paginate_by = 8
    context_object_name = "department"

    def get_queryset(self):
        search = self.request.GET["search"]

        return Department.objects.filter(Q(name__icontains=search))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search"] = self.request.GET["search"]
        return context


def get_id_for_nomenclature(request):
    """
        Give ids.
    """
    nomenclature = request.GET["nomenclature"]
    print(nomenclature)
    nomenclature_ids = NomenclatureModel.objects.get(name=nomenclature).generate_id
    return render(request, "inventory/display_id.html", {"ids": nomenclature_ids})
