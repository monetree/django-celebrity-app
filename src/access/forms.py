from django import forms
from access.models import Register

class SignupForm(forms.Form):

    username = forms.CharField(label='', max_length=60,
        widget = forms.TextInput(
            attrs = {
                'class'       : 'text',
                'name'        : 'username',
                'placeholder' : 'Username',
                
            }
        )
    )

    email = forms.EmailField(label='', max_length=60,
        widget = forms.EmailInput(
            attrs = {
                'class'       : 'text email',
                'name'        : 'email',
                'placeholder' : 'Email',
        }
    )
)

    password = forms.CharField(label='', max_length=60,
        widget=forms.PasswordInput(
            attrs = {
                'class'       : 'text',
                'name'        : 'password',
                'placeholder' : 'Password',
        }
    )
)

    conform_password = forms.CharField(label='', max_length=60,
        widget=forms.PasswordInput(
            attrs = {
                'class'       : 'text w3lpass',
                'name'        : 'conform_password',
                'placeholder' : 'Confirm Password',
        }
    )
)

    class Meta():
        model  = Register
        fields = ['username','email','password']





