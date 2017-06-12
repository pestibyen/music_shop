from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, default='')
    description = models.TextField(default='', blank=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=30, default='')
    category_id = models.ForeignKey(Category)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, default='')
    manufacturer = models.CharField(max_length=40, default='', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.CharField(max_length=255, default='none')
    description = models.TextField(default='', blank=True)
    subcategory_id = models.ForeignKey(SubCategory)

    def __str__(self):
        return self.name


class Client(models.Model):
    firstname = models.CharField(max_length=20, default='')
    lastname = models.CharField(max_length=30, default='')
    username = models.CharField(max_length=20, default='')  # будет обязательным
    password = models.CharField(max_length=20)  # Надо узнать как сделать шифрование пароля, чтоб не хранить его в базе в явном виде
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=13, default='', blank=True)
    address = models.TextField(max_length=300, default='', blank=True)

    def __str__(self):
        return self.username


class Order(models.Model):
    client_id = models.ForeignKey(Client)
    orderdate = models.DateTimeField()

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

    ordercost = models.DecimalField(max_digits=8, decimal_places=2,
                                    default=0)  # , editable=False

    def __str__(self):
        if self.status == 'Open':
            return '{0.id}: {0.status}'.format(self)
        else:
            return '{0.id}: {0.status} = {0.ordercost}'.format(self)


class OrderItem(models.Model):
    order_id = models.ForeignKey(Order)
    product_id = models.ForeignKey(Product)
    quantity = models.SmallIntegerField()

    def __str__(self):
        return '{0.id}: {1.name} x {2.quantity}'.format(self.order_id, self.product_id, self)


class New(models.Model):
    newsheader = models.CharField(max_length=30)
    newstext = models.TextField(default='')
    newsdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.newsheader
