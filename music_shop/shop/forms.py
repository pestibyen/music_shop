from django import forms
from django.conf import settings
from .models import SubCategory
from django.core import validators


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


class AddingProductForm(forms.Form):
    name = forms.CharField(max_length=50)
    manufacturer = forms.CharField(max_length=40, required=False)
    price = forms.DecimalField(max_digits=8, decimal_places=2, validators=[validators.MinValueValidator(0)])
    subcategory = forms.ModelChoiceField(queryset=SubCategory.objects.all())
    description = forms.CharField(max_length=1000, required=False)

    FORMATS = '\.jpg|\.jpeg|.png|\.gif'
    photo1 = forms.FilePathField(path=settings.MEDIA_ROOT, recursive=True,
                                 match=FORMATS)
    photo2 = forms.FilePathField(path=settings.MEDIA_ROOT, recursive=True,
                                 match=FORMATS, required=False)
    photo3 = forms.FilePathField(path=settings.MEDIA_ROOT, recursive=True,
                                 match=FORMATS, required=False)
    photo4 = forms.FilePathField(path=settings.MEDIA_ROOT, recursive=True,
                                 match=FORMATS, required=False)
    photo5 = forms.FilePathField(path=settings.MEDIA_ROOT, recursive=True,
                                 match=FORMATS, required=False)


