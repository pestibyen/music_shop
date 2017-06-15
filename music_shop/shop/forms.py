from django import forms


class RegistrationForm(forms.Form):
    firstname = forms.CharField(label='Your name', max_length=20,
                                help_text='Letters only, max length = 20')
    lastname = forms.CharField(label='Last name', max_length=30,
                               help_text='Letters only, max length = 30')
    username = forms.CharField(label='User name', max_length=20,
                               help_text='Only letters, numbers, underscores or hyphens, max length = 20')
    password = forms.CharField(label='Password', max_length=20)
    email = forms.EmailField(label='E-mail', max_length=40)
    phone = forms.CharField(label='Phone', max_length=13,
                            help_text='+375xxxxxxxxx')
    address = forms.CharField(label='Address', max_length=300)
