from django import forms
from inventory.models import Inventory, Commodities, Commodity


class AddInventoryForm(forms.ModelForm):
    """
        Add Inventory
    """

    class Meta:
        """
            Meta class for inventory.
        """

        models = Inventory
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'form-control'}),
            'depreciation_percent': forms.TextInput(attrs={'form-control'})
        }


class CommoditiesForm(forms.ModelForm):
    """
        Add commodities.
    """

    class Meta:
        """
            Meta class for commodities.
        """

        models = Commodities
        fields = '__all__'
        exclude = ('current_price')

        widgets = {
            'inventory': forms.ModelChoiceField(Inventory, empty_label='Add Inventory'),
            'quantity': forms.TextInput(attrs = {'class': 'form-control'}),
            'buy_date': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'})
        }

        abstract = True


class AddCommoditiesForm(CommoditiesForm):
    """
        Add commodities.
    """

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.current_price = instance.price
        if commit:
            instance.save()
        return instance
    

class UpdateCommoditiesForm(CommoditiesForm):
    pass


class CommodityForm(forms.ModelForm):
    """
        Commodity Form.
    """

    class Meta:
        """
            Meta class for commodity form.
        """

        models = Commodity
        fields = '__all__'

        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'commodity_name': forms.TextInput(attrs={'class': 'form-control'}),
            'assign_to': forms.TextInput(attrs={'class': 'form-control'})
        }
