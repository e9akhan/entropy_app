from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserForm(UserCreationForm):
    """
        User form.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        """
            Meta class for User form.
        """

        model = User
        fields = ('username', 'email')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }

# class LoginForm(forms.Form):
#     """
#         Login Form.
#     """

#     username = forms.CharField(max_length=20)
#     password = forms.CharField(
#         max_length=20,
#         widget=forms.PasswordInput,
#         help_text="Password must be of only 8 characters."
#     )

#     username.widget.attrs.update({'class': 'form-control'})
#     password.widget.attrs.update({'class': 'form-control'})


#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        

class UserAuthenticatioForm(AuthenticationForm):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

