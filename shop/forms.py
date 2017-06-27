from django.forms import ModelForm, CharField, FilePathField, DecimalField, ModelChoiceField, PasswordInput, TextInput
from django.core.exceptions import NON_FIELD_ERRORS
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import password_validation
from django.core import validators
from .models import Product, SubCategory
from django.conf import settings


class RegistrationForm(ModelForm):
    username = CharField(label='', max_length=40, help_text='До 40 символов',
                         validators=[validators.EmailValidator(
                             message='Введите действительный адрес электронной почты.')],
                         widget=TextInput(
                             attrs={'class': 'form-control', 'placeholder': 'E-mail'}))
    password = CharField(label='', max_length=20,
                         help_text='От 8 до 20 символов',
                         validators=[password_validation.validate_password],
                         widget=PasswordInput(
                             attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    first_name = CharField(label='', max_length=20, required=True,
                           help_text='Только буквы, от 2 до 20 символов',
                           validators=[validators.RegexValidator(
                               regex='^[а-яА-ЯёЁa-zA-Z]{2,20}$',
                               message='Введите правильное имя.')],
                           widget=TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'Имя'}))

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name')
        error_messages = {
            NON_FIELD_ERRORS: {'unique_together': "%(model_name)s's %(field_labels)s are not unique.",}
        }


class LoginForm(AuthenticationForm):
    username = CharField(label='', max_length=40,
                         widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}))
    password = CharField(label='',
                         widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    error_messages = {
        'invalid_login': 'Введите правильный адрес электронной почты и пароль.',
        'inactive': 'This account is inactive.',
    }


class AddingProductForm(ModelForm):
    name = CharField(max_length=50, required=True)
    manufacturer = CharField(max_length=40, required=False)
    price = DecimalField(max_digits=8, decimal_places=2, required=True,
                               validators=[validators.MinValueValidator(0)])
    subcategory = ModelChoiceField(queryset=SubCategory.objects.all())
    description = CharField(max_length=1000, required=False)

    FORMATS = '\.jpg|\.jpeg|\.png|\.gif'
    photo1 = FilePathField(path=settings.MEDIA_ROOT, recursive=True,
                                 match=FORMATS)
    photo2 = FilePathField(path=settings.MEDIA_ROOT, recursive=True,
                                 match=FORMATS, required=False)
    photo3 = FilePathField(path=settings.MEDIA_ROOT, recursive=True,
                                 match=FORMATS, required=False)
    photo4 = FilePathField(path=settings.MEDIA_ROOT, recursive=True,
                                 match=FORMATS, required=False)
    photo5 = FilePathField(path=settings.MEDIA_ROOT, recursive=True,
                                 match=FORMATS, required=False)

    class Meta:
        model = Product
        fields = ('name', 'manufacturer', 'price', 'subcategory', 'description')
