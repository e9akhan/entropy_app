from django import forms
from inventory.models import NomenclatureModel, RecordModel, Department, AssignItemModel


class NomenclatureForm(forms.ModelForm):
    """
    Add Nomenclature
    """

    class Meta:
        """
        Meta class for nomenclature.
        """

        model = NomenclatureModel
        fields = ("name",)

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }


class RecordForm(forms.ModelForm):
    """
    Record Form.
    """

    nomenclature = forms.ModelChoiceField(
        queryset=NomenclatureModel.objects.all(), empty_label="Add Nomenclature"
    )
    nomenclature.widget.attrs.update({"class": "form-select"})

    class Meta:
        """
        Meta class for records.
        """

        model = RecordModel
        fields = "__all__"

        widgets = {
            "quantity": forms.TextInput(attrs={"class": "form-control"}),
            "buy_date": forms.DateInput(attrs={"class": "form-control"}),
            "price": forms.TextInput(attrs={"class": "form-control"}),
        }


class AssignItemForm(forms.ModelForm):
    """
    Assign Item Form.
    """

    nomenclature = forms.ModelChoiceField(
        queryset=NomenclatureModel.objects.all(), empty_label="Add Nomenclature"
    )
    nomenclature.widget.attrs.update({"class": "form-select"})

    department = forms.ModelChoiceField(
        queryset=Department.objects.all(), empty_label="Add Department"
    )
    department.widget.attrs.update({"class": "form-select"})

    class Meta:
        """
        Meta class for assign item form.
        """

        model = AssignItemModel
        fields = "__all__"

        widgets = {
            "assign_to": forms.TextInput(attrs={"class": "form-control"}),
            "item_id": forms.Select(attrs={"class": "form-select"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "functionality": forms.Select(attrs={"class": "form-select"}),
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
        fields = "__all__"

        widgets = {"name": forms.TextInput(attrs={"class": "form-control"})}
