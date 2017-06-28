from django.forms import ModelForm, CharField, PasswordInput, TextInput
from django.core.exceptions import NON_FIELD_ERRORS
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import password_validation
from django.core import validators

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
