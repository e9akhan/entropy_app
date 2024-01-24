from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UpdateUserForm(forms.ModelForm):
    """
        User form.
    """

    class Meta:
        """
            Meta class for User form.
        """

        model = User
        fields = ('email', 'first_name', 'last_name')

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UserForm(UserCreationForm):
    """
        User form.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            if key=='admin':
                continue
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        """
            Meta class for User form.
        """

        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    admin = forms.BooleanField(required=False)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_superuser = self.cleaned_data['admin']

        if commit:
            user.save()
        return user
        

class UserAuthenticationForm(AuthenticationForm):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

