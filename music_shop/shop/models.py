from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(default='', blank=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=30, unique=True)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name


class Photo(models.Model):
    filename = models.CharField(help_text='Use the following format: image002.jpg or gitars/gitara042.png',
                             max_length=200, unique=True)

    def __str__(self):
        return self.filename


class Product(models.Model):
    name = models.CharField(max_length=50, default='')
    manufacturer = models.CharField(max_length=40, default='', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.CharField(max_length=300, blank=True)  # список фоток конкретного продукта, т.е.: список id из таблицы Photo
    description = models.TextField(default='', blank=True)
    subcategory = models.ForeignKey(SubCategory)

    def __str__(self):
        return self.name


class Address(models.Model):
    '''
        Сюда попадает адрес из формы (регистрации или доставки) и получает id.
        Этот id сразу же добавляется в Client.addresslist (реализовано для
        регистрации в представлении registration, для доставки - не реализовано)
    '''
    address = models.CharField(max_length=300, default='', blank=True, unique=True)

    def __str__(self):
        if len(str(self.address)) > 13:
            return '{}...'.format(self.address[:13])
        else:
            return self.address


class Client(models.Model):
    firstname = models.CharField(help_text='Letters only, max length = 20',
                                 max_length=20, default='')
    lastname = models.CharField(help_text='Letters only, max length = 30',
                                max_length=30, default='')
    username = models.CharField(help_text='Only letters, numbers, underscores or hyphens, max length = 20',
                                max_length=20, default='')
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    phone = models.CharField(help_text='+375xxxxxxxxx',
                             max_length=13, default='', blank=True)
    addresslist = models.CharField(max_length=300, blank=True)  # список адресов юзера, т.е.: список id из таблицы Address

    def __str__(self):
        return self.username


class Order(models.Model):
    client = models.ForeignKey(Client)
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


class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return '{0.id}: {1.name} x {2.quantity}'.format(self.order, self.product, self)


class New(models.Model):
    newsheader = models.CharField(max_length=50)
    newstext = models.TextField(default='')
    newsdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.newsheader
