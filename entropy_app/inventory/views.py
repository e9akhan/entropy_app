from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from inventory.forms import AddCommoditiesForm, CommodityForm, InventoryForm, UpdateCommoditiesForm
from inventory.models import CommoditiesModel, CommodityModel, InventoryModel


# Create your views here.
class ListInventory(ListView):
    """
        List Inventory.
    """

    model = InventoryModel
    template_name = 'inventory/list_inventory.html'
    paginate_by = 10
    context_object_name = 'inventories'


class ListAllCommodities(ListView):
    """
        List all commodities.
    """

    model = CommoditiesModel
    template_name = 'inventory/list_commodities.html'
    paginate_by = 10
    context_object_name = 'commodities'


class ListCommodities(ListView):
    """
        List Commodities.
    """

    model = CommoditiesModel
    template_name = 'inventory/list_commodities.html'
    paginate_by = 10
    context_object_name = 'commodities'

    def get_queryset(self):
        return CommoditiesModel.objects.filter(inventory = self.kwargs['inventory_name'])


class ListCommodity(ListView):
    """
        List Commodities.
    """

    model = CommodityModel
    template_name = 'inventory/list_commodity.html'
    paginate_by = 10
    context_object_name = 'commodities'

    def get_queryset(self):
        return CommodityModel.objects.filter(commodity_name = self.kwargs['commodities_id'])


class FunctionalCommodity(ListView):
    model = CommodityModel
    template_name = 'inventory/item_status.html'
    paginate_by = 10
    context_object_name = 'commodities'

    def get_queryset(self):
        return CommodityModel.objects.filter(status = 'functional')


class NonFunctionalCommodity(ListView):
    model = CommodityModel
    template_name = 'inventory/item_status.html'
    paginate_by = 10
    context_object_name = 'commodities'

    def get_queryset(self):
        return CommodityModel.objects.filter(status = 'nonfunctional')


class Alerts(ListView):
    pass 


class CreateInventory(SuccessMessageMixin, CreateView):
    """
        Create Inventory.
    """

    template_name = 'inventory/add_inventory.html'
    success_url = reverse_lazy('list-inventory')
    form_class = InventoryForm
    success_message = 'Inventory Added.'


class CreateCommodities(SuccessMessageMixin, CreateView):
    """
        Create Commodities.
    """

    template_name = 'inventory/add_commodities.html'
    form_class = AddCommoditiesForm
    success_url = reverse_lazy('add-commodities')
    success_message = 'Added Commodities.'


class CreateCommodity(SuccessMessageMixin, CreateView):
    """
        Create Commodity.
    """

    template_name = 'inventory/add_commodity.html'
    form_class = CommodityForm
    success_url = reverse_lazy('add-commodity')
    success_message = 'Added Commodity.'

    def form_valid(self, form):
        instance = CommoditiesModel.objects.get(
            pk = form.cleaned_data['commodity_name'].pk
        )

        if instance.total_assigned == instance.quantity:
            messages.info(self.request, 'All commodity already assigned.')
            return render(self.request, 'add_commodity.html', {'form': form})

        return super().form_valid(form)


class UpdateInventory(SuccessMessageMixin, UpdateView):
    """
        Update Inventory.
    """

    model = InventoryModel
    template_name = 'inventory/update_inventory.html'
    form_class = InventoryForm
    success_url = reverse_lazy('inventories')
    success_message = 'Inventory Updated'

    def get(self, request, *args, **kwargs):
        try:
            self.get_object()
        except InventoryModel.DoesNotExist:
            messages.info(request, 'Commodity does not exists.')
            return redirect('inventories')

        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return InventoryModel.objects.get(name = self.kwargs['name'])


class UpdateCommodity(SuccessMessageMixin, UpdateView):
    """
        Update Commodity.
    """

    model = CommodityModel
    template_name = 'inventory/update_commodity.html'
    form_class = CommodityForm
    success_message = 'Commodity Updated'

    def get(self, request, *args, **kwargs):
        try:
            self.get_object()
        except CommodityModel.DoesNotExist:
            messages.info(request, 'Commodity does not exists.')
            return redirect(f'inventory/{kwargs.get("commodities_id")}/commodity/')

        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return CommodityModel.objects.get(id = self.kwargs['id'])
    
    def get_success_url(self, **kwargs):
        return redirect(f'inventory/{kwargs.get("commodities_id")}/commodity/')


class UpdateCommodities(SuccessMessageMixin, UpdateView):
    """
        Update Commodities.
    """

    model = CommoditiesModel
    template_name = 'inventory/update_commodity.html'
    form_class = UpdateCommoditiesForm
    success_message = 'Commodities Updated'

    def get(self, request, *args, **kwargs):
        try:
            self.get_object()
        except CommodityModel.DoesNotExist:
            messages.info(request, 'Commodity does not exists.')
            return redirect(f'inventory/{kwargs.get("inventory_name")}/commodities/')

        return super().get(request, *args, **kwargs)
    
    def get_success_url(self, **kwargs):
        return redirect(f'inventory/{kwargs.get("inventory_name")}/commodities/')


class DetailCommodities(DetailView):
    """
        Detail Commodities.
    """

    model = CommoditiesModel
    template_name = 'inventory/detail_commodities.html'
    context_object_name = 'commodities'

    def get(self, request, *args, **kwargs):
        try:
            self.get_object()
        except CommodityModel.DoesNotExist:
            messages.info(request, 'Commodity does not exists.')
            return redirect(f'inventory/{kwargs.get("inventory_name")}/commodities/')

        return super().get(request, *args, **kwargs)
    
    def get_success_url(self, **kwargs):
        return redirect(f'inventory/{kwargs.get("inventory_name")}/commodities/')


class DetailCommodity(DetailView):
    """
        Detail Commodity.
    """

    model = CommodityModel
    template_name = 'inventory/detail_commodity.html'
    context_object_name = 'commodity'

    def get(self, request, *args, **kwargs):
        try:
            self.get_object()
        except CommodityModel.DoesNotExist:
            messages.info(request, 'Commodity does not exists.')
            return redirect(f'inventory/{kwargs.get("commodities_id")}/commodity/')

        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return CommodityModel.objects.get(id = self.kwargs['id'])

    
class DeleteInventory(SuccessMessageMixin, DeleteView):
    """
        Delete Inventory.
    """

    template_name = "inventory/delete_inventory.html"
    model = InventoryModel
    context_object_name = 'item'
    success_message = 'Inventory Deleted.'

    def get(self, request, *args, **kwargs):
        try:
            self.get_object()
        except InventoryModel.DoesNotExist:
            messages.info(request, 'Commodity does not exists.')
            return redirect('inventories')

        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return InventoryModel.objects.get(name = self.kwargs['name'])

class DeleteCommodities(SuccessMessageMixin, DeleteView):
    """
        Delete Commodities.
    """

    template_name = "inventory/delete_commodities.html"
    model = CommoditiesModel
    context_object_name = 'item'
    success_message = 'Commodities Deleted.'

class DeleteCommodity(SuccessMessageMixin, DeleteView):
    """
        Delete Commodity.
    """

    template_name = "inventory/delete_commodity.html"
    model = CommodityModel
    context_object_name = 'item'
    success_message = 'Commodity Deleted.'

    def get(self, request, *args, **kwargs):
        try:
            self.get_object()
        except CommodityModel.DoesNotExist:
            messages.info(request, 'Commodity does not exists.')
            return redirect(f'inventory/{kwargs.get("commodities_id")}/commodity/')

        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return CommodityModel.objects.get(id = self.kwargs['id'])