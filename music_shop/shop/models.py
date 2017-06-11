from django.db import models


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=30, default='none')
    description = models.TextField(default='none')

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    subcategory_id = models.AutoField(primary_key=True)
    subcategory_name = models.CharField(max_length=30, default='none')
    category_id = models.ForeignKey(Category)

    def __str__(self):
        return self.subcategory_name


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='noname')
    manufacturer = models.CharField(max_length=40, default='noname')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.CharField(max_length=255, default='none')
    description = models.TextField(default='none')
    subcategory_id = models.ForeignKey(SubCategory)

    def __str__(self):
        return self.name


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=20, default='none')
    lastname = models.CharField(max_length=30, default='none')
    username = models.CharField(max_length=20, default='none')  # будет обязательным
    password = models.CharField(max_length=20)  # Надо узнать как сделать шифрование пароля, чтоб не хранить его в базе в явном виде
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=13, default='none')
    address = models.TextField(default='none')

    def __str__(self):
        return self.username


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    orderdate = models.DateTimeField()
    ordercost = models.DecimalField(max_digits=8, decimal_places=2)
    client_id = models.ForeignKey(Client)

    order_open = 'order_open'
    order_done = 'order_done'
    order_canceled = 'order_canceled'

    options = (
        (order_open, 'Open'),
        (order_done, 'Done'),
        (order_canceled, 'Canceled'),
    )
    status = models.CharField(max_length=14,
                              choices=options,
                              default=order_open)

    def __str__(self):
        return self.order_id


class OrderItem(models.Model):
    orderitem_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order)
    product_id = models.ForeignKey(Product)
    quantity = models.SmallIntegerField()

    def __str__(self):
        return self.orderitem_id


class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    newsheader = models.CharField(max_length=30)
    newstext = models.TextField(default='none')
    newsdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.newsheader
