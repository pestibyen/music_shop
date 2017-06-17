from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from .models import SubCategory
from django.core import validators
from shop.models import Client


def validate_username(value):
    if Client.objects.filter(username=value):
        raise ValidationError('Такой Username уже занят, выбирите другой.')


class RegistrationForm(forms.Form):
    firstname = forms.CharField(label='Your name', max_length=20, required=False,
                                help_text='Только буквы, от 1 до 20 символов',
                                validators=[validators.RegexValidator(
                                    regex='^[а-яА-ЯёЁa-zA-Z]{1,20}$')])

    lastname = forms.CharField(label='Last name', max_length=30, required=False,
                               help_text='Только буквы, от 1 до 30 символов',
                               validators=[validators.RegexValidator(
                                   regex='^[а-яА-ЯёЁa-zA-Z-]{1,30}$')])

    username = forms.CharField(label='User name', max_length=20,
                               help_text='Буквы, цифры, дефисы и подчёркивания, от 3 до 20 символов',
                               validators=[validators.RegexValidator(regex='^[A-Za-z0-9_-]{3,20}$'), validate_username])

    password = forms.CharField(label='Password', max_length=20,
                               help_text='Строчные и прописные латинские буквы, цифры, дефисы и подчёркивания, от 5 до 20 символов',
                               validators=[validators.RegexValidator(
                                   regex='^[A-Za-z0-9_-]{5,20}$')])

    email = forms.EmailField(label='E-mail', max_length=40, required=False)

    phone = forms.CharField(label='Phone', max_length=13, required=False,
                            help_text='+375xxxxxxxxx',
                            validators=[validators.RegexValidator(
                                regex='^\+[0-9]{12}$')])

    address = forms.CharField(label='Address', max_length=300, required=False)


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


