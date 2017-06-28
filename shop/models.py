from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13, default='', blank=True,
                             help_text='+375xxxxxxxxx',
                             validators=[validators.RegexValidator(regex='^\+[0-9]{12}$')])

    addresslist = models.CharField(verbose_name='Address',
                                   max_length=300, default='', blank=True,
                                   validators=[validators.int_list_validator(sep=',')])

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return '{}'.format(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(default='', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class SubCategory(models.Model):
    name = models.CharField(max_length=30, unique=True)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'


class Photo(models.Model):
    filename = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.filename

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'


class Product(models.Model):
    name = models.CharField(max_length=50, default='')
    manufacturer = models.CharField(max_length=40, default='', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # photo = models.CharField(validators=[validators.int_list_validator(sep=',')],
    #                         max_length=300, blank=True)  # список фоток конкретного продукта, т.е.: список id из таблицы Photo
    photo = models.ImageField(upload_to='product/', blank=True)
    description = models.TextField(default='', blank=True)
    subcategory = models.ForeignKey(SubCategory)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Address(models.Model):
    '''
        Сюда попадает адрес из формы оформления заказа и получает id.
        Этот id сразу же добавляется в Client.addresslist
    '''
    address = models.CharField(max_length=200, unique=True)

    def __str__(self):
        if len(str(self.address)) > 13:
            return '{}...'.format(self.address[:13])
        else:
            return self.address

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'


class Order(models.Model):
    user = models.ForeignKey(User)
    orderstartdate = models.DateTimeField(auto_now_add=True)
    orderenddate = models.DateTimeField(auto_now=True)

    ORDER_OPEN = 'Open'
    ORDER_DONE = 'Done'
    ORDER_CANCELED = 'Canceled'

    options = (
        (ORDER_OPEN, 'Open'),
        (ORDER_DONE, 'Done'),
        (ORDER_CANCELED, 'Canceled'),
    )
    status = models.CharField(max_length=14, choices=options,
                              default=ORDER_OPEN)

    # При изменении Order.status на Done или Canceled автоматически
    # расчитывается сумма всего заказа и сохраняется в ordercost.
    # Реализовано с помощь Trigger Function SAVECOST() в БД.
    ordercost = models.DecimalField(max_digits=8, decimal_places=2,
                                    default=0, editable=False)

    def __str__(self):
        if self.status == 'Open':
            return '{0.id}: {0.status}'.format(self)
        else:
            return '{0.id}: {0.status} = {0.ordercost}'.format(self)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return '{0.id}: {1.name} x {2.quantity}'.format(self.order, self.product, self)

    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'


class News(models.Model):
    newsheader = models.CharField(max_length=50)
    newstext = models.TextField(default='')
    newsdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.newsheader

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
