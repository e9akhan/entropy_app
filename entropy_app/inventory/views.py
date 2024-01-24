from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from inventory.forms import AddInventoryForm, CommodityForm, UpdateInventoryForm, ItemForm, DepartmentForm
from inventory.models import ItemModel, CommodityModel, InventoryModel, ItemModel, Department


# Create your views here.
@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class ListItem(ListView):
    """
        List Item.
    """

    model = ItemModel
    template_name = 'inventory/list_items.html'
    paginate_by = 8
    context_object_name = 'items'


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class ListInventories(ListView):
    """
        List inventories.
    """

    template_name = 'inventory/list_inventories.html'
    paginate_by = 8
    context_object_name = 'inventories'

    def get_queryset(self):
        return InventoryModel.objects.all()[::-1]


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class ListCommodity(ListView):
    """
        List Commodities.
    """

    template_name = 'inventory/list_commodity.html'
    paginate_by = 8
    context_object_name = 'commodities'

    def get_queryset(self):
        return CommodityModel.objects.filter(item = self.kwargs['item'])[::-1]


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class ListInventoryCommodity(ListView):
    """
        List Inventory Commodities.
    """

    template_name = 'inventory/list_commodity.html'
    paginate_by = 8
    context_object_name = 'commodities'

    def get_queryset(self):
        return CommodityModel.objects.filter(inventory = self.kwargs['id'])[::-1]


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class ListDepartment(ListView):
    template_name = 'inventory/list_department.html'
    paginate_by = 8
    context_object_name = 'departments'

    def get_queryset(self):
        return Department.objects.all()[::-1]


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class FunctionalCommodity(ListView):
    model = CommodityModel
    template_name = 'inventory/item_status.html'
    paginate_by = 8
    context_object_name = 'commodities'

    def get_queryset(self):
        return CommodityModel.objects.filter(status = 'Functional')[::-1]


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class NonFunctionalCommodity(ListView):
    model = CommodityModel
    template_name = 'inventory/item_status.html'
    paginate_by = 8
    context_object_name = 'commodities'

    def get_queryset(self):
        return CommodityModel.objects.filter(status = 'Non-Functional')[::-1]


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class CreateItem(SuccessMessageMixin, CreateView):
    """
        Create Item.
    """

    template_name = 'inventory/add_item.html'
    success_url = reverse_lazy('items')
    form_class = ItemForm
    success_message = 'Item Added.'


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class CreateInventory(SuccessMessageMixin, CreateView):
    """
        Create Inventory.
    """

    template_name = 'inventory/add_inventory.html'
    form_class = AddInventoryForm
    success_message = 'Added Inventory.'

    def get_success_url(self) -> str:
        return reverse_lazy('inventories')


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class CreateCommodity(SuccessMessageMixin, CreateView):
    """
        Create Commodity.
    """

    template_name = 'inventory/add_commodity.html'
    form_class = CommodityForm
    success_message = 'Added Commodity.'

    def form_valid(self, form):
        inventory = InventoryModel.objects.get(id = form.cleaned_data['inventory'].id)

        if inventory.quantity <= inventory.get_assigned:
            messages.info(self.request, 'All inventories already assigned.')
            return render(self.request, 'inventory/add_commodity.html', {'form': form})
        
        instance = ItemModel.objects.get(
            name = inventory.item
        )

        if instance.get_assigned >= instance.get_quantity:
            messages.info(self.request, 'All items already assigned.')
            return render(self.request, 'inventory/add_commodity.html', {'form': form})

        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse_lazy('commodity', kwargs = {'item': self.object.item})


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class CreateDepartment(SuccessMessageMixin, CreateView):
    model = Department
    template_name = 'inventory/add_department.html'
    form_class = DepartmentForm
    success_url = reverse_lazy('departments')
    success_message = 'Department Created.'


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class UpdateItem(SuccessMessageMixin, UpdateView):
    """
        Update Item.
    """

    model = ItemModel
    template_name = 'inventory/update_item.html'
    form_class = ItemForm
    success_url = reverse_lazy('items')
    success_message = 'Item Updated'

    def get(self, request, *args, **kwargs):
        try:
            self.get_object()
        except ItemModel.DoesNotExist:
            messages.info(request, 'Item does not exists.')
            return redirect('items')
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return ItemModel.objects.get(name = self.kwargs['item'])


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
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
            return redirect('items')
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return CommodityModel.objects.get(id = self.kwargs['id'])
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('commodity', kwargs={'item': self.object.item})


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class UpdateInventory(SuccessMessageMixin, UpdateView):
    """
        Update Inventory.
    """

    model = InventoryModel
    template_name = 'inventory/update_inventory.html'
    form_class = UpdateInventoryForm
    success_message = 'Inventory Updated'

    def get(self, request, *args, **kwargs):
        try:
            self.get_object()
        except InventoryModel.DoesNotExist:
            messages.info(request, 'Inventory does not exists.')
            return redirect('inventories')
        return super().get(request, *args, **kwargs)
    
    def get_success_url(self):
        return reverse_lazy('inventories')


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class UpdateDepartment(SuccessMessageMixin, UpdateView):
    """
        Update Department.
    """

    model = Department
    template_name = 'inventory/update_department.html'
    form_class = DepartmentForm
    success_url = reverse_lazy('departments')
    success_message = 'Department updated.'

    def get(self, request, *args, **kwargs):
        try:
            self.get_object()
        except Department.DoesNotExist:
            messages.info(request, 'Department does not exists.')
            return redirect('departments')
        
        return super().get(request, *args, **kwargs)

    def get_object(self):
        return Department.objects.get(name = self.kwargs['name'])


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class DeleteItem(SuccessMessageMixin, DeleteView):
    """
        Delete Item.
    """

    template_name = "inventory/delete_item.html"
    model = ItemModel
    context_object_name = 'item'
    success_message = 'Item Deleted.'
    success_url = reverse_lazy('items')

    def get(self, request, *args, **kwargs):
        try:
            self.get_object()
        except ItemModel.DoesNotExist:
            messages.info(request, 'Item does not exists.')
            return redirect('items')
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return ItemModel.objects.get(name = self.kwargs['item'])


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
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
            messages.info(request, 'Inventory does not exists.')
            return redirect('inventories')
        return super().get(request, *args, **kwargs)

    def get_success_url(self) -> str:
        return reverse_lazy('inventories')


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
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
            return redirect('items')
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return CommodityModel.objects.get(id = self.kwargs['id'])
    
    def get_success_url(self) -> str:
        return reverse_lazy('commodity', kwargs = {'item': self.object.item})


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class DeleteDepartment(SuccessMessageMixin, DeleteView):
    """
        Delete Department.
    """

    template_name = 'inventory/delete_department.html'
    context_object_name = 'item'
    success_url = reverse_lazy('departments')
    success_message = 'Department Deleted.'

    def get(self, request, *args, **kwargs):
        try:
            self.get_object()
        except:
            messages.info(request, 'Department does not exist.')
            return redirect('departments')

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return Department.objects.get(name = self.kwargs['name'])


