from .models import Product
from categories.models import SubCategory
from django.forms import ModelForm, CharField, DecimalField, ModelChoiceField, ImageField, Textarea
from django.core import validators


class AddingProductForm(ModelForm):
    name = CharField(max_length=50, required=True)
    manufacturer = CharField(max_length=40, required=False)
    price = DecimalField(max_digits=8, decimal_places=2, required=True,
                               validators=[validators.MinValueValidator(0)])
    subcategory = ModelChoiceField(queryset=SubCategory.objects.all())
    description = CharField(max_length=1000, required=False, widget=Textarea)

    FORMATS = '\.jpg|\.jpeg|\.png|\.gif'
    photo = ImageField()

    class Meta:
        model = Product
        fields = ('name', 'manufacturer', 'price', 'subcategory', 'description')
