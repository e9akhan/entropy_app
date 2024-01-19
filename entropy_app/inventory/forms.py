from django import forms
from inventory.models import InventoryModel, CommoditiesModel, CommodityModel, Department


class InventoryForm(forms.ModelForm):
    """
        Add Inventory
    """

    class Meta:
        """
            Meta class for inventory.
        """

        model = InventoryModel
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'depreciation_percent': forms.TextInput(attrs={'class': 'form-control'})
        }


class CommoditiesForm(forms.ModelForm):
    """
        Commodities.
    """

    inventory = forms.ModelChoiceField(queryset = InventoryModel.objects.all(), empty_label='Add Inventory name')
    department = forms.ModelChoiceField(queryset = Department.objects.all(), empty_label='Add Department')

    inventory.widget.attrs.update({'class': 'form-control'})
    department.widget.attrs.update({'class': 'form-control'})

    class Meta:
        """
            Meta class for commodities.
        """

        model = CommoditiesModel
        fields = '__all__'
        exclude = ('current_price', 'total_assigned')

        widgets = {
            'quantity': forms.TextInput(attrs = {'class': 'form-control'}),
            'buy_date': forms.DateInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }


class AddCommoditiesForm(CommoditiesForm):
    """
        Add commodities.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.current_price = instance.price
        if commit:
            instance.save()
        return instance
    

class UpdateCommoditiesForm(CommoditiesForm):
    pass


class CommodityForm(forms.ModelForm):
    commodity_name = forms.ModelChoiceField(queryset = CommoditiesModel.objects.all(), empty_label='Add Commodity name')
    commodity_name.widget.attrs.update({'class': 'form-control'})
    """
        Commodity Form.
    """

    class Meta:
        """
            Meta class for commodity form.
        """

        model = CommodityModel
        fields = '__all__'

        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'assign_to': forms.TextInput(attrs={'class': 'form-control'})
        }