class Alerts(ListView):
    """
        Alert system.
    """
    template_name = 'inventory/alerts.html'
    paginate_by = 8
    context_object_name = 'alerts'

    def get_queryset(self):
        return [item.name for item in ItemModel.objects.all() if item.get_functional_items <= 5]


class CommoditySearch(ListView):
    """
        Seach Commodity.
    """
    template_name = 'inventory/list_commodity.html'
    paginate_by = 8
    context_object_name = 'commodities'

    def get_queryset(self):
        search = self.request.GET['search']

        return CommodityModel.objects.filter(
            Q(id__icontains = search) | Q(assign_to__icontains = search) |
            Q(item__name__icontains = search) | Q(department__name__icontains = search) |
            Q(status__icontains = search)
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET['search']
        return context


class ItemSearch(ListView):
    """
        Item search.
    """
    template_name = 'inventory/list_items.html'
    paginate_by = 8
    context_object_name = 'items'

    def get_queryset(self):
        search = self.request.GET['search']

        return ItemModel.objects.filter(
            Q(name__icontains = search) | Q(depreciation_percent__icontains = search)
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET['search']
        return context


class InventorySearch(ListView):
    """
        Search Inventory.
    """
    template_name = 'inventory/list_inventories.html'
    paginate_by = 8
    context_object_name = 'inventories'

    def get_queryset(self):
        search = self.request.GET['search']

        return InventoryModel.objects.filter(
            Q(quantity__icontains = search) | Q(price__icontains = search) |
            Q(current_price__icontains = search) | Q(buy_date__icontains = search) |
            Q(item__name__icontains = search)
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET['search']
        return context


class DepartmentSearch(ListView):
    """
        Search Department.
    """
    template_name = 'inventory/list_department.html'
    paginate_by = 8
    context_object_name = 'department'

    def get_queryset(self):
        search = self.request.GET['search']

        return Department.objects.filter(
            Q(name__icontains = search)
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET['search']
        return context