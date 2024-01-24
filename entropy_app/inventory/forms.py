from django import forms
from inventory.models import InventoryModel, ItemModel, CommodityModel, Department


class ItemForm(forms.ModelForm):
    """
        Add Inventory
    """

    class Meta:
        """
            Meta class for inventory.
        """

        model = ItemModel
        fields = ('name', 'depreciation_percent')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'depreciation_percent': forms.TextInput(attrs={'class': 'form-control'})
        }


class InventoryForm(forms.ModelForm):
    """
        Commodities.
    """

    item = forms.ModelChoiceField(queryset = ItemModel.objects.all(), empty_label='Add Inventory name')
    item.widget.attrs.update({'class': 'form-control'})

    class Meta:
        """
            Meta class for inventories.
        """

        model = InventoryModel
        fields = '__all__'
        exclude = ('current_price', 'total_assigned')

        widgets = {
            'quantity': forms.TextInput(attrs = {'class': 'form-control'}),
            'buy_date': forms.DateInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }


class AddInventoryForm(InventoryForm):
    """
        Add inventory.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.current_price = instance.price
        if commit:
            instance.save()
        return instance
    

class UpdateInventoryForm(InventoryForm):
    """
        Update Inventory Form.
    """
    pass


class CommodityForm(forms.ModelForm):
    """
        Commodity Form.
    """

    department = forms.ModelChoiceField(queryset = Department.objects.all(), empty_label='Add Department')
    inventory = forms.ModelChoiceField(queryset = InventoryModel.objects.all(), empty_label='Add Inventory name')

    inventory.widget.attrs.update({'class': 'form-control'})
    department.widget.attrs.update({'class': 'form-control'})

    class Meta:
        """
            Meta class for commodity form.
        """

        model = CommodityModel
        fields = '__all__'
        exclude = ('item',)

        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'assign_to': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }


class DepartmentForm(forms.ModelForm):
    """
        Department Form.
    """

    class Meta:
        """
            Meta class for department form.
        """

        model = Department
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }
