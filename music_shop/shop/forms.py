from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from .models import SubCategory
from django.core import validators
from .models import Client


def validate_username(value):
    if Client.objects.filter(username=value):
        raise ValidationError('Пользователь с таким адресом электронной почты уже зарегистрирован.')


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Электронная почта', max_length=40,
                               validators=[validators.EmailValidator(
                                   message='Введите действительный адрес электронной почты.'), validate_username])

    password = forms.CharField(label='Пароль', max_length=20,
                               help_text='Латинские буквы, цифры, дефисы и подчёркивания, от 5 до 20 символов',
                               validators=[validators.RegexValidator(
                                   regex='^[A-Za-z0-9_-]{5,20}$')])

    firstname = forms.CharField(label='Имя', max_length=20,
                                help_text='Только буквы, от 2 до 20 символов',
                                validators=[validators.RegexValidator(regex='^[а-яА-ЯёЁa-zA-Z]{2,20}$')])

    # lastname = forms.CharField(label='Last name', max_length=30, required=False,
    #                            help_text='Только буквы, до 30 символов',
    #                            validators=[validators.RegexValidator(
    #                                regex='^[а-яА-ЯёЁa-zA-Z-]{0,30}$')])
    #
    # phone = forms.CharField(label='Phone', max_length=13, required=False,
    #                         help_text='+375xxxxxxxxx',
    #                         validators=[validators.RegexValidator(
    #                             regex='^\+[0-9]{12}$')])
    #
    # address = forms.CharField(label='Address', max_length=300, required=False,
    #                           help_text='Буквы, цифры, дефисы, пробелы, точки и запятые.',
    #                           validators=[validators.RegexValidator(
    #                               regex='^[A-Za-zа-яёЁА-Я0-9,\.\s-]*$')])


class AddingProductForm(forms.Form):
    name = forms.CharField(max_length=50)
    manufacturer = forms.CharField(max_length=40, required=False)
    price = forms.DecimalField(max_digits=8, decimal_places=2, validators=[validators.MinValueValidator(0)])
    subcategory = forms.ModelChoiceField(queryset=SubCategory.objects.all())
    description = forms.CharField(max_length=1000, required=False)

    FORMATS = '\.jpg|\.jpeg|\.png|\.gif'
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


