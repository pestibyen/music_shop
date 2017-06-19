from django.forms import ModelForm, CharField, FilePathField, DecimalField, ModelChoiceField
from django.core.exceptions import NON_FIELD_ERRORS
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.core import validators
from .models import Product, SubCategory
from django.conf import settings


class RegistrationForm(ModelForm):
    username = CharField(label='Электронная почта', max_length=40,
                               validators=[validators.EmailValidator(
                                   message='Введите действительный адрес электронной почты.')])
    password = CharField(label='Пароль', max_length=20,
                               help_text='От 8 до 20 символов',
                               validators=[password_validation.validate_password])
    first_name = CharField(label='Имя', max_length=20, required=True,
                                help_text='Только буквы, от 2 до 20 символов',
                                validators=[validators.RegexValidator(regex='^[а-яА-ЯёЁa-zA-Z]{2,20}$')])

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name')
        error_messages = {
            NON_FIELD_ERRORS: {'unique_together': "%(model_name)s's %(field_labels)s are not unique.",}
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